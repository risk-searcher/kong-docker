# kong-docker

A customized Kong docker pre-installed with request-firewall and flexible-rate-limit plugins

# Testbed

There is a docker-compose file inside Testbed which include the database, a echo webserver for testing, and Konga as well.

The docker-compose file uses `profiles` which requires docker-compose 1.28 which is not supported on MacOS yet.

1. Init DB

Please uncomment the `init-db` section and the run `docker-compose run init-db` to initalize the kong database

After that, you can comment the `init-db` section again.

And if you see the following error message, just run it again (timing issue)
```
Error: [PostgreSQL error] failed to retrieve PostgreSQL server_version_num: connection refused

  Run with --v (verbose) or --vv (debug) for more details
```

2. Start the whole app

Just run `docker-compose up`, which will start database/kong/konga/echo-server

3. Login to Konga

Goto `http://localhost:1337`

Connect your Konga to Kong by url `http://kong:8001`

4. Setup a new service

- name: webserver <-- you can name it anything
- host: webserver <-- can't rename this, this is the docker name
- protocol: http
- port: 1234

5. Setup a new route

- name all-route
- hosts: localhost

6. Setup your plugin

Run `python update_kong.py` to setup your plugins


