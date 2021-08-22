## List all EC2 resources within the account in all regions and its related resources
##

import boto3
import pprint

session=boto3.session(profile_name="aws_ec2_iam_user",region_name="us-east-1")

##  List all regions is a feature available just for client objects (nor for resources)
##

client = session.client(service_name='ec2')
all_regions=client.describe_regions()

##  This will list ALL regions 
#
##  pprint.pprint(all_regions['Regions'])
#
## So we will get just the regions name in a list 
#
list_of_regions[]
for each_region in all_regions['Regions']:
    #print(each_region['RegionName'])
    list_of_regions.append(each_region['RegionName'])
    print(list_of_regions)  

## Once we got the regions list, we can use resource instead of client to reduce de amount of code
## We need a session for each region
#
## For each_region in list_of_Regions we will get the EC2 list
#     


for each_region in list_of_Regions:
    session=boto3.session(profile_name="aws_ec2_iam_user",region_name=each_region)
    resource=session.resource(service_name="ec2")
    all_EC2s=resource.describe_instances()
    list_of_EC2s[]
    for each_EC2 in all_EC2s['Name']:
        list_of_EC2s.append(each_EC2['InstanceName']
        print ("List of EC2s:", each_EC2)
    


