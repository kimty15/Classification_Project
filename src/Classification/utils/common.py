import os
# from box.exceptions import BoxValueError
import yaml
from Classification import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
from Classification.exception import CustomExpection
import sys


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logging.error("Can load the file yaml")
        raise CustomExpection(e,sys)
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"created directory at: {path}")
    except Exception as e:
        logging.error("Error occured in creating directories")
        raise CustomExpection(e,sys)



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"json file saved at: {path}")
    except Exception as e:
        logging.error("Error occured in saving json file")
        raise CustomExpection(e,sys)




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    try:
        with open(path) as f:
            content = json.load(f)

        logging.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logging.error("Error occured in loading json file")
        raise CustomExpection(e,sys)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    try:
        joblib.dump(value=data, filename=path)
        logging.info(f"binary file saved at: {path}")
    except Exception as e:
        logging.error("Error occured in saving binary file")
        raise CustomExpection(e,sys)


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(path)
        logging.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        logging.error("Error occured in loading binary file")
        raise CustomExpection(e,sys)

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logging.error("Error occured in getting size of file")
        raise CustomExpection(e,sys)


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
