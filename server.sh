#!/bin/sh

. .venv/bin/activate
python -m http.server 8000 --bind 127.0.0.1 --directory source/_site/html

