# 가제

*TODO*
- application name 정하기

## How to start

### Launch docker
```shell
docker-compose -p application-name -f docker/docker-compose.yml up
```

### Install dependency
```shell
poetry shell
poetry install
```

### Apply alembic revision
```shell
alembic upgrade head
```
