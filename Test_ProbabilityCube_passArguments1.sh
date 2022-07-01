#!/bin/bash
#SBATCH -N 2
#SBATCH -C haswell
#SBATCH -q regular
#SBATCH -J No&
#SBATCH --mail-user=lianming@udel.edu
#SBATCH --mail-type=ALL
#SBATCH -t 00:02:00

#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread


#run the application:
module load python
srun -N 1 -n 1 -c 64 --cpu_bind=cores python3 /global/cscratch1/sd/lianming/Test_ProbabilityCube_passArguments.py 5 7 60 91 urY &
srun -N 1 -n 1 -c 64 --cpu_bind=cores python3 /global/cscratch1/sd/lianming/Test_ProbabilityCube_passArguments.py 5 8 60 81 ur
