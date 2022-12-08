#!/bin/bash

# conda

HOME_PATH=/domus/h1/$USER

cd ${HOME_PATH}
rm ${HOME_PATH}/Miniconda3-latest-Linux-x86_64.sh
rm -rf ${HOME_PATH}/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash ${HOME_PATH}/Miniconda3-latest-Linux-x86_64.sh -b -p ${HOME_PATH}/miniconda3
${HOME_PATH}/miniconda3/bin/conda init bash # must, create ${HOME_PATH}/.bashrc

source ${HOME_PATH}/.bashrc
export CONDA_ENV_NAME=py38_apex
conda create -y -n $CONDA_ENV_NAME python=3.8 pip=20.2
eval "$(conda shell.bash hook)" # must for activate env
conda activate $CONDA_ENV_NAME

# babel
conda install -y pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=10.2 -c pytorch
python3.8 -m pip install --no-cache-dir --upgrade pip
python3.8 -m pip install transformers
python3.8 -m pip install sentencepiece
python3.8 -m pip install protobuf
python3.8 -m pip install sacremoses
python3.8 -m pip install nltk
python3.8 -m pip install --no-cache-dir wandb

# apex
rm -rf ${HOME_PATH}/apex
git clone https://github.com/NVIDIA/apex
cd ${HOME_PATH}/apex
python3.8 ${HOME_PATH}/apex/setup.py install