# How did I dockerize?

1. Created this Dockerfile (based on .../04_data_science_essentials/Dockerfile)
2. docker build -t python-data-testing .
3. docker run -p 8888:8888 -p 9000:9000 -v $(pwd):/app python-data-testing
4. copy/paste the token into browser running on 8888

5. edit docker file so that:
```
FROM python:3.7-slim-buster
```

6. docker rm *VARIOUS IMAGES*
7. docker rmi python-data-testing:latest
8. repeat 2 thru 4

YASSS! the image was 600MB instead of 1300MB