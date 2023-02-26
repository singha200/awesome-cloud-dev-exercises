'''Modify the ec2 creation script to create and attach a new security group '''
import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2')

# Define the parameters for the instance
image_id = 'your-ami'  # Amazon Linux 2 AMI ID
instance_type = 't2.micro'  # Instance type
key_name = 'my-keypair'  # Key pair name
subnet_id = 'your-subnet'  # Subnet ID

# Define the parameters for the security group
security_group_name = 'my-security-group'  # Security group name
security_group_description = 'My security group'  # Security group description
ip_permissions = [
    {
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    }
]

# Create the security group
try:
    response = ec2.create_security_group(
        GroupName=security_group_name,
        Description=security_group_description,
        VpcId=subnet_id
    )
    security_group_id = response['GroupId']
    print(f'Created security group {security_group_name} with ID {security_group_id}')
    # Authorize inbound traffic to the security group
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=ip_permissions
    )
    print('Inbound traffic authorized to the security group')
    # Launch the instance with the security group attached
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=1
    )
    # Print the instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f'Launched EC2 instance {instance_id} with security group {security_group_name}')
except Exception as e:
    print(f'Error launching EC2 instance: {e}')
