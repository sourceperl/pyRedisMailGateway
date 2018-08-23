# pyRedisMailGateway
A Gateway between Redis (pub/sub) and IMAP/SMTP mail protocols


### Setup redis

    sudo apt-get install redis-server
    # edit config file /etc/redis/redis.conf
    # for use with pi SD card, we need to reduce backup cycle
    # -> here we use only "save 3600 1"

### Copy config file (URL, API credentials, misc...)

    # edit home/pi/.mail_gateway_config_sample with credentials
    # save as .dashboard_config
    cp home/pi/.mail_gateway_config /home/pi/

### Setup

    sudo pip3 install -r requirements.txt
    sudo cp -r scripts/* /usr/local/bin/

### Setup supervisor

    sudo apt-get install supervisor
    # copy conf
    sudo cp etc/supervisor/conf.d/mail_gateway.conf /etc/supervisor/conf.d/
    # reload conf
    sudo supervisorctl update