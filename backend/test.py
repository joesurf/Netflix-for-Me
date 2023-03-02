from main import getMetadataFromDynamoDB, getVideoLinkFromS3

# print(getMetadataFromDynamoDB('dirtyTestVideo'))



import boto3

def getVideoLink(object_key):
    bucket_name = "mflx-upload-stroage"
    key = object_key


    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file("upload.txt", key)
    location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)


# print(getVideoLink('dirtyTestVideo'))
