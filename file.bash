#!/bin/bash
sudo service mysql restart
mysql -uroot -e "create database box character set utf8"
mysql -uroot -e "create user 'box@localhost'"
mysql -uroot -e "grant all privileges on box.* to 'box'"
mysql -uroot -e "SET PASSWORD FOR box = PASSWORD('boxboxbox')"
./ask/manage.py syncdb
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/ask.conf /etc/gunicorn.d/ask
sudo service nginx restart
sudo service gunicorn restart
