#!/bin/sh

#Edit this script to install FEET-required programs by changing the relative paths (~) to specific paths 
#requires conda environments and also python. Python-2.7.15 works, and probably most others. (can add it to virtual environment below if not already available)
#I recommend always using `tmux` or using `screen`
#Set up the subfolders and files as shown in this folder. (the FEET/ folder)

cd ~/FEET/
git clone https://github.com/Arkadiy-Garber/FeGenie.git
cd FeGenie

source ~/miniconda3/etc/profile.d/conda.sh
conda config --add channels defaults 2> /dev/null
conda config --add channels bioconda 2> /dev/null
conda config --add channels conda-forge 2> /dev/null
conda config --add channels au-eoed 2> /dev/null
conda config --add channels r
# Build virtual environment
conda create -n fegenie hmmer diamond prodigal blast --yes
conda activate fegenie

## creating directory for conda-env-specific source files
mkdir -p $CONDA_PREFIX/etc/conda/activate.d

## adding FeGenie bin path and HMM_dir variable:
echo '#!/bin/sh'" 
export PATH=\"$(pwd):"'$PATH'\"" 
export rscripts=\"$(pwd)/rscripts\"
export iron_hmms=\"$(pwd)/hmms/iron\"" >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo "export R_LIBS=~/miniconda3/envs/fegenie/lib/R/library" >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

conda deactivate


# re-activating environment so variable and PATH changes take effect
conda activate fegenie


# Install R
conda install r-base
conda install -c r r-ggplot2
conda install -c r r-reshape
conda install -c r r-reshape2
conda install -c r r-tidyverse
conda install -c r r-argparse
conda install -c r r-ggdendro
conda install -c r r-ggpubr
conda install -c r r-grid


conda update fegenie


#All this is just to get fegenie and R to both work in a conda environment. If it doesn't work, mosts of R is not needed anyways, the basic output files of FeGenie are sufficient for FEET. 