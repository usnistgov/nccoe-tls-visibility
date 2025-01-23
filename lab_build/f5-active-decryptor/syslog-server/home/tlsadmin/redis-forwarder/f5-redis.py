import sys, os, redis, re, json, argparse, datetime, time, io
from collections import deque


if sys.version_info[:3] < (3,0,0):
    print('requires Python >= 3.0.0')
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

tlsKeyLogRegex ='^(.*) ### (?P<tuple>[0-9A-Za-z\.;]+) ### (?P<json>(.*))'
redisHost = 'redis.visibility.nccoe.org'
r = redis.Redis( redisHost , port=6379, ssl=True)

file = open(filename, 'r')

file.seek(0, io.SEEK_END) # skip to the end of the file so that we don't read the entire file again.

while True:

    where = file.tell()
    line = file.readline() # attempt to read the next line

    if not line:

       time.sleep(1)
       file.seek(where) # if we failed to read the next line, return back to the end of the last line

    else:
        line = line.replace("\"","")
        tlsKeyLogMatch = re.match(tlsKeyLogRegex,line)

        if tlsKeyLogMatch:

            group = tlsKeyLogMatch.group('tuple')
            client_random = group.split(';')[-1]

            json_blob = {}
            json_fields = list(map(lambda x: x.split(':'), tlsKeyLogMatch.group('json').split(',')))

            for k in json_fields:
                # use this to have uppercase hex
                # json_blob[k[0]] = k[1] if k[0] == 'MK' or k[0] == 'CETS' else k[1].upper()

                # use this to have lowercase hex
                json_blob[k[0]] = k[1]

            redis_key = "sk-cr" + client_random
            redis_field1 = "fkj"

            redis_field2 = json.dumps(json_blob)
            xadd_fields = { redis_field1 : redis_field2 }
            now = datetime.datetime.now()
            r.xadd(name = redis_key, fields = xadd_fields) # send it off to redis
            print(now.strftime("%Y-%m-%d %H:%M:%S"), redis_key)
