#!/bin/bash
#SBATCH -J 0_5_12
#SBATCH -N 11
#SBATCH -n 176
#SBATCH -C haswell
#SBATCH -q regular
#SBATCH -t 03:00:00
#SBATCH --image=stephey/nersc-dask-example:v0.6.0
#SBATCH --mail-user=lianming@udel.edu
#SBATCH --mail-type=ALL

rm -f $SCRATCH/scheduler.json

#start your dask cluster
srun -u shifter dask-mpi --scheduler-file=$SCRATCH/scheduler.json --nthreads=1 --memory-limit=0 --no-nanny --local-directory=/tmp &

sleep 10

#now run your dask script
shifter python /global/cscratch1/sd/lianming/000.py 0 6 12