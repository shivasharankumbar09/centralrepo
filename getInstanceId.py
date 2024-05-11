import boto3


#gets EC2 instance id of instance in running state

def describeEC2Instances():
    #create a boto3 ec2 client
    ec2_client = boto3.client('ec2')

    #describe instances
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instances = []
    

    #extract instances data
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
           active_instances.append(instance['InstanceId'])
    
    for instance in active_instances:
        print(instance)
   

if __name__ == "__main__":
    instances = describeEC2Instances()
    


