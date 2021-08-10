# Import the SDK
import boto3
import uuid

# Instantiate a new client object (with no params or config boto3 defaults to env >> credentials >> IAM role)
s3client = boto3.client('s3')

# Create S3 bucket with a unique name (in the global namespace) 
bucket_name = 'python-sdk-sample-{}'.format(uuid.uuid4())
print('Creating new bucket with name: {}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)

# Now the bucket is created, and we will be able to find it in our list of buckets.
list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    if bucket['Name'] == bucket_name:
        print('(Just created) --> {} - there since {}'.format(
            bucket['Name'], bucket['CreationDate']))

# The files (objects) stored in the bucket can be referred to by its key (AKA the name)
object_key = 'python_sample_key.txt'

# The object holds some data
# Create (PUT) a new object with the key "py_sample_key.txt" and content "Hello World!"
print('Uploading some data to {} with key: {}'.format(
    bucket_name, object_key))
s3client.put_object(Bucket=bucket_name, Key=object_key, Body=b'Hello World!')

# Using client API, generate pre-signed URL (secure link, not public)
# By default, URL expires after 1 hour
# 604800 seconds === 1 week
url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': object_key})
print('\nTry this URL in your browser to download the object:')
print(url)

# Error checking
try:
    input = raw_input
except NameError:
    pass
input("\nPress enter to continue...")

# NOTE:
# As seen in create_bucket, list_buckets, put_object methods...
# Client API requires an explicit specify for all params in each operation
# Most methods in the client class map to 1 underlying API call to the AWS service (S3)

# Resource API is also an option
# That has resource objects, which abstract out the over-the-network API calls
# Below, we instantiate and use 'bucket' or 'object' objects

# Console print
print('\nNow using Resource API')

# Create the service resource object
s3resource = boto3.resource('s3')

# Create bucket object
bucket = s3resource.Bucket(bucket_name)

# Create object object
obj = bucket.Object(object_key)
print('Bucket name: {}'.format(bucket.name))
print('Object key: {}'.format(obj.key))
print('Object content length: {}'.format(obj.content_length))
print('Object body: {}'.format(obj.get()['Body'].read()))
print('Object last modified: {}'.format(obj.last_modified))

# NOTE: 
# Buckets can't be deleted unless they are empty!
# Below, we delete everything, utilizing the collection 'objects' and the batch action 'delete'
# Batch actions returns a list of responses (bc boto3 may have to take multiple iterations to complete the action)
print('\nDeleting all objects in bucket {}.'.format(bucket_name))
delete_responses = bucket.objects.delete()
for delete_response in delete_responses:
    for deleted in delete_response['Deleted']:
        print('\t Deleted: {}'.format(deleted['Key']))

# Bucket empty? => delete the bucket
print('\nDeleting the bucket.')
bucket.delete()
