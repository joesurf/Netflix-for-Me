import logging
import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
import os
import sys
import json
import threading


from stepfunctions.uploadVideoToS3 import upload_file


def main():
    boto3.setup_default_session(profile_name='nflx', region_name='us-east-1')


    bucket = 'nflx-upload-storage' # 'netflix-for-me-nflx'
    filename = "/Users/joesurf/Downloads/TianLongBaBu/The Demi-Gods and Semi-Devils E2.mp4"
    # object_name = os.path.basename(filename)

    # Create object key
    object_key = str(os.path.basename(filename))

    metadata = {
        'object_key': object_key,
        'title': 'The Demi-Gods and Semi-Devils - Episode 2',
        'description': 'Set in 11th-century China and adapted from wuxia novel',
        'tags': ['Chinese'],
        'series': 'The Demi-Gods and Semi-Devils'
    }

    if insertMetadataInDynamoDB(metadata):
        print("Sucessfully inserted metadata")

        if upload_file(
            file_name=filename, 
            bucket=bucket, 
            object_name=object_key
        ):

            print("Successfully uploaded file")

            # Update DynamoDB of 



def insertMetadataInDynamoDB(movie_object):
    try:
        client = boto3.client('dynamodb')
        response = client.put_item(
            TableName='nflx-metadata',
            Item={
                's3_object_key': {'S': movie_object["object_key"]},
                'title': {'S': movie_object["title"]},
                'description': {'S' : movie_object["description"]},  
                'tags': {'SS': movie_object["tags"]},                 
            }
        )
        return True
    except Exception as e:
        print("Unable to insert item")
        print(e)
        return False

    


def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    config = TransferConfig(multipart_threshold=1024 * 25, 
                            max_concurrency=10,
                            multipart_chunksize=1024 * 25,
                            use_threads=True)


    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(
            file_name, bucket, object_name,
            ExtraArgs={"ContentType": 'video/mp4'},
            Config=config,
            Callback=ProgressPercentage(file_name)
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()



if __name__ == "__main__":
    main()
