import os
import sys
import time
import redis

if len(sys.argv) != 2:
    print("""
      Command: python example.py [REDIS_SERVER_IP]

      Example: python example.py 192.168.1.119
      """)
    sys.exit(1)

r = redis.StrictRedis(
  host=sys.argv[1],
  port=6379,
  password=os.environ.get('REDIS_PASSWORD'),
  db=0
)
r.set('foo', 'bar')

while True:
    print('%s: %s' % (time.strftime('%H:%M:%S'), r.get('foo')))
    time.sleep(1)
