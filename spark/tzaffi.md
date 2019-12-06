# How to run

1. docker build -t domino .
2. docker run -p 8893:8888 -v $(pwd):/app domino
3. copy/paste the token into browser running on port 8893

# Cleaning up

1. docker rm *VARIOUS IMAGES*
2. docker rmi domino:latest


