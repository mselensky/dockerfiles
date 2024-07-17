FROM mambaorg/micromamba
ARG DEBIAN_FRONTEND=noninteractive

# build environment from yml
COPY --chown=$MAMBA_USER:$MAMBA_USER openbabel-env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
