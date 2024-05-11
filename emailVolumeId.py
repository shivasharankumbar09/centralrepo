import boto3
import os
from botocore.exceptions import ClientError

def send_email(subject, body):
    # Create an SES client
    ses_client = boto3.client('ses')

    # Specify sender and recipient email addresses
    sender = "shivasharan.kumbar@aquera.com"  # Replace with your sender email address
    recipient = "shivasharankumbar09@gmail.com"  # Replace with your recipient email address

    # Create the message
    message = {
        'Subject': {'Data': subject},
        'Body': {'Text': {'Data': body}}
    }

    # Try to send the email
    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={'ToAddresses': [recipient]},
            Message=message
        )
    except ClientError as e:
        print("Error sending email:", e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:", response['MessageId'])

def get_volume_id():
    # Create EC2 Boto3 client
    ec2_client = boto3.client('ec2')

    # Describe volumes
    vol_response = ec2_client.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    unattached_volumes = []

    # Extract volume data
    for vol in vol_response['Volumes']:
        unattached_volumes.append(vol['VolumeId'])

    return unattached_volumes

if __name__ == "__main__":
    # Call the function to get volume IDs
    volumes = get_volume_id()
    
    # Send email notification
    subject = "Unattached Volume IDs"
    body = "\n".join(volumes)
    send_email(subject, body)
