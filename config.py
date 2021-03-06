"""
Config class
"""
from datetime import time


class Config:

    createTime = time(10, 0)
    terminateTime = time(22, 0)
    describeTime = time(16, 0)

    EXECUTE = {}
    BUCKET = "backup-bucket-nidhish"
    DESTINATION = "backup/"
    SOURCE = r"C:\\Users\\USER\\Nidhish\\"
    DESTINATION_FILENAME = "backup"
    ARCHIVE_TYPE = "zip"
    IGNORE_DIRS = [".git", "layers", "env", "node_modules", "apple", "__pycache__"]
    IGNORE_FILES = ["backup.zip",]
  
