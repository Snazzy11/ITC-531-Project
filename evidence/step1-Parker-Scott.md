
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
$ git log --stat -1 -- services/parker-service
commit 85ba79c797c3e720f73149f04823feb38e678bf4
Author: Parker Scott <98108108+Snazzy11@users.noreply.github.com>
Date:   Sat Oct 31 18:39:46 2026 -0400

    First service
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 services/parker-service/app.py | 34 ++++++++++++++++++++++++++++++++--
 1 file changed, 32 insertions(+), 2 deletions(-)

[exit 0]

### 3
$ docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS                    PORTS                                         NAMES
f66721268c10   project/parker-service:v1   "uvicorn app:app --h…"   19 seconds ago   Up 19 seconds (healthy)   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   step1

[exit 0]

### 3
$ docker exec step1 id
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)

[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/10
HTTP/1.1 200 OK
date: Sat, 31 Oct 2026 22:40:27 GMT
server: uvicorn
content-length: 72
content-type: application/json

{"resolution":"1280x720","frames":10,"bytes":27648000,"megabytes":27.65}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/abc
HTTP/1.1 422 Unprocessable Content
date: Sat, 31 Oct 2026 22:40:27 GMT
server: uvicorn
content-length: 146
content-type: application/json

{"detail":[{"type":"int_parsing","loc":["path","n"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}
[exit 0]

### 3
$ curl -s -i -X POST http://localhost:8000/orders -H Content-Type:\ application/json -d \{\"title\":\"Demo\ clip\"\,\"frames\":300\,\"fps\":30\}
HTTP/1.1 201 Created
date: Sat, 31 Oct 2026 22:40:27 GMT
server: uvicorn
content-length: 154
content-type: application/json

{"order_id":"db30f25c-f1ed-4969-b647-0bf8e9b30303","title":"Demo clip","frames":300,"fps":30,"duration_seconds":10.0,"bytes":829440000,"megabytes":829.44}
[exit 0]

### 3
$ curl -s -i -X POST http://localhost:8000/orders -H Content-Type:\ application/json -d \{\"title\":\"Demo\ clip\"\,\"frames\":300\,\"fps\":500\}
HTTP/1.1 422 Unprocessable Content
date: Sat, 31 Oct 2026 22:40:27 GMT
server: uvicorn
content-length: 139
content-type: application/json

{"detail":[{"type":"less_than_equal","loc":["body","fps"],"msg":"Input should be less than or equal to 120","input":500,"ctx":{"le":120}}]}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.1.0 -e ENVIRONMENT=staging project/parker-service:v1
f88f1288668a5cc4bb3d3687bb2685b47d5a3c5fd0c372bfb0568993952c2c68

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"ITC 532 Module 1 Service","version":"2.1.0","environment":"staging","hostname":"f88f1288668a","docs":"/docs"}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.2.0 -e ENVIRONMENT=production project/parker-service:v1
e04df9b97c6b6131d2aae0507b59e1138cf87ccebdc30084e33a66efe8bf214c

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"ITC 532 Module 1 Service","version":"2.2.0","environment":"production","hostname":"e04df9b97c6b","docs":"/docs"}
[exit 0]

### 2
$ git log --stat -1 -- services/directory
commit c61920ed8f3a0fb052beb3e8b019e8f26098a061
Author: Parker Scott <98108108+Snazzy11@users.noreply.github.com>
Date:   Sun Nov 1 20:08:43 2026 -0500

    First service
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 services/directory/Dockerfile       | 39 ++++++++++++++++++
 services/directory/app.py           | 80 +++++++++++++++++++++++++++++++++++++
 services/directory/requirements.txt |  3 ++
 3 files changed, 122 insertions(+)

[exit 0]

### 3
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                                         NAMES
6c37316d79f7   project/directory:v1   "uvicorn app:app --h…"   21 seconds ago   Up 21 seconds (healthy)   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   step1

[exit 0]

### 3
$ docker exec step1 id
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)

[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/10
HTTP/1.1 200 OK
date: Mon, 02 Nov 2026 01:09:08 GMT
server: uvicorn
content-length: 36
content-type: application/json

{"clubs":10,"per_page":10,"pages":1}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/abc
HTTP/1.1 422 Unprocessable Content
date: Mon, 02 Nov 2026 01:09:08 GMT
server: uvicorn
content-length: 146
content-type: application/json

{"detail":[{"type":"int_parsing","loc":["path","n"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}
[exit 0]

### 3
$ curl -s -i -X POST http://localhost:8000/orders -H Content-Type:\ application/json -d \{\"club_id\":1\,\"student_name\":\"Parker\ Scott\"\,\"student_email\":\"parker@example.edu\"\}
HTTP/1.1 201 Created
date: Mon, 02 Nov 2026 01:09:08 GMT
server: uvicorn
content-length: 100
content-type: application/json

{"status":"received","club_id":1,"student_name":"Parker Scott","student_email":"parker@example.edu"}
[exit 0]

### 3
$ curl -s -i -X POST http://localhost:8000/orders -H Content-Type:\ application/json -d \{\"club_id\":1\,\"student_name\":\"Parker\ Scott\"\,\"student_email\":\"not-an-email\"\}
HTTP/1.1 422 Unprocessable Content
date: Mon, 02 Nov 2026 01:09:08 GMT
server: uvicorn
content-length: 221
content-type: application/json

{"detail":[{"type":"string_pattern_mismatch","loc":["body","student_email"],"msg":"String should match pattern '^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$'","input":"not-an-email","ctx":{"pattern":"^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"}}]}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/directory/status
HTTP/1.1 200 OK
date: Mon, 02 Nov 2026 01:09:08 GMT
server: uvicorn
content-length: 109
content-type: application/json

{"service":"directory","status":"ok","version":"2.0.0","environment":"development","hostname":"6c37316d79f7"}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.1.0 -e ENVIRONMENT=staging project/directory:v1
cb23b8811a0e0a874fb62ca114060782ec8f05954ab43cf59f9e599c4beaa8d3

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"Club Directory Service","version":"2.1.0","environment":"staging","hostname":"cb23b8811a0e","docs":"/docs"}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.2.0 -e ENVIRONMENT=production project/directory:v1
ac4c7ab7a922c11795447811f25a318d2e520264d61bdd49ef1d074b5a5937b2

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"Club Directory Service","version":"2.2.0","environment":"production","hostname":"ac4c7ab7a922","docs":"/docs"}
[exit 0]
