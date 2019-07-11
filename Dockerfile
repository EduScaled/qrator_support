FROM python:3.7-stretch

COPY . /app
WORKDIR /app

RUN apt-get update \
    && apt-get install -y python-dev \
                          python-pip \
                          curl \
                          vim \
                          telnet \
   && apt-get clean && rm -rf /var/lib/apt/lists/* \
   && pip install pipenv

RUN pipenv install --system

CMD ["flask", "run", "--host=0.0.0.0"]