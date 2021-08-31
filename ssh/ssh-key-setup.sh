#!/bin/bash

# User Variables
netid=ate4
remoteserver=node.zoo.cs.yale.edu

# Creates an SSH key and transfers it to the remote server
echo '\n\n\n' | ssh-keygen -t rsa -b 4096
cat ~/.ssh/id_rsa.pub | ssh $netid@$remoteserver "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
