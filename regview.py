#!/usr/bin/env python3

import requests
import argparse
import www_authenticate

headers = {"User-Agent": "regview"}

parser = argparse.ArgumentParser(
    description="regview - Registry viewer",
    add_help=True,
)
parser.add_argument(
    "-u",
    dest="url",
    help="Registry host (default: %(default)s)",
    default="http://localhost:5000",
)
args = parser.parse_args()


def get_catalog():
    try:
        response = requests.get("%s/v2/_catalog" % args.url, headers=headers)
    except Exception as e:
        print("Unable to connect to", args.url, "with error:", e)
        exit(1)
    if response.status_code != 200:
        print("wrong exit code:", response.status_code)
        exit(1)
    return response.json()["repositories"]


def get_tags(url):
    token = None
    response = requests.get(url, headers=headers)
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
            auth_response = requests.get(auth_url, headers=headers)
            if auth_response.status_code != 200:
                print("Wrong exit code:", response.status_code, auth_url)
                exit(1)
            token = auth_response.json()["token"]
            headers["Authorization"] = "Bearer %s" % token
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print("Wrong exit code:", response.status_code, auth_url)
                exit(1)
        else:
            print("Unsupported Auth method: %s" % url)
            exit(1)
    elif response.status_code == 401:
        print("Unknown Auth method: %s" % url)
        exit(1)
    return response.json()["tags"], token


def main():
    repos = get_catalog()
    for repo in repos:
        registry_tags, token = get_tags("%s/v2/%s/tags/list" % (args.url, repo))
        for tag in registry_tags:
            print("%s/%s:%s" % (args.url.split("/")[-1], repo, tag))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        exit(130)
