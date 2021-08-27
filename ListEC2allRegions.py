## list all existing EC2 instances from all AWS Regions
## This code was buit based on the youtube video presentation: https://www.youtube.com/watch?v=VXxScSbbRAs 
## The objective of reproducing this code is educational and is not intent to be used commercially
##

import boto3
import pprint

from pkg_resources import cleanup_resources

session=boto3.Session('ec2',region_name='sa-east-1')
ec2_cli=boto3.client(service_name='ec2')

all_regions=ec2_cli.describe_regions()

##  List all regions is a feature available just for client objects (see ec2_cli statement above)

list_of_regions=[]

for each_region in all_regions['Regions']:
    list_of_regions.append(each_region['RegionName'])
print(list_of_regions)

##  To list the EC2 instances from each regions, is necessary to open a session in each reagion.
##  In adition, we need to refer to Resources instead of client to let code simple and easir to code

for each_region in list_of_regions:
    session=boto3.Session('ec2',region_name=each_region)
    ec2=boto3.resource('ec2',each_region)
    print("List of EC2 instances from the region: ", each_region)
    for each_instance in ec2.instances.all():
        print(each_instance.id,each_instance.state['Name'])

## The output expected to be generate is similar to the following:
## For the purpose for this test, there was just one instance located in the São Paulo region.
##
##
##      List of EC2 instances from the region:  ap-northeast-3
##      List of EC2 instances from the region:  ap-northeast-2
##      List of EC2 instances from the region:  ap-northeast-1
##      List of EC2 instances from the region:  sa-east-1
##      i-069034efe5cj63646eb running
##      List of EC2 instances from the region:  ca-central-1
##      List of EC2 instances from the region:  ap-southeast-1
##      List of EC2 instances from the region:  ap-southeast-2
##      List of EC2 instances from the region:  eu-central-1
##      List of EC2 instances from the region:  us-east-1
##      List of EC2 instances from the region:  us-east-2
##      List of EC2 instances from the region:  us-west-1
##      List of EC2 instances from the region:  us-west-2
