# describe ec2 instances

import boto3

def describeEC2Instances():
    #create a boto3 ec2 client
    ec2_client = boto3.client('ec2')

    #describe instances
    response = ec2_client.describe_instances()

    #extract instances data
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name']
            }
            instances.append(instance_info)
    return instances

if __name__ == "__main__":
    instances = describeEC2Instances()
    for instance in instances:
        print(instance)

        