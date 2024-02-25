FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y tmux htop && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /dir1

RUN mkdir -p dir2 dir3

CMD ["/bin/bash"]
