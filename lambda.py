##############################
####  serializeImageData  ####
##############################

import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event["s3_key"]
    bucket = event["s3_bucket"]
    
    # Download the data from s3 to /tmp/image.png
    boto3.resource('s3').Bucket(bucket).download_file(key, '/tmp/image.png')
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }


##############################
####    imageClassifier   ####
##############################

import json
import sagemaker
import base64
import boto3
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-10-26-20-58-18-113'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"])

    # Instantiate a Predictor
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, 
                                        ContentType='image/png', 
                                        Body=image)
    predictor = json.loads(response['Body'].read().decode('utf-8'))

    # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    # inferences = 
    
    # We return the data back to the Step Function    
    event["inferences"] = predictor
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


##############################
####  inferenceThreshold  ####
##############################

import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    # Parse the JSON in the "body" key of the event
    event_body = json.loads(event["body"])
    
    # Access the "inferences" array from the parsed JSON
    inferences = event_body.get("inferences", [])
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(inferences, default=0) > THRESHOLD
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
