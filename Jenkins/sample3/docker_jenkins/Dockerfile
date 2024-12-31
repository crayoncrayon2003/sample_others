# Use the Jenkins LTS base image
FROM jenkins/jenkins:lts

# Switch to root user to install Docker and Python
USER root

# Install necessary dependencies and Docker
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    # curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    # add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    # apt-get install -y docker-ce-cli && \
    apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# # Install Docker Compose
# RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
#     chmod +x /usr/local/bin/docker-compose

# Create a symbolic link for python to point to python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Switch back to the Jenkins user
USER jenkins
