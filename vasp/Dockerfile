FROM ubuntu:24.04
ARG DEBIAN_FRONTEND=noninteractive

# installation reference:
# https://github.nrel.gov/nrel-cloud-computing/tco2024-data-analysis/blob/main/vasp_install.md

RUN apt-get update && \
	apt-get install git libssl-dev \
	--no-install-recommends -y
ENV GIT_SSL_NO_VERIFY=true
RUN git clone -c feature.manyFiles=true https://github.com/spack/spack.git 
ENV CWD=`pwd`,  
RUN fstr='dospack () { export SPACK_USER_CONFIG_PATH='${CWD}'/myconfig ; source '${CWD}'/spack/share/spack/setup-env.sh ; spack bootstrap root --scope defaults '${CWD}'/myboot ; }' ; eval $fstr 
RUN echo $fstr > dospack.func 
RUN cat dospack.func  

RUN dospack

RUN spack compiler find 
RUN spack install gcc 
RUN spack compiler find 
RUN spack install intel-oneapi-compilers 
RUN spack install intel-oneapi-mpi intel-oneapi-ccl intel-oneapi-dal intel-oneapi-dnn intel-oneapi-ipp intel-oneapi-ippcp intel-oneapi-mkl intel-oneapi-tbb intel-oneapi-vpl
RUN spack install hdf5%oneapi +fortran +mpi ^intel-oneapi-mpi

