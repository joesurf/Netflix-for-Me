import os

from stepfunctions.uploadVideoToS3 import upload_file
from stepfunctions.insertMetadataInDynamoDB import insertMetadataInDynamoDB


def main():

    bucket = 'nflx-upload-storage' # 'netflix-for-me-nflx'
    filename = "/Users/joesurf/Downloads/gamingTestVideo.mp4"
    # object_name = os.path.basename(filename)

    # Create object key
    object_key = str(os.path.basename(filename))

    metadata = {
        'object_key': object_key,
        'title': "The Avengers Begins",
        'description': 'A fight to the death',
        "tags": ["modern"]
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


    

if __name__ == "__main__":
    main()
