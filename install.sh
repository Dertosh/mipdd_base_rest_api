#!/bin/bash
myproject="mipdd_base_rest_api"
virtualenv /opt/$myproject_env
source /opt/$myproject_env/bin/activate
pip3 install -r $myproject/req.txt
cpus=$(cat /proc/cpuinfo | grep processor | wc -l)
echo "workers = $cpus" > $myproject/gunicorn.conf.py
#mkdir /opt/$myproject/$myproject
cp $myproject /opt/$myproject_env
cp $myproject.conf /etc/supervisor/conf.d/
sudo update-rc.d supervisor enable
sudo service supervisor start