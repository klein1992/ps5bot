# Adapted from https://sourcery.ai/blog/python-docker/
FROM python:3.9-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM selenium/standalone-chrome:88.0 AS runtime

USER root

# Install python and pipenv
RUN sudo apt-get update -y
# RUN sudo apt-get install -y software-properties-common
# RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt-get install -y python3.9 python3-pip
RUN pip3 install pipenv

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Copy scripts into final image
COPY poll.sh bestbuy-checkout.py ./
RUN chmod +x poll.sh

# Create and switch to a new user
RUN useradd appuser
USER appuser

# Run the application
ENTRYPOINT "./poll.sh"


