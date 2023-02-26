''' Create a boto3 script to create EC2 instance '''
import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2')

# Define the parameters for the instance
image_id = 'your-ami-id'  # Amazon Linux 2 AMI ID
instance_type = 't2.micro'  # Instance type
key_name = 'my-keypair'  # Key pair name
security_group_ids = ['your-security-group']  # Security group ID(s)
subnet_id = 'your-subnet'  # Subnet ID

# Launch the instance
try:
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=1
    )
    # Print the instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f'Launched EC2 instance {instance_id}')
except Exception as e:
    print(f'Error launching EC2 instance: {e}')
