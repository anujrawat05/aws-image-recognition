import boto3

def lambda_handler(event, context):
    # Initialize Rekognition client
    rekognition = boto3.client('rekognition')
    
    # Specify the S3 bucket and image file
    bucket = 'image-bucky'
    image = 'test-image.jpg'
    
    # Call Rekognition to detect labels
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image
            }
        },
        MaxLabels=10,  # Maximum number of labels to return
        MinConfidence=70  # Minimum confidence level for labels
    )
    
    # Process and return the response
    labels = [label['Name'] for label in response['Labels']]
    return {
        'statusCode': 200,
        'body': labels
    }