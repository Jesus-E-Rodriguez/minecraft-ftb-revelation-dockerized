FROM openjdk:8-jre

# Updating container
RUN apt-get update && \
	apt-get install apt-utils --yes && \
    apt-get --yes install python3 python3-pip && \
	apt-get upgrade --yes --allow-remove-essential && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Setting workdir
WORKDIR /minecraft

# Copy files over
COPY . .

# Set permissions
RUN chmod u+x test start

# Run tests
RUN ./test

