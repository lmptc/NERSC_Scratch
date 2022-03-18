#!/bin/bash
#SBATCH -N 1
#SBATCH -C knl
#SBATCH -q regular
#SBATCH -J Test_K_1_272
#SBATCH --mail-user=lianming@udel.edu
#SBATCH --mail-type=ALL
#SBATCH -t 02:00:00

#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread


#run the application:
srun -n 1 -c 272 --cpu_bind=cores python3 /global/cscratch1/sd/lianming/ProbabilityCube_KNLTest.py
