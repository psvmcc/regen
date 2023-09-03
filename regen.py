#!/usr/bin/env python3

import os
import re
import requests
import argparse
import yaml
import www_authenticate
import hashlib
import time

APP_NAME = "regen"

parser = argparse.ArgumentParser(
    description="regen - Registry RAW data generator",
    add_help=True,
)
parser.add_argument(
    "-c",
    dest="config",
    help="Config path (default: %(default)s)",
    default="config_example.yaml",
)
parser.add_argument(
    "-d",
    dest="data_path",
    help="Data path (default: %(default)s)",
    default="/tmp/regen_data",
)
parser.add_argument(
    "-v",
    dest="verbose",
    help="Verbosity",
    action="store_true",
)
args = parser.parse_args()


def read_config(path):
    if not os.path.isfile(path):
        print("Config file not found: %s" % path)
        exit(1)
    with open(path, "r") as stream:
        try:
            d = yaml.safe_load(stream)
            return d
        except yaml.YAMLError as e:
            print("Read config error", e)
            exit(1)


def get_tags(url, basic_auth=None):
    headers = {"User-Agent": APP_NAME}
    token = None
    tags = []
    url_prefix = url.split("/v2/")[0]
    response = requests.get(url, headers=headers, auth=basic_auth)
    if response.status_code == 200:
        tags = response.json()["tags"]
        while "next" in response.links:
            url = url_prefix + response.links["next"]["url"]
            response = requests.get(url, headers=headers, auth=basic_auth)
            tags += response.json()["tags"]
    if response.status_code not in [200, 401]:
        print("Wrong exit code:", response.status_code)
        exit(1)
    if response.status_code == 401 and "www-authenticate" in response.headers:
        parsed = www_authenticate.parse(response.headers["WWW-Authenticate"])
        if "bearer" in parsed:
            auth_url = "%s?service=%s&scope=%s" % (
                parsed["bearer"]["realm"],
                parsed["bearer"]["service"],
                parsed["bearer"]["scope"],
            )
            auth_response = requests.get(auth_url, headers=headers, auth=basic_auth)
            if auth_response.status_code != 200:
                print(
                    "Wrong exit code:",
                    response.status_code,
                    auth_url,
                    auth_response.headers,
                )
                exit(1)
            token = auth_response.json()["token"]
            headers["Authorization"] = "Bearer %s" % token
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print("Wrong exit code 1:", response.status_code, auth_url)
                exit(1)
            tags = response.json()["tags"]
            while "next" in response.links:
                url = url_prefix + response.links["next"]["url"]
                response = requests.get(url, headers=headers)
                tags += response.json()["tags"]
        else:
            print("Unsupported Auth method: %s" % url)
            exit(1)
    elif response.status_code == 401:
        print("Unknown Auth method: %s" % url)
        exit(1)
    return tags, token


def get_manifest(
    scheme, registry, image, image_prefix, tag, token=None, basic_auth=None
):
    headers = {"User-Agent": APP_NAME}
    url = "%s://%s/v2/%s/manifests/%s" % (scheme, registry, image, tag)
    image_name = "%s/%s" % (image_prefix, image)
    headers[
        "Accept"
    ] = "application/vnd.docker.distribution.manifest.v2+json, application/vnd.docker.distribution.manifest.list.v2+json, application/vnd.oci.image.index.v1+json, application/vnd.oci.image.manifest.v1+json"
    if token:
        headers["Authorization"] = "Bearer %s" % token
        basic_auth = None

    response = requests.get(url, headers=headers, auth=basic_auth)
    i = 0
    if response.status_code == 429:
        while response.status_code != 200 and i != 10:
            time.sleep(5)
            if args.verbose:
                print("> loop [1]:", i, "code:", response.status_code)
            response = requests.get(url, headers=headers, auth=basic_auth)
            i += 1
        if response.status_code == 429:
            print("* ERROR[429]:", response.json()["errors"][0]["message"])
            return False

    if response.status_code != 200:
        print("* wrong exit code 1:", response.status_code)
        print(response.headers)
        print(response.json())
        return False

    blob_file_name = ""
    manifest_digest = ""
    if (
        response.headers["Content-Type"] == "application/vnd.oci.image.index.v1+json"
        or response.headers["Content-Type"]
        == "application/vnd.docker.distribution.manifest.list.v2+json"
    ):
        for manifest in response.json()["manifests"]:
            if (
                manifest["platform"]["architecture"] == "amd64"
                and manifest["platform"]["os"] == "linux"
            ):
                manifest_digest = manifest["digest"]
                url = "%s://%s/v2/%s/manifests/%s" % (
                    scheme,
                    registry,
                    image,
                    manifest_digest,
                )
        response = requests.get(url, headers=headers, auth=basic_auth)
        i = 0
        if response.status_code == 429:
            while response.status_code != 200 and i != 10:
                time.sleep(5)
                if args.verbose:
                    print("> loop [2]:", i, "code:", response.status_code)
                response = requests.get(url, headers=headers, auth=basic_auth)
                i += 1
            if response.status_code == 429:
                print(response.json()["errors"][0]["message"])
                return False
        if response.status_code != 200:
            print("* wrong exit code 2:", response.status_code)
            print(response.headers)
            print(response.json())
            return False

    if response.json()["schemaVersion"] != 2:
        print("* Wrong schema version")
        return False

    if (
        response.headers["Content-Type"]
        == "application/vnd.docker.distribution.manifest.v2+json"
    ):
        manifest_digest = response.headers["Docker-Content-Digest"]

    blob_file_name = "%s/docker/registry/v2/blobs/sha256/%s/%s/data" % (
        args.data_path,
        manifest_digest.split(":")[1][:2],
        manifest_digest.split(":")[1],
    )
    if not os.path.exists(os.path.dirname(blob_file_name)):
        os.makedirs(os.path.dirname(blob_file_name))
    with open(blob_file_name, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    layers = ["sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"]
    layers.append(response.json()["config"]["digest"])
    for layer in response.json()["layers"]:
        layers.append(layer["digest"])

    for layer in layers:
        layer_link_file_name = (
            "%s/docker/registry/v2/repositories/%s/_layers/sha256/%s/link"
            % (
                args.data_path,
                image_name,
                layer.split(":")[1],
            )
        )
        if not os.path.exists(os.path.dirname(layer_link_file_name)):
            os.makedirs(os.path.dirname(layer_link_file_name))
        with open(layer_link_file_name, "w") as f:
            f.write(layer)

        blob_file_name = "%s/docker/registry/v2/blobs/sha256/%s/%s/data" % (
            args.data_path,
            layer.split(":")[1][:2],
            layer.split(":")[1],
        )
        if os.path.exists(blob_file_name):
            sha256_hash = hashlib.sha256()
            with open(blob_file_name, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            if sha256_hash.hexdigest() == layer.split(":")[1]:
                if args.verbose:
                    print("> found local blob:", blob_file_name)
                continue

        blob_url = "%s://%s/v2/%s/blobs/%s" % (scheme, registry, image, layer)
        if "Accept" in headers:
            headers.pop("Accept")
        if args.verbose:
            print("> downloading blob:", blob_url)
        blob_response = requests.get(blob_url, headers=headers, auth=basic_auth)
        if response.status_code != 200:
            print("Wrong blob response code:", response.status_code)

        if not os.path.exists(os.path.dirname(blob_file_name)):
            os.makedirs(os.path.dirname(blob_file_name))
        with open(blob_file_name, "wb") as f:
            for chunk in blob_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    manifest_files = []
    manifest_files.append(
        "%s/docker/registry/v2/repositories/%s/_manifests/tags/%s/current/link"
        % (args.data_path, image_name, tag)
    )
    manifest_files.append(
        "%s/docker/registry/v2/repositories/%s/_manifests/tags/%s/index/sha256/%s/link"
        % (
            args.data_path,
            image_name,
            tag,
            manifest_digest.split(":")[1],
        )
    )
    manifest_files.append(
        "%s/docker/registry/v2/repositories/%s/_manifests/revisions/sha256/%s/link"
        % (
            args.data_path,
            image_name,
            manifest_digest.split(":")[1],
        )
    )
    for file in manifest_files:
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        with open(file, "w") as f:
            f.write(manifest_digest)
    return True


def main():
    cfg = read_config(args.config)
    exit_code = 0
    failed_syncs = []
    for item in cfg["registries"]:
        params = cfg["registries"][item]
        registry = params["url"]
        image_prefix = ""
        if "image_prefix" in params:
            image_prefix = params["image_prefix"]
        scheme = "http" if "insecure" in params and params["insecure"] else "https"
        if "auth" in params:
            basic_auth = (params["auth"]["login"], params["auth"]["password"])
        for image in params["images"]:
            print("[%s] Processing image: %s/%s" % (item, registry, image))
            tags_list_url = "%s://%s/v2/%s/tags/list" % (scheme, registry, image)
            if "auth" in params:
                registry_tags, token = get_tags(tags_list_url, basic_auth)
            else:
                registry_tags, token = get_tags(tags_list_url)
            tags = []
            if "tags" in params["images"][image]:
                tags = params["images"][image]["tags"]
            if "regexp" in params["images"][image]:
                tags += list(
                    filter(
                        lambda tag: re.match(params["images"][image]["regexp"], tag),
                        registry_tags,
                    )
                )
            print(
                "[%s] Image tags: %s/%s: %s" % (item, registry, image, ", ".join(tags))
            )
            for tag in tags:
                print(
                    "[%s] Processing image tag: %s/%s:%s" % (item, registry, image, tag)
                )
                if "auth" in params:
                    get_manifest(
                        scheme, registry, image, image_prefix, tag, token, basic_auth
                    )
                else:
                    if not get_manifest(
                        scheme, registry, image, image_prefix, tag, token
                    ):
                        exit_code = 1
                        failed_syncs.append(
                            "[%s] %s/%s:%s" % (item, registry, image, tag)
                        )
    if exit_code == 1:
        print("\nSync failed for next images:")
        print("\n".join(failed_syncs))
    exit(exit_code)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        exit(130)
