#!/bin/bash

user=xxxx	#must fill in user id

#calls ssh to connect to the Yale Zoo
function zoo() {

	if (($# < 2)); then
		ssh $user@node.zoo.cs.yale.edu
	else
		ssh $user@$1.zoo.cs.yale.edu
	fi

}


#calls sftp to connect to the Yale Zoo
function zoos() {

	sftp $user@node.zoo.cs.yale.edu

}
