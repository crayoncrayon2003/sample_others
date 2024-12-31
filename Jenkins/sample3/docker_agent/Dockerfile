FROM jenkins/inbound-agent:alpine

USER root

# Update the package list and install Python3 and pip
RUN apk update && \
    apk add --no-cache python3 py3-pip

USER jenkins

