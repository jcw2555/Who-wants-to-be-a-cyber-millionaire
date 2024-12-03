# Use Python 2.7.16 base image (Alpine version for smaller size)
FROM python:2.7.16-alpine

# Install Python 3 and pip3
RUN apk add --no-cache python3 py3-pip

# Install build dependencies for compiling Python packages
RUN apk add --no-cache build-base python3-dev

# Create application directory
RUN mkdir /cybermillionaire

# Set the working directory inside the container
WORKDIR /cybermillionaire

# Upgrade pip for Python 2.7 and Python 3
RUN pip install --upgrade pip
RUN pip3 install --upgrade pip

# Install Python dependencies from requirements.txt using pip for Python 2.7
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install openai for Python 3 using pip3
RUN pip3 install --upgrade openai

# Copy the rest of the application files to the container
COPY ./cybermillionaire /cybermillionaire

# Copy the entrypoint.sh script to the container
COPY ./entrypoint.sh /

# Make sure entrypoint.sh is executable
RUN chmod +x /entrypoint.sh

# Set entrypoint to run the entrypoint.sh script
ENTRYPOINT ["sh", "/entrypoint.sh"]
