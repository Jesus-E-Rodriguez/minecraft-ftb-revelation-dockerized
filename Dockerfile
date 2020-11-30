# Taken partly from https://hub.docker.com/r/jonasbonno/ftb-revelation/dockerfile
FROM openjdk:8-jre

# Updating container
RUN apt-get update && \
	apt-get install apt-utils --yes && \
	apt-get upgrade --yes --allow-remove-essential && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Setting workdir
WORKDIR /minecraft

# Copy files over
COPY . .

# Create world directory
RUN mkdir -p /minecraft/world

# Set up scripts
RUN sed -i 's/\r$//g' test
RUN chmod +x test

RUN sed -i 's/\r$//g' start
RUN chmod +x start

# Create EULA
RUN echo "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula)." > eula.txt && \
	echo "$(date)" >> eula.txt && \
	echo "eula=TRUE" >> eula.txt

# Run tests
RUN ./test