#!/bin/bash
sudo sed -i '12s/Order allow,deny/Order deny,allow/' /etc/apache2/sites-enabled/000-default
sudo sed -i '13i \\t\tallow from 192.168.100.1/255.255.255.255' /etc/apache2/sites-enabled/000-default
sudo /etc/init.d/apache2 restart
