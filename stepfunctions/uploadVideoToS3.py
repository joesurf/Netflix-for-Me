import logging
import boto3
from botocore.exceptions import ClientError
import os
import json


def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """



    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(
            file_name, bucket, object_name,
            ExtraArgs={'Metadata': {"ContentType": 'video/mp4'}}
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


