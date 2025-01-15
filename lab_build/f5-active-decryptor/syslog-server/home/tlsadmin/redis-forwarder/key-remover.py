import sys, os, redis, re, json
from time import time
from collections import deque


if sys.version_info[:3] < (3,0,0):
    print('requires Python >= 3.0.0')
    sys.exit(1)

if len(sys.argv) < 1:
    sys.exit('Missing command line argument, ex. ' + os.path.basename(__file__)  + ' <tlsKeyLog.txt>')

tlsKeyLogRegex ='^(.*) ### (?P<tuple>[0-9A-Za-z\.;]+) ### (?P<json>(.*))'
redisHost = 'redis.visibility.nccoe.org'
r = redis.Redis( redisHost , port=6379, ssl=True)

for key in r.scan_iter():
    if ('_' in str(key)):
        r.delete(key)
