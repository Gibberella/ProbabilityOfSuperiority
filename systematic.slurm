#!/bin/bash --login
#SBATCH --constraint=[intel16|intel18|amd20]
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=4:00:00
#SBATCH --array=1-151
#SBATCH --output=slurm-%a.out
echo "SLURM_JOBID: " $SLURM_JOBID
echo "SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID
echo "SLURM_ARRAY_JOB_ID: " $SLURM_ARRAY_JOB_ID

module purge
module load Conda/3

python systematic.py $SLURM_ARRAY_TASK_ID
