FROM mambaorg/micromamba
ARG DEBIAN_FRONTEND=noninteractive

# build tensorflow environment from yml
# conda env made via (on a Kestrel GPU node): 
    # mamba create -n tensorflow-env-cuda123 conda-forge::tensorflow[build=*cuda*] nvidia/label/cuda-12.3.0::cuda
COPY --chown=$MAMBA_USER:$MAMBA_USER tensorflow-env-cuda123.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

WORKDIR "/home/mambauser"
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]