#!/bin/bash


#Sudo open -a Docker

# Need to add a sleep here

#Sudo docker build -t capstone/web-srv:1.0 .

# assume docker is already installed and running

# supply dir of web app with argument
if [ -z "$1" ] 
then
    echo "Usage: $0 [PATH TO WEB APP]"
else
    sudo docker run -d --name Demo -p 8080:80 -v $1:/usr/local/apache2/htdocs/ httpd:2.4
    echo "web app being hosted at\nhttp://localhost:8080/"
fi
