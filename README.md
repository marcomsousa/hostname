# Simple image that returns the container ID on http get

This is a minimalist flask app that returns the container ID via HTTP GET.

Based on [Alpine Linux](https://alpinelinux.org/), so the image is quite small.

Run the Docker container using the command shown below.

```bash
$ docker run -d --name hostname -p 5000:5000 marcomsousa/hostname
```

Run in a Docker Swarm Cluster with replicas

```bash
$ docker service create \
--name hostname \
--publish 5000:5000 \
--replicas 5 \
marcomsousa/hostname
```
