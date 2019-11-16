# Redis with Python

...which is useful for playing around with redis

Based off of [this blog post](https://medium.com/@mike.p.moritz/using-docker-compose-to-deploy-a-lightweight-python-rest-api-with-a-job-queue-37e6072a209b)

## Project structure

```
├── myproj_app
│   └── Dockerfile  (for jupyter)
│   └── docker-compose.yml  (for everything)
│   └── docker-compose.override.yml  (where the ports are defined so that docker-compose is more flexible)
│   └── requirements.txt  (for jupyter)
```

## How to run this

1. docker-compose build # this is optional, can go directly to #2
2. docker-compose up
3. copy/paste the token into browser running on 8888

## How to pause

*1. ^C from #1 above to pause
*1. docker-compose stop  (if was in detached mode)

## How to restart (detached) but view the logs

1. docker-compose restart
2. docker-compose logs --follow

## How to stop, delete images, but not the volumes

1. docker-compose down

## How to stop and clean out everything INCLUDING VOLUMES inside of /var/lib/docker/volumes/IMAGE_NAME

### WARNING: you probably DO NOT want to do this

1. docker-compose down -v