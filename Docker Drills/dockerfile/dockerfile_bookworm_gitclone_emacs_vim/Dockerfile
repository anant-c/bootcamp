FROM debian:bookworm-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git vim emacs

RUN git clone https://github.com/anant-c/bootcamp .

CMD ["bash"]
