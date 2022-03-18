#!/bin/bash
#SBATCH -J Test
#SBATCH -N 1
#SBATCH -n 16
#SBATCH -C haswell
#SBATCH -q debug
#SBATCH -t 00:30:00
#SBATCH --image=stephey/nersc-dask-example:v0.6.0
#SBATCH --mail-user=lianming@udel.edu
#SBATCH --mail-type=ALL

#start your dask cluster
srun -u shifter dask-mpi --scheduler-file=$SCRATCH/scheduler.json --nthreads=1 --memory-limit=0 --no-nanny --local-directory=/tmp &

sleep 10

#now run your dask script
shifter python /global/cscratch1/sd/lianming/ProbabilityCube_forDask_Test.py