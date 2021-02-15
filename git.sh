#!/bin/bash

#recursively updates each submodule of a git repository
function updatesub() {

	git submodule foreach --recursive git pull origin master

}
