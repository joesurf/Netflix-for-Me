import boto3


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




# import boto3
# from uuid import uuid4
# def lambda_handler(event, context):
#     s3 = boto3.client("s3")
#     dynamodb = boto3.resource('dynamodb')
#     for record in event['Records']:
#         bucket_name = record['s3']['bucket']['name']
#         object_key = record['s3']['object']['key']
#         size = record['s3']['object'].get('size', -1)
#         event_name = record ['eventName']
#         event_time = record['eventTime']
#         dynamoTable = dynamodb.Table('s3Metadataserverless')
#         dynamoTable.put_item(
#             Item={
#                 'Resource_id': str(uuid4()), 
#                 'Bucket': bucket_name, 
#                 'Object': object_key,
#                 'Size': size, 
#                 'Event': event_name, 
#                 'EventTime': event_time
#             }
#         )

