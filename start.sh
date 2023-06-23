#!/bin/bash
name="webapp"
docker rm $(docker ps -aq --filter name=$name)
docker rmi $name

docker build -t $name .
docker run -dp 5000:5000 --name $name $name
