
### 1
$ git ls-files
.gitignore
compose/.gitkeep
docs/diagrams/.gitkeep
evidence/step1-dmacv3.md
k8s/base/.gitkeep
k8s/overlays/.gitkeep
scripts/.gitkeep
services/firstService/Dockerfile
services/firstService/app.py
services/firstService/requirements.txt
terraform/.gitkeep

[exit 0]

### 1
$ git status --short --ignored
?? services/membership/
!! evidence.md

[exit 0]

### 2
$ git log --stat -1 -- services/membership
commit 589aad0c671942f4864d15751168fcac4b517d8e
Author: devBurton <dev.burton21@gmail.com>
Date:   Sun Nov 1 17:49:29 2026 -0500

    Add membership service

 services/membership/app.py           | 65 ++++++++++++++++++++++++++++++++++++
 services/membership/requirements.txt |  3 ++
 2 files changed, 68 insertions(+)

[exit 0]

### 3
$ docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS                   PORTS                                         NAMES
d56a5e1a9676   project/membership:v1   "uvicorn app:app --h…"   7 seconds ago   Up 6 seconds (healthy)   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   step1

[exit 0]

### 3
$ docker exec step1 id
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)

[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/10
HTTP/1.1 200 OK
date: Sun, 01 Nov 2026 22:51:22 GMT
server: uvicorn
content-length: 21
content-type: application/json

{"n":10,"result":100}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/compute/abc
HTTP/1.1 422 Unprocessable Content
date: Sun, 01 Nov 2026 22:51:22 GMT
server: uvicorn
content-length: 146
content-type: application/json

{"detail":[{"type":"int_parsing","loc":["path","n"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/orders -X POST -H content-type:\ application/json -d \{\"club_id\":\ 1\,\ \"student_name\":\ \"Test\ Student\"\,\ \"student_email\":\ \"student@example.edu\"\}
HTTP/1.1 201 Created
date: Sun, 01 Nov 2026 22:51:22 GMT
server: uvicorn
content-length: 81
content-type: application/json

{"club_id":1,"student_name":"Test Student","student_email":"student@example.edu"}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/orders -X POST -H content-type:\ application/json -d \{\"club_id\":\ 0\,\ \"student_name\":\ \"A\"\,\ \"student_email\":\ \"student@example.edu\"\}
HTTP/1.1 422 Unprocessable Content
date: Sun, 01 Nov 2026 22:51:22 GMT
server: uvicorn
content-length: 267
content-type: application/json

{"detail":[{"type":"greater_than","loc":["body","club_id"],"msg":"Input should be greater than 0","input":0,"ctx":{"gt":0}},{"type":"string_too_short","loc":["body","student_name"],"msg":"String should have at least 2 characters","input":"A","ctx":{"min_length":2}}]}
[exit 0]

### 3
$ curl -s -i http://localhost:8000/health
HTTP/1.1 200 OK
date: Sun, 01 Nov 2026 22:51:22 GMT
server: uvicorn
content-length: 121
content-type: application/json

{"status":"healthy","timestamp":"2026-11-01T22:51:22.367567+00:00","hostname":"d56a5e1a9676","environment":"development"}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.1.0 -e ENVIRONMENT=staging project/membership:v1
c8d4fab23856caf1a9433168ed30459c443b35ccee86bee9995ecf58b7bbe11d

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"Club Membership Service","version":"2.1.0","environment":"staging","hostname":"c8d4fab23856","docs":"/docs"}
[exit 0]

### 3
$ docker run -d --name step1 -p 8000:8000 -e APP_VERSION=2.2.0 -e ENVIRONMENT=production project/membership:v1
ebc242a74777ccb9af2e61df99c460897f82ab4d3332332b54e4a70db5aa1119

[exit 0]

### 3
$ curl -s http://localhost:8000/
{"app":"Club Membership Service","version":"2.2.0","environment":"production","hostname":"ebc242a74777","docs":"/docs"}
[exit 0]

### 3
$ docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS                   PORTS                                         NAMES
ebc242a74777   project/membership:v1   "uvicorn app:app --h…"   8 seconds ago   Up 8 seconds (healthy)   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   step1

[exit 0]

### 3
$ docker exec step1 id
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)

[exit 0]

### 2
$ git log --stat -1 -- services/membership
commit 8f379c6646b27fbdf0b4001e8dc6a6aafc8684c2
Author: devBurton <dev.burton21@gmail.com>
Date:   Sun Nov 1 18:04:19 2026 -0500

    Devon step 1

 services/membership/Dockerfile       | 35 +++++++++++++++++++
 services/membership/app.py           | 65 ++++++++++++++++++++++++++++++++++++
 services/membership/requirements.txt |  3 ++
 3 files changed, 103 insertions(+)

[exit 0]
