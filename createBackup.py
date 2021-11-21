import shutil
from config import Config
from s3handler import S3handler
import zipfile
import os
from datetime import datetime
from multipartUpload import multi_part_upload_with_s3


def saveToS3():
    obj = S3handler()
    resp = obj.saveArchive(Config.BUCKET, Config.DESTINATION_FILENAME, Config.DESTINATION)


def archiveDir(dir_name):
    print("Zipping...")
    shutil.make_archive(Config.DESTINATION_FILENAME, Config.ARCHIVE_TYPE, dir_name)

def zipItUp(dir_name):
    with zipfile.ZipFile(Config.DESTINATION_FILENAME + "." + Config.ARCHIVE_TYPE, 'w', compression=zipfile.ZIP_STORED, allowZip64=True) as zipped:
        zipped.write(dir_name)

def zipdir(path):
    # ziph is zipfile handle
    zipf = zipfile.ZipFile(Config.DESTINATION_FILENAME + "." + Config.ARCHIVE_TYPE, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        if not any(string in root for string in Config.IGNORE_DIRS) and not any(string in files for string in Config.IGNORE_FILES):
            print(root)
            for file in files:
                zipf.write(os.path.join(root, file))
    zipf.close()


def backupFunc():
    t1 = datetime.now()
    zipdir(Config.SOURCE)
    # zipItUp(Config.SOURCE)
    # archiveDir(Config.SOURCE)
    t2 = datetime.now()
    print((t2-t1).total_seconds())
    # saveToS3()
    multi_part_upload_with_s3()
    t3 = datetime.now()
    print((t3-t2).total_seconds())
