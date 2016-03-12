#!/bin/bash
./mange.py syncdb
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo service nginx restart
sudo service gunicorn restart
