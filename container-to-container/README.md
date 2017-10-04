This example demonstrates:

* Simplistic bootstrapping of a Python environment in a container (`Dockerfile.testrunner`)
* Inter-container communication when using `docker-compose`
* [Dealing with waiting for a container to be ready](https://docs.docker.com/compose/startup-order/) with [dockerize](https://github.com/jwilder/dockerize#waiting-for-other-dependencies). this is much more reliable and robust than shell script hacks for race conditions.
* Leveraging environment variables to share configuration information between containers spun up by `docker-compose` (e.g. hostname of database is `dev-database` defined by the `docker-compose.yml`)


### Build testrunner container
```
make
```
This builds the `testrunner` container, which houses a `fabfile.py` with a simple command that talks to the `mysql:5.7` container with a `fab` command. Note that we don't bother creating a virtualenv, since the `testrunner` container *is* an isolated environment.

### Run the set of containers
```
docker-compose up
```

### What to expect

You'll see the `testrunner` container poll every 5 seconds using dockerize waiting for the `mysql:5.7` container to finish starting up. Once MySQL finishes initializing, you'll see the `testrunner` execute a fabric command inside the container:

```
fab -f /fabfile.py query_mysql
```

which queries the `mysql:5.7` container to get a list of the databases it has, and prints it out in green:

```
$ docker-compose up

Starting containertocontainer_dev-database_1 ...
Starting containertocontainer_dev-database_1 ... done
Starting containertocontainer_testrunner_1 ...
Starting containertocontainer_testrunner_1 ... done
Attaching to containertocontainer_dev-database_1, containertocontainer_testrunner_1
...
dev-database_1  | Version: '5.7.19'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
...
testrunner_1    | 2017/10/04 01:56:03 Connected to tcp://dev-database:3306
testrunner_1    | --------------------------------------------------------------------------------
testrunner_1    | databases found:
testrunner_1    | information_schema
testrunner_1    | demo
testrunner_1    | mysql
testrunner_1    | performance_schema
testrunner_1    | sys
testrunner_1    | --------------------------------------------------------------------------------
testrunner_1    |
testrunner_1    | Done.
testrunner_1    | 2017/10/04 01:56:03 Command finished successfully.
```
