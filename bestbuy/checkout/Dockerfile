ARG CHROME_TAG=89.0

FROM selenium/standalone-chrome:${CHROME_TAG} as base

USER root

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Get the add-apt-repository package
RUN apt-get update -y && apt-get install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update -y && apt-get install -y \
python3.9 \
python3-pip

FROM base AS python-deps

USER seluser
# Install pipenv and compilation dependencies
WORKDIR $HOME
RUN python3.9 -m pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
ENV PATH="$HOME/.local/bin:$PATH"
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --python 3.9 --deploy

FROM base AS runtime

# Copy virtual env from python-deps stage
WORKDIR $HOME
COPY --from=python-deps $HOME/.venv ./.venv
ENV PATH="$HOME/.venv/bin:$PATH"

# Copy scripts into final image
COPY poll.sh bestbuy-checkout.py ./

USER root
RUN chmod +x poll.sh

USER seluser
# Run the application
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["python3.9 bestbuy-checkout.py"]


