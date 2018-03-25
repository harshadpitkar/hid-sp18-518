# Boto3 for managing S3

## Overview
Python libraries exist now that help you abstract your project from your cloud 
provider. This may be important if you think you may need to use multiple cloud 
providers or if you want to ensure you take steps to avoid provider lock-in. 
There are multiple providers in this space and two of them are Apache Libcloud 
and Boto. To put it simply, these libraries allow you to code simple resource 
management that is independent of cloud provider specific API calls. 

To begin using the boto3 library in your python environment, you need to install the boto3 package using the Python package management system, pip.

`pip install boto3`

Now that you have installed boto3, let’s take a look at what it makes available in the console editor.

First, open python and import boto3 like below.

`python3`

`>>> import boto3`

A useful feature to use in Python is the help() function.

`>>> help(boto3)`

`>>> help(boto3.s3)`


Now that you have familiarized yourself with boto3, let's begin to use it. For this tutorial, we will be leveraging boto3 to configure and manage S3 in AWS. To do so, you first will need credentials for an active AWS account. As credential management can be its own topic, I recommend looking at the configuration guide here http://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration

Now that you have credentials set up for AWS, we need to tell boto3 which provider you will be leveraging. 

The boto3.client or more specifically for S3, the boto3.resource can be defined with your flavor of cloud provider. Since s3 is the goal, the following will define s3 and declare a local variable to store the boto3 s3 client.

`>>> s3 = boto3.client('s3')`

Next, if you have s3 buckets already in place, you can use the following to list them. This will test your credentials and setup and ensure you can take on more advanced tasks with boto3.

Using list_buckets() function will allow us to store a JSON response for buckets that the credentials have access to. To print out the result, you can point to the Buckets array.

`>>> response = s3.list_buckets()`

`>>> print response['Buckets']
[{u'CreationDate': datetime.datetime(2018, 3, 25, 18, 22, 8, tzinfo=tzutc()), u'Name': 'bucket-for-iu-cloud-computing'}]`

To create a bucket, you can leverage create_bucket. Be mindful of DNS requirements for buckets and ensure the name is not already in use. The errors reported by boto3 are useful but sometimes quite verbose.

For example
`>>> s3.create_bucket(Bucket='another-bucket-for-iu-cloud-computing')`

There are a large family of functions that can be found here:
http://boto3.readthedocs.io/en/latest/reference/services/s3.html

The functions are grouped between creation, deletion and aspects like permissions or policies for the bucket.

To learn more about Boto and it's other features, please visit http://boto3.readthedocs.io/en/latest/
