FROM ubuntu:18.04

RUN apt-get update \
  && apt-get -y install tesseract-ocr \
   && apt-get install tesseract-ocr-spa -y\
  && apt-get install -y python3.10 \
  && apt-get install -y python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]