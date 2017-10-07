# nginx-static-content

Demonstrates a bare-bones configuration to show static content (html and an image). Follows the NGINX [Beginners Guide](https://nginx.org/en/docs/beginners_guide.html) (skipping over starting/stopping the service since that's handled by the base `nginx` docker image)

### build the container

```
docker build -t nginx-static-content .
```

### run it and map port 80 to the host machine

```
docker run -p80:80 nginx-static-content
```

### curl the index.html

```
$ curl -s "http://localhost"
<html>
  <head></head>
  <body>hello world</body>
</html>
```

### curl the duck.jpg

```
$  curl -s "http://localhost/images/duck.jpg" > duck.jpg && file -I duck.jpg && rm duck.jpg
duck.jpg: image/jpeg; charset=binary
```

### see the access logs printed from the running container

```
$  docker run -p80:80 nginx-static-content
172.17.0.1 - - [07/Oct/2017:15:32:14 +0000] "GET / HTTP/1.1" 200 58 "-" "curl/7.43.0"
172.17.0.1 - - [07/Oct/2017:15:34:14 +0000] "GET /images/duck.jpg HTTP/1.1" 200 386168 "-" "curl/7.43.0"
```