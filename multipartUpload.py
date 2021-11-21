import threading
import boto3
import os
import sys
from boto3.s3.transfer import TransferConfig
from config import Config

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_id")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_key")
s3 = boto3.resource('s3',region_name="us-east-1",
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


def multi_part_upload_with_s3():

    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    file_path = os.path.dirname(__file__) + "\\" + Config.DESTINATION_FILENAME + "." + Config.ARCHIVE_TYPE
    key_path = Config.DESTINATION + Config.DESTINATION_FILENAME + "." + Config.ARCHIVE_TYPE
    s3.meta.client.upload_file(file_path, Config.BUCKET, key_path,
                            Config=config,
                            Callback=ProgressPercentage(file_path))
    print("\n")


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()
