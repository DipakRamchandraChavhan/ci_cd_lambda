import boto3

def lambda_handler(event, context):
    print('Hello World start')
        
    s3_client = boto3.client('s3')

    response = s3_client.list_buckets()
    
    buckets=response['Buckets']

    for bucket in buckets:
        print(bucket['Name'])
        
    print('Hello World end')

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
