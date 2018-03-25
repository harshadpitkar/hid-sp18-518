#Boto for managing S3

##Overview
Python libraries exist now that help you abstract your project from your cloud 
provider. This may be important if you think you may need to use multiple cloud 
providers or if you want to ensure you take steps to avoid provider lock-in. 
There are multiple providers in this space and two of them are Apache Libcloud 
and Boto. To put it simply, these libraries allow you to code simple resource 
management that is independent of cloud provider specific API calls. 

To begin using the boto library in your python environment, you need to install the boto package using the Python package management system, pip.

`sudo pip install boto`

Now that you have installed boto, let’s take a look at what it makes available in the console editor.

First, open python and import boto like below.

`python`

`>>> import boto`

A useful feature to use in Python is the help() function.

`>>> help(boto)`

`>>> help(boto.s3)`

To learn more about Boto and it's other features, please visit http://boto3.readthedocs.io/en/latest/