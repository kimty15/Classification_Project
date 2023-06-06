from src.Classification import logging
from src.Classification.exception import CustomExpection
import sys
from src.Classification.utils.common import read_yaml
from src.Classification.exception import CustomExpection
from pathlib import Path
path_file = 'config\config.yaml'




# def test_read_yaml_exception():
#     try:
#         config = read_yaml(path_file)
#         logging.info("Read successfully")
#     except Exception as e:
#         logging.error("Error occured in read file yaml")
#         raise CustomExpection(e,sys)
    
# main 
if __name__ == "__main__":
    config_data = read_yaml(Path(path_file))
    print(config_data.artifacts_root)
