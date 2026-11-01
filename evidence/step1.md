
### 1
$ git ls-files
.gitignore
compose/.gitkeep
docs/diagrams/.gitkeep
k8s/base/.gitkeep
k8s/overlays/.gitkeep
scripts/.gitkeep
terraform/.gitkeep

[exit 0]

### 1
$ git status --short --ignored
!! evidence.md

[exit 0]

### 2
$ git log --stat -1 -- services/firstService/
commit 4b911b3c6ed2689349cb1e722a429fc9e1c91fa5
Author: dmacv3 <lildouglasis@gmail.com>
Date:   Sun Nov 1 17:21:28 2026 -0500

    First service

 services/firstService/Dockerfile       | 39 +++++++++++++++++++++
 services/firstService/app.py           | 64 ++++++++++++++++++++++++++++++++++
 services/firstService/requirements.txt |  3 ++
 3 files changed, 106 insertions(+)

[exit 0]

### 3
$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS                   PORTS                                         NAMES
b366fd008963   project/firstservice:v1   "uvicorn app:app --h…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   step1

[exit 0]

### 3
$ docker exec step1 id
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)

[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/10
HTTP/1.1 200 OK
date: Sun, 01 Nov 2026 22:23:15 GMT
server: uvicorn
content-length: 7
content-type: application/json

3628800
[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/abc
HTTP/1.1 422 Unprocessable Content
date: Sun, 01 Nov 2026 22:23:21 GMT
server: uvicorn
content-length: 146
content-type: application/json

{"detail":[{"type":"int_parsing","loc":["path","n"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}
[exit 0]

### 3
$ curl -s -i -X POST http://localhost:8000/orders -H content-type:\ application/json -d \{\"order_id\":1\,\"item_name\":\"Burger\"\,\"order_message\":\"no\ pickles\"\}
HTTP/1.1 200 OK
date: Sun, 01 Nov 2026 22:24:10 GMT
server: uvicorn
content-length: 61
content-type: application/json

{"Ordered":"Burger","Order Number":1,"Requests":"no pickles"}
[exit 0]

### 3
$ curl -s -i -X POST http://localhost:8000/orders -H content-type:\ application/json -d \{\"order_id\":2\,\"item_name\":\"\"\,\"order_message\":\"no\ pickles\"\}
HTTP/1.1 422 Unprocessable Content
date: Sun, 01 Nov 2026 22:24:29 GMT
server: uvicorn
content-length: 149
content-type: application/json

{"detail":[{"type":"string_too_short","loc":["body","item_name"],"msg":"String should have at least 1 character","input":"","ctx":{"min_length":1}}]}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.1.0 -e ENVIRONMENT=staging project/firstservice:v1
0c98b64a89b1a7144cc11c7a0c966f8b194088503f8fb14f0aa3f05e0e8ee456

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"ITC 532 Module 1 Service","version":"2.1.0","environment":"staging","hostname":"0c98b64a89b1","docs":"/docs"}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.2.0 -e ENVIRONMENT=production project/firstservice:v1
84f5b218a313fa6af6210117131e36127dabf7b7bfc2aa641ad89f33b81cfaf7

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"ITC 532 Module 1 Service","version":"2.2.0","environment":"production","hostname":"84f5b218a313","docs":"/docs"}
[exit 0]
