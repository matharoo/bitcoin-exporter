# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /bitcoin-exporter

# Copy the current directory contents into the container at /app
COPY . /bitcoin-exporter

# Install any needed packages
RUN pip install prometheus_client requests

# bitcoin-exporter expose at 8000
EXPOSE 8000

# Run bitcoin-exporter.py when the container launches
CMD ["python", "bitcoin-exporter.py"]
