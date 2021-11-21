"""
Module to handle Json functions related to EBS
"""
from boto3 import client, resource, Session
from config import Config
import os


class S3handler:
    
    def __init__(self):
        AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_id")
        AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_key")
        self.client = client('s3', region_name="us-east-1",
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        
        self.session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


    def saveArchive(self, bucket, filename, location):
        s3 = self.session.resource('s3')
        destination = "{}{}.{}".format(location, filename, Config.ARCHIVE_TYPE)
        print(destination)
        obj = s3.Object(bucket,destination)
        result = obj.put(Body=open('{}.{}'.format(filename,Config.ARCHIVE_TYPE), 'rb'))
        res = result.get('ResponseMetadata')
        if res.get('HTTPStatusCode') == 200:
            print('File Uploaded Successfully')
        else:
            print('File Not Uploaded')
            
