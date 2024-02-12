#!/bin/bash

#SBATCH --job-name=array
#SBATCH --array=1
#SBATCH --time=10:00:00
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=80
#SBATCH --output=array_${SLURM_ARRAY_TASK_ID}.out
#SBATCH --error=array_${SLURM_ARRAY_TASK_ID}.err
#SBATCH --exclusive 


module load python
source /home/fs02/pmr82_0001/rg727/CALFEWS-main/.venv_conda_calfews/bin/activate 
python jupyter_notebook_commands.py 