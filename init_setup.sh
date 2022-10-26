echo [$(date)]: "Start"
echo [$(date)]: "Creating Conda Environment with python 3.8"
conda create -p ./env python=3.8 -y
echo [$(date)]: "Activating the Created Conda Environment"
source activate ./env
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "End"


