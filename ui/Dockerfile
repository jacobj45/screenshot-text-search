FROM ubuntu:18.04

RUN apt update && \
    apt install -y python3 python3-pip git
RUN pip3 install meilisearch
RUN git clone https://github.com/imjoy-team/imjoy-elfinder.git && \
    cd imjoy-elfinder && \
    git checkout ff3186c4b216c46d4ddbf38b840debdec92f3602 && \
    pip3 install -r requirements_dev.txt && \
    pip3 install -e .

COPY ./elfinder.py /imjoy-elfinder/imjoy_elfinder/elfinder.py
COPY ./elfinder-main.js /imjoy_elfinder/templates/elfinder/main.js

VOLUME /inputs
WORKDIR /inputs
EXPOSE 8765
CMD ["imjoy-elfinder", "--thumbnail", "--host", "0.0.0.0"]
