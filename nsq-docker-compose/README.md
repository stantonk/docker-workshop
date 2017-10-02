Set of containers providing a fully working nsqd
-----------------

* start the 3 nsq containers defined in `docker-compose.yml`

```
docker-compose up -d
```

* see that they're running, ports are exposed/mapped to the host machine

```
docker ps
```

or you can also use `docker-compose ps` to scope to only those
containers.

* check out the admin running in the browser at [http://localhost:4171/]()

* run our infinite-loop container (another example in this repo), and pipe it's messages to a topic on our dockerized nsq setup:

``` 
docker run loop | to_nsq --topic demo --nsqd-tcp-address 127.0.0.1:4150
```

* open [http://localhost:4171/topics/demo]() and watch the message counts tick up.

* in another terminal window, run:

```
nsq_tail --topic demo --nsqd-tcp-address 127.0.0.1:4150
```

# notice i haven't installed...anything!

* stop the nsq containers

```
docker-compose stop
```
* and see that they aren't running anymore:

```
docker ps
``` 

* but see that they do still exist! they're just stopped.

```
docker ps -a | grep nsqdockercompose
```

refresh [http://localhost:4171/topics/demo]() to see that it is down.

* now let's start the nsq containers again, but this time we'll do it in the foreground so you can see their logging:

```
docker-compose up
```

* now refresh [http://localhost:4171/topics/demo](). the `demo` topic is still there! they persist...how is this possible? it's because your container, when stopped, [is nothing *but* data](https://docs.docker.com/engine/faq/#do-i-lose-my-data-when-the-container-exits)! Bear in mind though, this is not something to rely upon in production, if you really need persistent state, use a database that your containerized app/service stores information to.

By the way, use ctrl-c to stop te docker-compose stuff running in the foreground :).

* lets clean up completely; if we start it up again now, topics will be gone

```
docker-compose rm
```