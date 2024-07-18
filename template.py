import os 
import sys 
from pathlib import Path 
import logging
logging.basicConfig(filename="file.log",level=logging.INFO)

project_name="GBM"
list_of_files = [
     ".github/workflows/main.yaml",
     f"{project_name}/components/__init__.py",
     f"{project_name}/components/data_ingestion.py",
     f"{project_name}/components/data_transformation.py",
     f"{project_name}/components/model_training.py",
     f"{project_name}/components/model_pusher.py",
     f"{project_name}/components/model_evaluator.py",
     f"{project_name}/constant/__init__.py",
     f"{project_name}/entity/__init__.py",
     f"{project_name}/entity/artifact_entity.py",
     f"{project_name}/entity/config_entity.py",
     f"{project_name}/pipeline/__init__.py",
     f"{project_name}/pipeline/training_pipeline.py",
     f"{project_name}/exception.py",
     f"{project_name}/logger.py",
     "experiment/eda_research.ipynb",
     ".gitignore",
     "bentofile.yaml",
     "README.md",
     "LICENSE",
     "requirements.txt",
     "setup.py",
     "main.py"
]



for filepath in list_of_files:
     filepath=Path(filepath)
     filedir,filename=os.path.split(filepath)
     if filedir!="":
          os.makedirs(filedir,exist_ok=True)
          logging.info(f"Creating directory :{filedir} for the file {filename}")
     if (not os.path.exists(filepath))or (os.path.getsize(filepath)==0):
          with open(filepath,'w') as f:
                pass
                logging.info(f"Creating empty file:{filepath}")
     else:
          logging.info(f"{filename} is already exits")   