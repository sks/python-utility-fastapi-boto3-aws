import boto3

def get_bucket_info():
    s3_client = boto3.client('s3') # Create an S3 client
    buckets = s3_client.list_buckets() # Retrieve the list of existing buckets

    new_buckets=[]
    for bucket in buckets['Buckets']: 
        bucket_name = bucket["Name"], # Output the bucket names
        new_buckets.append(bucket_name)
    return{
    "new_buckets" : new_buckets
    }        

def get_instances_info():
    ec2_client = boto3.client('ec2') # Create an EC2 client
    instances = ec2_client.describe_instances() # Retrieve the list of existing Instances
    new_instances=[]
    instance_name= None
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
                for tag in instance['Tags']:    
                        instance_name = tag['Value'] # Output the Instances names              
                new_instances.append(instance_name)
    return{
    "new_instances" : new_instances
    }     
      