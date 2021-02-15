
#a shorter way to use openssl for https, mimics telnet syntax
#	(remember: use port 443 instead of 80 for https connections)
function https() {

        if (($# == 2)); then
                openssl s_client -connect $1:$2
        else
                echo invalid arguments
        fi

}
