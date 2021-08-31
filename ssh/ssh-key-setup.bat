Rem User Variables
set netid=ate4
set remoteserver=node.zoo.cs.yale.edu

Rem Creates an SSH key and transfers it to the remote server
echo -ne '\n\n\n' | ssh-keygen -t rsa -b 4096
cat %userprofile%/.ssh/id_rsa.pub | ssh %netid%@%remoteserver% "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
