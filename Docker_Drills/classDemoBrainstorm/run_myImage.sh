#!/usr/bin/env bash

IMAGE_NAME="python-anant-image9"
VERSION="1.2.1"
CONTAINER_NAME="python-testing15"
LABEL_DESCRIPTION="testing the container image"
echo "IMAGE_NAME=${IMAGE_NAME}"
echo "CONTAINER_NAME=${CONTAINER_NAME}"
echo "LABEL_DESCRIPTION=${LABEL_DESCRIPTION}"
echo "VERSION=${VERSION}"
# exit 1

# docker build -t ${IMAGE_NAME}:${VERSION} .

docker run -it --name $CONTAINER_NAME \
              --label owner=$USER \
              --label description="${LABEL_DESCRIPTION}" \
                ${IMAGE_NAME}:${VERSION} bash -c "python3 main.py; exec bash"
