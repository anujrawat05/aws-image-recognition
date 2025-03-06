# Infrastructure Setup

This folder contains instructions for setting up the AWS resources required for the AWS Image Recognition System.

## Steps to Set Up AWS Resources

### 1. Create an S3 Bucket
1. Go to the **S3 Console**.
2. Click **Create Bucket**.
3. Enter a unique bucket name (e.g., `my-image-recognition-bucket`).
4. Enable **Public Access** (if required).
5. Click **Create Bucket**.

### 2. Create an IAM Role for Lambda
1. Go to the **IAM Console**.
2. Click **Roles > Create Role**.
3. Select **AWS Lambda** as the use case.
4. Attach the following policies:
   - `AmazonRekognitionFullAccess`
   - `AmazonS3ReadOnlyAccess`
5. Name the role (e.g., `lambda-rekognition-role`).
6. Click **Create Role**.

### 3. Create a Lambda Function
1. Go to the **Lambda Console**.
2. Click **Create Function**.
3. Choose **Author from scratch**.
4. Enter a function name (e.g., `image-recognition-lambda`).
5. Select **Python 3.x** as the runtime.
6. Under **Permissions**, select the IAM role you created earlier.
7. Click **Create Function**.
8. Copy the code from `lambda/lambda_function.py` into the Lambda function editor.
9. Deploy the function.

### 4. Configure S3 Event Trigger
1. Go to the **S3 Console**.
2. Select the bucket you created earlier.
3. Go to the **Properties** tab.
4. Scroll down to **Event Notifications** and click **Create Event Notification**.
5. Enter a name for the event.
6. Select **All object create events**.
7. Under **Send to**, choose **Lambda Function**.
8. Select the Lambda function you created earlier.
9. Click **Save Changes**.

### 5. Test the Setup
1. Upload an image to the S3 bucket.
2. Check the **CloudWatch Logs** for the Lambda function to see the results.