#!/bin/bash

# Exit if already running
for pid in `/usr/sbin/pidof python3`; do
    if grep -q keylog2redis.py /proc/$pid/cmdline; then
        exit 0
    fi
done

# Run keylog2redis
cd $HOME
echo "---" >> /var/log/keylog2redis.log
echo "Starting keylog2redis" >> /var/log/keylog2redis.log
date >> /var/log/keylog2redis.log
echo "---" >> /var/log/keylog2redis.log
/root/keylog2redis.py >> /var/log/keylog2redis.log 2>&1 &

exit 0
