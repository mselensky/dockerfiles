FROM mambaorg/micromamba:1.5.8-jammy
ARG DEBIAN_FRONTEND=noninteractive

# build environment from yml
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yaml /tmp/env.yaml
RUN micromamba clean --all --yes
RUN micromamba install -y -n base -f /tmp/env.yaml
RUN micromamba clean --all --yes

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
