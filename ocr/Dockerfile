FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y software-properties-common python3-pip && \
    add-apt-repository -y ppa:alex-p/tesseract-ocr && \
    apt-get update
RUN apt-get install -y tesseract-ocr-eng
RUN pip3 install meilisearch xxhash

CMD ["python3", "-u", "/work/main.py"]
