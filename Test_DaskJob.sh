#!/bin/bash
#SBATCH -J TestDask
#SBATCH -N 1
#SBATCH -n 2
#SBATCH -C haswell
#SBATCH -q regular
#SBATCH -t 00:30:00
#SBATCH --image=stephey/nersc-dask-example:v0.6.0
#SBATCH --mail-user=lianming@udel.edu

#start your dask cluster
srun -u shifter dask-mpi --scheduler-file=$SCRATCH/scheduler.json --nthreads=1 --memory-limit='auto' --no-nanny --local-directory=/tmp &

sleep 10

#now run your dask script
srun -u shifter python /global/cscratch1/sd/lianming/Test_DaskJob.py