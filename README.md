# regen - container registry mirroring

Doesn't support garbage collection for non config local images.

## requirements
```
pip install www_authenticate
```

## help

### regen
```
$ ./regen.py -h                                                                                                                                                         ⨯(1.185s)
usage: regen.py [-h] [-c CONFIG] [-d DATA_PATH] [-v]

regen - Registry RAW data generator

options:
  -h, --help    show this help message and exit
  -c CONFIG     Config path (default: config_example.yaml)
  -d DATA_PATH  Data path (default: /tmp/regen_data)
  -v            Verbosity
```
### regview
```
$ ./regview.py -h                                                                                                                                                                                                       ✓(25.247s)
usage: regview.py [-h] [-u URL]

regview - Registry viewer

options:
  -h, --help  show this help message and exit
  -u URL      Registry host (default: http://localhost:5000)
```

## sync

### first run with verbosity
```
$ time ./regen.py -v
[local] Processing image: 192.168.1.10:5000/some_image
[local] Image tags: 192.168.1.10:5000/some_image: latest
[local] Processing image tag: 192.168.1.10:5000/some_image:latest
> downloading blob: http://192.168.1.10:5000/v2/some_image/blobs/sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4
> downloading blob: http://192.168.1.10:5000/v2/some_image/blobs/sha256:6e0da8412a07eb5e5b51d640a9b7aa83d52520fc3070e90df180365de5118831
> downloading blob: http://192.168.1.10:5000/v2/some_image/blobs/sha256:7264a8db6415046d36d16ba98b79778e18accee6ffa71850405994cffa9be7de
> downloading blob: http://192.168.1.10:5000/v2/some_image/blobs/sha256:5d3bef190674697b771adeb8c3a02be0c10979f678b04493863f83d57d658561
> downloading blob: http://192.168.1.10:5000/v2/some_image/blobs/sha256:a2eebff772ba0856bb71f404a31148dfb65c227d4d980a66808d9012fc3bc50b
[dockerhub] Processing image: registry-1.docker.io/library/nginx
[dockerhub] Image tags: registry-1.docker.io/library/nginx: latest, 1.24.0
[dockerhub] Processing image tag: registry-1.docker.io/library/nginx:latest
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:eea7b3dcba7ee47c0d16a60cc85d2b977d166be3960541991f3e6294d795ed24
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:52d2b7f179e32b4cbd579ee3c4958027988f9a8274850ab0c7c24661e3adaac5
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:fd9f026c631046113bd492f69761c3ba6042c791c35a60e7c7f3b8f254592daa
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:055fa98b43638b67d10c58d41094d99c8696cc34b7a960c7a0cc5d9d152d12b3
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:96576293dd2954ff84251aa0455687c8643358ba1b190ea1818f56b41884bdbd
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:a7c4092be9044bd4eef78f27c95785ef3a9f345d01fd4512bc94ddaaefc359f4
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:e3b6889c89547ec9ba653ab44ed32a99370940d51df956968c0d578dd61ab665
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:da761d9a302b21dc50767b67d46f737f5072fb4490c525b4a7ae6f18e1dbbf75
[dockerhub] Processing image tag: registry-1.docker.io/library/nginx:1.24.0
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:bf09be6b0005cc81d4cc3c3cf836c84450e92a7c4dcb2e2e31d84843ff3d6c62
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:14726c8f78342865030f97a8d3492e2d1a68fbd22778f9a31dc6be4b4f12a9bc
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:e9fb7216ffafb1d000e09c25596de179b1ca2cb91aa582f09f1fd0b60208b735
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:c2cdfba273c9e338b42f20a23be9a3839fd07e81a9d3fbb4190aab8b4c1f51d2
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:68e1b6578e77816a63347c3aa8bd0832df52be412e8292c1258715bde7bac4f2
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:9f850bbc16d46b9602f17c3e5db3a671058b3c65371e59476ca81164ceb6021a
> downloading blob: https://registry-1.docker.io/v2/library/nginx/blobs/sha256:c1258e81cd034611c756c54f9714e000e324332d2bcc973849f2fd49a1ecf4b8
[dockerhub] Processing image: registry-1.docker.io/prom/prometheus
[dockerhub] Image tags: registry-1.docker.io/prom/prometheus: v2.25.0, v2.26.0
[dockerhub] Processing image tag: registry-1.docker.io/prom/prometheus:v2.25.0
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:a618f5685492e55adfb68a25b09f1d644d9123f204602f8617d7f2c13ec27d5e
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:e5d9363303ddee1686b203170d78283404e46a742d4c62ac251aae5acbda8df8
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:3430c2c42129e987db5d5c5434ea73f0cbb44b931719cb2072203fcc05617d54
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:2bfce3fbbe89b906553952ce16790a23390f8195454760b0c1101fb8a5defb5e
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:15a994fbbcfeb293f8a2971faf295663a278e7cb44761f6c1643382c8ba4c1ff
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:fbaf3df466ade24942d6e61356ab60846b982ae9cf554ec3f99897eec8923283
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:783f8704483c29152aee2ed7af76b45270077cde0ae0d138d7774ad243f3a977
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:9521b00d1968d10efcf261415d10ead480ec4965558e911c62de13b5cf0d817b
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:0c8d377aea78a7e1479bad35aeaa6428145c745393f72d7bf98646f314d97470
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:dda53f010c3447c8100998464c9c441389a659b24a716c70e18fb83f9ca3782c
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:e3f24c1b9efefeaee94d2d3254b8c949569592eb0fec1475a3cda1209220c989
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:bc4648b145061d9f6a3d5c9ac0f02fa5fa9251ef0f324745aa18140a858f8a23
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:4b1496283cf8cd2add387e78303e6b14ce79ec77725f77759e2d5d3e52954012
[dockerhub] Processing image tag: registry-1.docker.io/prom/prometheus:v2.26.0
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:6d6859d1a42a2395a8eacc41c718a039210b377f922d19076ebbdd74aa047e89
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/e5/e5d9363303ddee1686b203170d78283404e46a742d4c62ac251aae5acbda8df8/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/34/3430c2c42129e987db5d5c5434ea73f0cbb44b931719cb2072203fcc05617d54/data
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:7631b5d56c90119ca30db0363f22150531b61b29a63f524f5e3ff3521a9a37de
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:343e06690c48d954899aa31f2dacb85d9f95acb7a5daf478aa6437bceb7b07d8
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:dc32e90574e94359e62c4001db1c340f5ef306460162f890bfaae1bd27b83b02
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:a6d5d01cd646fe07d6e632357ba5340ea3b44c40c2445d11b1939c89c100eafe
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:832428480103e7bb766dcf6d2cc1295a88135a7827748cef367c4c41458a8eb8
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:83e775ff17684827b7bc45f6b231afcf8a96f9a11112a13a2305335502257f4b
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:1ec97f56783601768071ede391d7f3435ae163c3eb01dc403147835f11f4ac6e
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:0cdf5b797911d694b9e30eac19d5b0774b9106c3393df1e67ef14598457df1ed
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:eb7d1f2acc9f31fa9df93073dbb4464eb4c052eaee0c4858707b2b55c7094ebc
> downloading blob: https://registry-1.docker.io/v2/prom/prometheus/blobs/sha256:541ffe559bd535edab750f167d5ccc0f71275f148f9eb9d20268d70b74b4bb85
[teleport] Processing image: public.ecr.aws/gravitational/teleport-distroless
[teleport] Image tags: public.ecr.aws/gravitational/teleport-distroless: 13.1.2, 13.1.4, 13.1.5, 13.1.0, 13.1.1
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.2
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:925196ac520e3708574f00670b126d55502827cf28a1214e343f20abec398d3f
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:a7ca0d9ba68fdce7e15bc0952d3e898e970548ca24d57698725836c039086639
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:fe5ca62666f04366c8e7f605aa82997d71320183e99962fa76b3209fdfbb8b58
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:b02a7525f878e61fc1ef8a7405a2cc17f866e8de222c1c98fd6681aff6e509db
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:fcb6f6d2c9986d9cd6a2ea3cc2936e5fc613e09f1af9042329011e43057f3265
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:e8c73c638ae9ec5ad70c49df7e484040d889cca6b4a9af056579c3d058ea93f0
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:1e3d9b7d145208fa8fa3ee1c9612d0adaac7255f1bbc9ddea7e461e0b317805c
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:4aa0ea1413d37a58615488592a0b827ea4b2e48fa5a77cf707d0e35f025e613f
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:7c881f9ab25e0d86562a123b5fb56aebf8aa0ddd7d48ef602faf8d1e7cf43d8c
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:5627a970d25e752d971a501ec7e35d0d6fdcd4a3ce9e958715a686853024794a
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:96266735468f361ae6828901a80fc15a7f75e26640351df9e0f0f9824f36cf92
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:2758d0c31c8ca76c3379e7b1be20adc4144e9230873bb2c5bdb41f3691fa75bc
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:08553ba93cfea7ad45b59911d8ed0a025489e7c3623920dfda331b9a49f1e8aa
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:dfc02eb7708f919bb3b56c008561e4430ea87cd33bc93cb65c2c3c7f0908e5cf
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:52907d314ddce378f3f36e26629baef60c71d72a0620b9d31c47c8cb9de6467e
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:4eec690774a46467a912715848c71dbbdb049008b2252432155522a7f9ccfa92
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:15a3e63c40e07ab8fb8d48739906a03a2e247e5df2cd4e6c4be65c562e97b98f
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:5d5c4a057ce635c1b160eebb71fb9c5596da357167272936fa396eafa278b13d
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:e4238507b5d4ecedc303e02f92659e89878cd8c72ed77684de39edc07dd368e1
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.4
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:76f4679042c2c0fb3bc5c392bb3f00c933b3ed41ca7c02a381605588e6d23b8e
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a7/a7ca0d9ba68fdce7e15bc0952d3e898e970548ca24d57698725836c039086639/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fe/fe5ca62666f04366c8e7f605aa82997d71320183e99962fa76b3209fdfbb8b58/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/b0/b02a7525f878e61fc1ef8a7405a2cc17f866e8de222c1c98fd6681aff6e509db/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fc/fcb6f6d2c9986d9cd6a2ea3cc2936e5fc613e09f1af9042329011e43057f3265/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/e8/e8c73c638ae9ec5ad70c49df7e484040d889cca6b4a9af056579c3d058ea93f0/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/1e/1e3d9b7d145208fa8fa3ee1c9612d0adaac7255f1bbc9ddea7e461e0b317805c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4a/4aa0ea1413d37a58615488592a0b827ea4b2e48fa5a77cf707d0e35f025e613f/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/7c/7c881f9ab25e0d86562a123b5fb56aebf8aa0ddd7d48ef602faf8d1e7cf43d8c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/56/5627a970d25e752d971a501ec7e35d0d6fdcd4a3ce9e958715a686853024794a/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/96/96266735468f361ae6828901a80fc15a7f75e26640351df9e0f0f9824f36cf92/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/27/2758d0c31c8ca76c3379e7b1be20adc4144e9230873bb2c5bdb41f3691fa75bc/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/08/08553ba93cfea7ad45b59911d8ed0a025489e7c3623920dfda331b9a49f1e8aa/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/df/dfc02eb7708f919bb3b56c008561e4430ea87cd33bc93cb65c2c3c7f0908e5cf/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/52/52907d314ddce378f3f36e26629baef60c71d72a0620b9d31c47c8cb9de6467e/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4e/4eec690774a46467a912715848c71dbbdb049008b2252432155522a7f9ccfa92/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:88364459d131c41834576e5925d8bd327d82f96e768f96e43a9f34d869437fdd
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:17d6f6d2b59e62809285e587329e0d6f5747046dbe01f35bc955a28a19bf18ee
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:6ecd5b78d86dab333f6b146dd9b04fb625012b2017a3da2f86b829516dbfd1e4
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.5
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:0a781b1c113bcfba0ccb7a651707b90ac15373a092d8ebf141390b5208a0751b
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a7/a7ca0d9ba68fdce7e15bc0952d3e898e970548ca24d57698725836c039086639/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fe/fe5ca62666f04366c8e7f605aa82997d71320183e99962fa76b3209fdfbb8b58/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/b0/b02a7525f878e61fc1ef8a7405a2cc17f866e8de222c1c98fd6681aff6e509db/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fc/fcb6f6d2c9986d9cd6a2ea3cc2936e5fc613e09f1af9042329011e43057f3265/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/e8/e8c73c638ae9ec5ad70c49df7e484040d889cca6b4a9af056579c3d058ea93f0/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/1e/1e3d9b7d145208fa8fa3ee1c9612d0adaac7255f1bbc9ddea7e461e0b317805c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4a/4aa0ea1413d37a58615488592a0b827ea4b2e48fa5a77cf707d0e35f025e613f/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/7c/7c881f9ab25e0d86562a123b5fb56aebf8aa0ddd7d48ef602faf8d1e7cf43d8c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/56/5627a970d25e752d971a501ec7e35d0d6fdcd4a3ce9e958715a686853024794a/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/96/96266735468f361ae6828901a80fc15a7f75e26640351df9e0f0f9824f36cf92/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/27/2758d0c31c8ca76c3379e7b1be20adc4144e9230873bb2c5bdb41f3691fa75bc/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/08/08553ba93cfea7ad45b59911d8ed0a025489e7c3623920dfda331b9a49f1e8aa/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/df/dfc02eb7708f919bb3b56c008561e4430ea87cd33bc93cb65c2c3c7f0908e5cf/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/52/52907d314ddce378f3f36e26629baef60c71d72a0620b9d31c47c8cb9de6467e/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4e/4eec690774a46467a912715848c71dbbdb049008b2252432155522a7f9ccfa92/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:979e6fc83ef10fbf5ce0df214e286d78208c770413a92fd11b002348c970cda7
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:9744babba07e78d1dbd4a5849fac40a9c7018e39c1889b3bd02ca1558d4fcdb7
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:3bcc97400f4ad861e97a18136b536ce19d289fa21790dc171d891a41cf196fa5
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.0
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:de9a5c11a9bd1ad647ed665e0a2aade5f87d512f334ed5a19e1882e8960f6424
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a7/a7ca0d9ba68fdce7e15bc0952d3e898e970548ca24d57698725836c039086639/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fe/fe5ca62666f04366c8e7f605aa82997d71320183e99962fa76b3209fdfbb8b58/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/b0/b02a7525f878e61fc1ef8a7405a2cc17f866e8de222c1c98fd6681aff6e509db/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fc/fcb6f6d2c9986d9cd6a2ea3cc2936e5fc613e09f1af9042329011e43057f3265/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/e8/e8c73c638ae9ec5ad70c49df7e484040d889cca6b4a9af056579c3d058ea93f0/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/1e/1e3d9b7d145208fa8fa3ee1c9612d0adaac7255f1bbc9ddea7e461e0b317805c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4a/4aa0ea1413d37a58615488592a0b827ea4b2e48fa5a77cf707d0e35f025e613f/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/7c/7c881f9ab25e0d86562a123b5fb56aebf8aa0ddd7d48ef602faf8d1e7cf43d8c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/56/5627a970d25e752d971a501ec7e35d0d6fdcd4a3ce9e958715a686853024794a/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/96/96266735468f361ae6828901a80fc15a7f75e26640351df9e0f0f9824f36cf92/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/27/2758d0c31c8ca76c3379e7b1be20adc4144e9230873bb2c5bdb41f3691fa75bc/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/08/08553ba93cfea7ad45b59911d8ed0a025489e7c3623920dfda331b9a49f1e8aa/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/df/dfc02eb7708f919bb3b56c008561e4430ea87cd33bc93cb65c2c3c7f0908e5cf/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/52/52907d314ddce378f3f36e26629baef60c71d72a0620b9d31c47c8cb9de6467e/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4e/4eec690774a46467a912715848c71dbbdb049008b2252432155522a7f9ccfa92/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:b2385e9fcfefce9a65ce8d29179984556f2069aec70122a9f55b9e4f7d20595b
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:e591a087093e179a120ec1c84d50831a816c3567cb1b1361d19332f124358c5f
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:f576ed2bfbb5ef41364b5705260700dbb7035a735243fa73635f32fadb8d8826
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.1
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:cc9ad672eb41a17bd5c912dc5c889e3f86f9432635991c4fb931a9d974837187
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a7/a7ca0d9ba68fdce7e15bc0952d3e898e970548ca24d57698725836c039086639/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fe/fe5ca62666f04366c8e7f605aa82997d71320183e99962fa76b3209fdfbb8b58/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/b0/b02a7525f878e61fc1ef8a7405a2cc17f866e8de222c1c98fd6681aff6e509db/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/fc/fcb6f6d2c9986d9cd6a2ea3cc2936e5fc613e09f1af9042329011e43057f3265/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/e8/e8c73c638ae9ec5ad70c49df7e484040d889cca6b4a9af056579c3d058ea93f0/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/1e/1e3d9b7d145208fa8fa3ee1c9612d0adaac7255f1bbc9ddea7e461e0b317805c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4a/4aa0ea1413d37a58615488592a0b827ea4b2e48fa5a77cf707d0e35f025e613f/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/7c/7c881f9ab25e0d86562a123b5fb56aebf8aa0ddd7d48ef602faf8d1e7cf43d8c/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/56/5627a970d25e752d971a501ec7e35d0d6fdcd4a3ce9e958715a686853024794a/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/96/96266735468f361ae6828901a80fc15a7f75e26640351df9e0f0f9824f36cf92/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/27/2758d0c31c8ca76c3379e7b1be20adc4144e9230873bb2c5bdb41f3691fa75bc/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/08/08553ba93cfea7ad45b59911d8ed0a025489e7c3623920dfda331b9a49f1e8aa/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/df/dfc02eb7708f919bb3b56c008561e4430ea87cd33bc93cb65c2c3c7f0908e5cf/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/52/52907d314ddce378f3f36e26629baef60c71d72a0620b9d31c47c8cb9de6467e/data
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/4e/4eec690774a46467a912715848c71dbbdb049008b2252432155522a7f9ccfa92/data
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:1543960bbe23b49aa7448d161074d2beb638d15aa03cb94706c7ba9d24dfeb00
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:a8747177a88ca64c768e0beea9f9a7009020699b3bbb091c0de0f6e67ef81733
> downloading blob: https://public.ecr.aws/v2/gravitational/teleport-distroless/blobs/sha256:19c889a973560cc8555da9e340ff663209fdb06bcc21bfa3d3dbef6f412e394a
[dh_auth] Processing image: registry-1.docker.io/psvmcc/test
[dh_auth] Image tags: registry-1.docker.io/psvmcc/test: latest
[dh_auth] Processing image tag: registry-1.docker.io/psvmcc/test:latest
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://registry-1.docker.io/v2/psvmcc/test/blobs/sha256:c6a6e4c49560f092928ac932eda3f2bae078eca44b7c3123c137422039741555
> downloading blob: https://registry-1.docker.io/v2/psvmcc/test/blobs/sha256:57c14dd66db0390dbf6da578421c077f6de8e88edd0815b4caa94607ba5f4c09
[k8s-gcr] Processing image: k8s.gcr.io/pause
[k8s-gcr] Image tags: k8s.gcr.io/pause: 3.2, 3.3
[k8s-gcr] Processing image tag: k8s.gcr.io/pause:3.2
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://k8s.gcr.io/v2/pause/blobs/sha256:80d28bedfe5dec59da9ebf8e6260224ac9008ab5c11dbbe16ee3ba3e4439ac2c
> downloading blob: https://k8s.gcr.io/v2/pause/blobs/sha256:c74f8866df097496217c9f15efe8f8d3db05d19d678a02d01cc7eaed520bb136
[k8s-gcr] Processing image tag: k8s.gcr.io/pause:3.3
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://k8s.gcr.io/v2/pause/blobs/sha256:0184c1613d92931126feb4c548e5da11015513b9e4c104e7305ee8b53b50a9da
> downloading blob: https://k8s.gcr.io/v2/pause/blobs/sha256:aeab776c48375e1a61810a0a5f59e982e34425ff505a01c2b57dcedc6799c17b
[ghcr] Processing image: ghcr.io/prymitive/karma
[ghcr] Image tags: ghcr.io/prymitive/karma: v0.93, v0.108
[ghcr] Processing image tag: ghcr.io/prymitive/karma:v0.93
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:85be69da50829e64939082561410279ab2139c5af9baa104970c99906bd54a35
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:e8614d09b7bebabd9d8a450f44e88a8807c98a438a2ddd63146865286b132d1b
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:c6f4d1a13b699c8490910fd4fd6c7056b90fd0da3077e4f29b4bd27bf0bae6cd
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:ea84ff93830e2778e56c74abeefdd353752c1c225d154277584957030ec48439
[ghcr] Processing image tag: ghcr.io/prymitive/karma:v0.108
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:aae7dfd42d5e162ad47f65fe5902abef9405590d798164e2688979ed51fb7df8
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:0a602d5f6ca3de9b0e0d4d64e8857e504ec7a8c47f1ec617d82a81f6c64b0fe8
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:d7fbeaa2da3f6cfab1f394b047209b702fd611e17c7ea79027900b833ad2a771
> downloading blob: https://ghcr.io/v2/prymitive/karma/blobs/sha256:7d5bd9ff74e2a22356e9faec2f2dc8e60adf1fc89266bd9f586dbc11b6b593e4
[quay] Processing image: quay.io/coreos/flannel
[quay] Image tags: quay.io/coreos/flannel: v0.13.0, v0.14.0
[quay] Processing image tag: quay.io/coreos/flannel:v0.13.0
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:e708f4bb69e310904d564a1e67c3833d6a0428d3cf8dd9b9abba25c7aa0f3dfe
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:df20fa9351a15782c64e6dddb2d4a6f50bf6d3688060a34c4014b0d9a752eb4c
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:0fbfec51320eb750b6ad819ec263b687ca0eb5e343933719b1eab68f003d9902
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:734a6c0a0c59b39d8bffdf25355081c91d06e0bfcc19b987a773b68868e4607b
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:41745b624d5fa1cb40391316507c250bf893d7d5cdab7a85fb863451bd5ef2bc
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:feca50c5fe0530fd57bc0093325f84b52a458d427949c76a4e9b07827c981905
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:071b96dd834b1e1a80641b7f78ba8c1e951c3b58c2a54ac08131e5a6f9e4ebba
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:5154c0aa012aa834dec43364f3d00ebcaa76b5808471798fb030deaa2d3db7e9
[quay] Processing image tag: quay.io/coreos/flannel:v0.14.0
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:8522d622299ca431311ac69992419c956fbaca6fa8289c76810c9399d17c69de
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:801bfaa63ef2094d770c809815b9e2b9c1194728e5e754ef7bc764030e140cea
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:e4264a7179f61a6c110d5178ec81d1382ff3bcf8cda4dd48bb2a406893449be0
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:bc75ea45ad2ece1b1550b45f6fab3cc9708b8a3f2443ceb6b5363c104129270e
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:78648579d12a2f0722ff7b0ee415d234b21a40a20031580af44ccc66bcd1ded5
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:3393447261e4eb9fa8d3f918b1545120d1f71005f5f748ac23156a949c47899a
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/07/071b96dd834b1e1a80641b7f78ba8c1e951c3b58c2a54ac08131e5a6f9e4ebba/data
> downloading blob: https://quay.io/v2/coreos/flannel/blobs/sha256:4de2f0468a918ba83d6d975731867958acf085608a988744dc57a35a7d33ee41
[k8s] Processing image: registry.k8s.io/pause
[k8s] Image tags: registry.k8s.io/pause: 3.9
[k8s] Processing image tag: registry.k8s.io/pause:3.9
> found local blob: /tmp/regen_data/docker/registry/v2/blobs/sha256/a3/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4/data
> downloading blob: https://registry.k8s.io/v2/pause/blobs/sha256:e6f1816883972d4be47bd48879a08919b96afcd344132622e4d444987919323c
> downloading blob: https://registry.k8s.io/v2/pause/blobs/sha256:61fec91190a0bab34406027bbec43d562218df6e80d22d4735029756f23c7007

________________________________________________________
Executed in  139.41 secs    fish           external
   usr time    8.58 secs    0.12 millis    8.58 secs
   sys time    3.39 secs    2.15 millis    3.39 secs

```

### second run without verbosity:
```
$ time ./regen.py
[local] Processing image: 192.168.1.10:5000/some_image
[local] Image tags: 192.168.1.10:5000/some_image: latest
[local] Processing image tag: 192.168.1.10:5000/some_image:latest
[dockerhub] Processing image: registry-1.docker.io/library/nginx
[dockerhub] Image tags: registry-1.docker.io/library/nginx: latest, 1.24.0
[dockerhub] Processing image tag: registry-1.docker.io/library/nginx:latest
[dockerhub] Processing image tag: registry-1.docker.io/library/nginx:1.24.0
[dockerhub] Processing image: registry-1.docker.io/prom/prometheus
[dockerhub] Image tags: registry-1.docker.io/prom/prometheus: v2.25.0, v2.26.0
[dockerhub] Processing image tag: registry-1.docker.io/prom/prometheus:v2.25.0
[dockerhub] Processing image tag: registry-1.docker.io/prom/prometheus:v2.26.0
[teleport] Processing image: public.ecr.aws/gravitational/teleport-distroless
[teleport] Image tags: public.ecr.aws/gravitational/teleport-distroless: 13.1.2, 13.1.4, 13.1.5, 13.1.0, 13.1.1
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.2
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.4
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.5
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.0
[teleport] Processing image tag: public.ecr.aws/gravitational/teleport-distroless:13.1.1
[dh_auth] Processing image: registry-1.docker.io/psvmcc/test
[dh_auth] Image tags: registry-1.docker.io/psvmcc/test: latest
[dh_auth] Processing image tag: registry-1.docker.io/psvmcc/test:latest
[k8s-gcr] Processing image: k8s.gcr.io/pause
[k8s-gcr] Image tags: k8s.gcr.io/pause: 3.2, 3.3
[k8s-gcr] Processing image tag: k8s.gcr.io/pause:3.2
[k8s-gcr] Processing image tag: k8s.gcr.io/pause:3.3
[ghcr] Processing image: ghcr.io/prymitive/karma
[ghcr] Image tags: ghcr.io/prymitive/karma: v0.93, v0.108
[ghcr] Processing image tag: ghcr.io/prymitive/karma:v0.93
[ghcr] Processing image tag: ghcr.io/prymitive/karma:v0.108
[quay] Processing image: quay.io/coreos/flannel
[quay] Image tags: quay.io/coreos/flannel: v0.13.0, v0.14.0
[quay] Processing image tag: quay.io/coreos/flannel:v0.13.0
[quay] Processing image tag: quay.io/coreos/flannel:v0.14.0
[k8s] Processing image: registry.k8s.io/pause
[k8s] Image tags: registry.k8s.io/pause: 3.9
[k8s] Processing image tag: registry.k8s.io/pause:3.9

________________________________________________________
Executed in   43.53 secs    fish           external
   usr time    2.17 secs    0.10 millis    2.17 secs
   sys time    0.45 secs    1.89 millis    0.45 secs

```
As you can see, its faster, just checked and validated local manifests and blobs.

## start local registry for serve

```
docker run --rm -p 5000:5000 --name registry -v /tmp/regen_data:/var/lib/registry:ro registry:2
```

## checking

### images and tags with regview
```
$ time ./regview.py                                                                                                                                                                                                      ✓(0.173s)
localhost:5000/some_image:latest
localhost:5000/coreos/flannel:v0.13.0
localhost:5000/coreos/flannel:v0.14.0
localhost:5000/docker.io/library/nginx:1.24.0
localhost:5000/docker.io/library/nginx:latest
localhost:5000/docker.io/prom/prometheus:v2.25.0
localhost:5000/docker.io/prom/prometheus:v2.26.0
localhost:5000/docker.io/psvmcc/test:latest
localhost:5000/gravitational/teleport-distroless:13.1.0
localhost:5000/gravitational/teleport-distroless:13.1.1
localhost:5000/gravitational/teleport-distroless:13.1.2
localhost:5000/gravitational/teleport-distroless:13.1.4
localhost:5000/gravitational/teleport-distroless:13.1.5
localhost:5000/lalalala/pause:3.2
localhost:5000/lalalala/pause:3.3
localhost:5000/pause:3.9
localhost:5000/prymitive/karma:v0.108
localhost:5000/prymitive/karma:v0.93

________________________________________________________
Executed in  137.94 millis    fish           external
   usr time   72.66 millis    0.08 millis   72.58 millis
   sys time   22.73 millis    1.70 millis   21.03 millis
```

### pulling image
```
$ docker pull localhost:5000/prymitive/karma:v0.108                                                                                                                                                                      ✓(0.022s)
v0.108: Pulling from prymitive/karma
0a602d5f6ca3: Pull complete
d7fbeaa2da3f: Pull complete
7d5bd9ff74e2: Pull complete
Digest: sha256:39363ba6f62280be31e18fb548636344e48076fe156c16e0a6e504cd6e480bd9
Status: Downloaded newer image for localhost:5000/prymitive/karma:v0.108
localhost:5000/prymitive/karma:v0.108

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview localhost:5000/prymitive/karma:v0.108
```
