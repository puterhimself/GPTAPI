FROM python:3.10.6-slim

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED 1
ENV wd=/home/app/

# Create and change to the app directory.
WORKDIR ${wd}

# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.
COPY ./requirements.txt .

# Install dependencies.
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY . .
# Run the web service on container startup.
# Use gunicorn webserver with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD gunicorn --bind 0.0.0.0:8000 app:app --workers=5