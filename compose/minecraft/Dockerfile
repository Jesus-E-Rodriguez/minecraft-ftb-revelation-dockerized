FROM openjdk:8-jdk-alpine

# Updating container and installing Python
RUN apk update && \
    apk upgrade && \
    apk add --no-cache --virtual=build-dependencies unzip && \
    apk add --no-cache bash && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

ENV WORKING_DIR="/minecraft"

# Setting workdir
WORKDIR $WORKING_DIR

# Copy files over
COPY ./minecraft .

COPY ./compose/minecraft/start /start
RUN chmod +u /start

COPY ./compose/minecraft/entrypoint /entrypoint
RUN chmod +u /entrypoint

# Run tests
ENTRYPOINT ["/entrypoint"]

