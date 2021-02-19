#!/bin/bash

# Function for generating the formatting for
# enumerability/diagonalization tables in LaTeX
function entab() {

	# Counts number of columns
	line_num=$(< "$1" wc -l)

	printf "\\\begin{tabular}{l|"
	for ((i=0 ; i <= $line_num ; i++)); do
		printf "l"
	done
	echo "}"

	# Generates top row
	while read line; do
		printf " & "
		printf "\$$line\$"
	done < $1 #horizontal axis

	echo " & \\\\ \\hline"

	# Generates middle rows
	while read vline; do

		printf "\$$vline\$"

		while read hline; do
			printf " & "
			printf "\$$vline$hline\$"
		done < $1 #horizontal axis

		echo " & \$\\cdots\$ \\\\"

	done < $2 #vertical axis

	# Generates last row
	while read line; do

		printf " & \$\\\vdots\$ "

	done < $1 #horizontal axis
	echo " & \$\\ddots\$"

	echo "\\end{tabular}"

}

