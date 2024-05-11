import boto3

#gets volume id of the unattached volumes and notify

def getVolumeID():
    #create ec2 boto client
    ec2_client = boto3.client('ec2')

    #describe instances
    vol_response = ec2_client.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    unAttachedVol = []

    #extract vol data
    for vol in vol_response['Volumes']:
        unAttachedVol.append(vol['VolumeId'])

    for volume in unAttachedVol:
        print(volume)

getVolumeID()