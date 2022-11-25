ARG BASE_PYTHON_IMAGE=python:3.11-alpine
ARG TARGETOS=linux
ARG TARGETARCH=amd64
ARG VERSION

FROM bufbuild/buf:1.9.0 as buf
WORKDIR /workspace
COPY ../api/proto /workspace
RUN buf generate --include-imports .

FROM ${BASE_PYTHON_IMAGE} as runtime

LABEL org.opencontainers.image.source="https://github.com/raptor-ml/raptor"
LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.url="https://raptor.ml"
LABEL org.opencontainers.image.title="Raptor Runtime"
LABEL org.opencontainers.image.description="Raptor Runtime is a sidecar that provides tooling for Raptor extensions"

RUN pip install --upgrade pip

WORKDIR /runtime
COPY . /runtime
COPY --from=buf /workspace/gen/python /runtime/proto
COPY ../labsdk/raptor/program.py .

RUN pip install -r requirements.txt

RUN GRPC_HEALTH_PROBE_VERSION=v0.4.14 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-${TARGETOS}-${TARGETARCH} && \
    chmod +x /bin/grpc_health_probe

CMD [ "python", "./runtime.py" ]