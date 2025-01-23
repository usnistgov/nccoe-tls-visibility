#!/usr/bin/env python3

import base64

import redis

from time import time
out = []

from redis.exceptions import ConnectionError, DataError, NoScriptError, RedisError, ResponseError

r = redis.Redis(host="redis.visibility.nccoe.org", port=6379,ssl=True)
keys = b'sk-cr<%client_random%>'

AVX::LOG(str(keys))
messages = r.xrange(keys, min='-')
AVX::LOG(messages)
json_data = []
for id, value in messages:
    #json_data.append({
    #    'id': id.decode(),
    #    'fkj': json.loads(value[b'fkj'].decode())
    #})
    AVX::LOG(value)
    out.append(json.loads(value[b'fkj'].decode()))
AVX::LOG(out)
if out == []:
    length = len(out)
    AVX::LOG(length)
    AVX::LOG({"error":"No data found on the client random"})
    AVX::OUTPUT({"error":"No data found on the client random","length":length})
else:
    length = len(out)
    AVX::LOG(length)
    AVX::OUTPUT({"result":out,"length":length})