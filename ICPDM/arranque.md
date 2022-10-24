# Arranque del sistema hadoop

```powershell
docker-compose -f .\hadoop.yml up -d
```

## WebUI de la arquitectura

- [Hadoop](http://localhost:8088/cluster)
- [Jupyter](http://localhost:8889/tree?)
- [HDFS](http://localhost:9870/dfshealth.html#tab-overview)

## Abrir terminal en uno de los nodos de la arquitectura

```powershell
docker container exec -ti namenode /bin/bash
```

Debemos cambiar donde pone _namecode_ por uno de los nombres de los nodos esclavo

## Parar ejecución

```powershell
docker-compose -f nombrefichero.yml down
```
