
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import boto3
from pprint import pprint


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/videos")
async def getVideos():
    return [getVideoInfo("dirtyTestVideo")]


@app.get("/videos/{object_key}")
async def getVideoInfo(object_key):
    """
    
    Expected output
    • S3 Object Url (Video Source)
    • Title
    """

    # Retrieve metadata from DynamoDB using object_key
    metadata = getMetadataFromDynamoDB(object_key)

    # Retrieve video link from S3 using object_key
    s3_video_link = getVideoLinkFromS3(object_key)

    return {
        "s3_video_source": s3_video_link,
        "title": metadata["title"]
    }


def getMetadataFromDynamoDB(object_key):
    try:
        client = boto3.client('dynamodb')
        response = client.get_item(
            TableName='nflx-metadata',
            Key={
                's3_object_key': {
                    'S': object_key
                }
            },
            AttributesToGet=[
                'title',
                'description',
                'tags'
            ],
        )

        metadata = {}

        for item in response['Item']:
            metadata[item] = list(response['Item'][item].values())[0]

        return metadata
    except Exception as e:
        print("Unable to get item")
        print(e)
        return False



def getVideoLinkFromS3(object_key):
    return f"https://www.sgunchained.com/{object_key}"




# @app.post("/fileUpload/{file}")
# async def upload(file):
#     print(file)
#     print("Uploading...")
#     cv2.imwrite(f"images/{file.name}", file)


@app.post("/infer/{file}")
async def infer(file):
    print(file)
    prediction = await run(file)
    return {"prediction": prediction}
