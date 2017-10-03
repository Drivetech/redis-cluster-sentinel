# redis-cluster-sentinel

> Ejemplo de cluster de redis usando sentinel y haproxy

## Uso
```shell
export REDIS_PASSWORD=your-pass
docker-compose up -d
docker-compose scale slave=2 sentinel=3
```

Con lo anterior se tienen 1 master, 2 slave y 3 sentinel

Testear conexión con python

```shell
pip install redis
```
```python
import time
import os
import redis

r = redis.StrictRedis(
  host='your ip',
  port=6379,
  password=os.environ.get('REDIS_PASSWORD'),
  db=0
)
r.set('foo', 'bar')

while True:
    print('%s: %s' % (time.strftime('%H:%M:%S'), r.get('foo')))
    time.sleep(1)
```

Simular balanceo de carga

```shell
# Detener nodo master
docker-compose pause master
sleep 10
# Reanudar nodo master
docker-compose unpause master
sleep 10
# Detener nodos slave
docker-compose pause slave
sleep 10
# Reanudar nodos slave
docker-compose unpause slave
```
