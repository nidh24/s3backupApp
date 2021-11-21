"""
main script
"""
from config import Config
import time
from createBackup import backupFunc
import traceback


def handler():
    """
    Main function which handles the application
    """
    try:
        backupFunc()
    except Exception as exc:
        traceback.print_exc()


if __name__ == "__main__":
    handler()