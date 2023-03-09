import os
from typing import get_type_hints, Union
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DEBUG = os.environ.get("DEBUG")