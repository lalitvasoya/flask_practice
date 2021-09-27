FROM jenkins/jenkins

USER root

# Install docker

RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh

# Install docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

RUN usermod -aG docker jenkins

USER jenkins