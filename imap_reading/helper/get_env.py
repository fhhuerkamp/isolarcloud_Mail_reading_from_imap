from dotenv import load_dotenv
import os

"""
    loads environment variables from .env
    or maybe from somewhere else in the future
"""

def get_env(environment_variable,source="dotenv"):
    if source == "dotenv":
        load_dotenv(override=False)
        return os.environ.get(environment_variable)
    return None
