import os
from typing import get_type_hints, Union
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = os.environ.get("DEBUG")