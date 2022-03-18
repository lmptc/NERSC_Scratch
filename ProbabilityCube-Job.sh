#!/bin/bash
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -q regular
#SBATCH -J Obj_23
#SBATCH --mail-user=lianming@udel.edu
#SBATCH --mail-type=ALL
#SBATCH -t 06:00:00

#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread


#run the application:
srun -n 1 -c 64 --cpu_bind=cores python3 /global/cscratch1/sd/lianming/ProbabilityCube.py
