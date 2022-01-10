import boto3

ec2_instances = [i['InstanceId'] for r in boto3.client('ec2').describe_instances()['Reservations'] for i in r['Instances']]

paginator = boto3.client('ssm').get_paginator('describe_instance_information')
page_iterator = paginator.paginate()
ssm_instances = []
for page in page_iterator:
    for instance in page['InstanceInformationList']:
        ssm_instances.append(instance['InstanceId'])

print('EC2 instances:')
print(len(ec2_instances))

print('SSM managed instances:')
print(len(ssm_instances))

print('Unmanaged EC2 instances:')
unmanaged_instances = set(ec2_instances) - set(ssm_instances)
print(len(unmanaged_instances))
print(unmanaged_instances)
