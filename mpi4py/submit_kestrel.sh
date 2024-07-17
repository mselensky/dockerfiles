#!/bin/bash
#SBATCH -A hpcapps
#SBATCH -p debug
#SBATCH -t 00:10:00
#SBATCH -N 2
#SBATCH --ntasks-per-node=16
#SBATCH --mem-per-cpu=200M
#SBATCH --job-name="hello_mpi"
#SBATCH -o /scratch/mselensk/logs/%x-%j.out

ml restore system
ml apptainer

APPTAINER_EXEC='apptainer exec -B /scratch:/scratch mpi4py.sif'

export MAXWORKERS=`echo $(($SLURM_CPUS_ON_NODE * $SLURM_JOB_NUM_NODES))`
mpirun -n $MAXWORKERS $APPTAINER_EXEC python hello_mpi.py