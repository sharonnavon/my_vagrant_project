#!/bin/bash
sudo apt-get install sshpass ; echo "yes y | /usr/bin/ssh-keygen -b 2048 -t rsa -f /home/vagrant/.ssh/id_rsa -q -N '' > /dev/null ; /usr/bin/sshpass -p 'vagrant' /usr/bin/ssh vagrant@server2 -o StrictHostKeyChecking=no 'hostname' > /dev/null ; /usr/bin/sshpass -p 'vagrant' /usr/bin/ssh-copy-id vagrant@server2 > /dev/null " >> /home/vagrant/.profile

