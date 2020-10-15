#!/bin/bash
exec gunicorn --config /app/gunicorn.conf.py wsgi:app