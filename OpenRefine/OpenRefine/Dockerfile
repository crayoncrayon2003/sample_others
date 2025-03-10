FROM debian:latest

RUN apt-get update && apt-get install -y \
    wget \
    openjdk-17-jre \
    && rm -rf /var/lib/apt/lists/*

ENV OPENREFINE_VERSION=3.9.0
ENV OPENREFINE_URL=https://github.com/OpenRefine/OpenRefine/releases/download/${OPENREFINE_VERSION}/openrefine-linux-${OPENREFINE_VERSION}.tar.gz

RUN wget -q ${OPENREFINE_URL} -O /tmp/openrefine.tar.gz && \
    mkdir -p /opt/openrefine && \
    tar -xzf /tmp/openrefine.tar.gz -C /opt/openrefine --strip-components=1 && \
    rm /tmp/openrefine.tar.gz

WORKDIR /opt/openrefine

EXPOSE 3333

CMD ["/opt/openrefine/refine", "-i", "0.0.0.0"]
