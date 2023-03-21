FROM alpine:latest

RUN apk update

RUN echo "Hello World" > ./survfile
ENTRYPOINT cat ./survfilecat