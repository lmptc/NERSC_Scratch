#!/bin/bash
#SBATCH -J 1000_2
#SBATCH -N 20
#SBATCH -n 320
#SBATCH -C haswell
#SBATCH -q regular
#SBATCH -t 01:00:00
#SBATCH --image=stephey/nersc-dask-example:v0.6.0
#SBATCH --mail-user=lianming@udel.edu
#SBATCH --mail-type=ALL

#start your dask cluster
srun -u shifter dask-mpi --scheduler-file=$SCRATCH/scheduler.json --nthreads=1 --memory-limit=0 --no-nanny --local-directory=/tmp &

sleep 10

#now run your dask script
shifter python /global/cscratch1/sd/lianming/ProbabilityCube_forDask_2.py