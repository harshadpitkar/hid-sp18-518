# Libcloud for managing EC2

## Overview
Python libraries exist now that help you abstract your project from your cloud 
provider. This may be important if you think you may need to use multiple cloud 
providers or if you want to ensure you take steps to avoid provider lock-in. 
There are multiple providers in this space and two of them are Apache Libcloud 
and Boto. To put it simply, these libraries allow you to code simple resource 
management that is independent of cloud provider specific API calls. 

To begin using the libcloud library in your python environment, you need to install the apache-libcloud package using the Python package management system, pip.

`pip install apache-libcloud`

Now that you have installed libcloud, let’s take a look at what it makes available in the console editor.

First, open python and import libcloud like below.

`python3`

`import libcloud`

A useful feature to use in Python is the help() function.

`help(libcloud)`

`help(libcloud.compute)`

Now that you have familiarized yourself with libcloud, let's begin to use it. For this tutorial, we will be leveraging libcloud to configure and manage EC2 in AWS. To do so, you first will need credentials for an active AWS account. As credential management can be its own topic, I recommend looking at the configuration guide here https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html

Now that you have credentials set up for AWS, we need to tell libcloud which provider you will be leveraging. 

The libcloud.compute can be defined with your flavor of cloud provider. Since EC2 is the goal, the following will define EC2 and declare a local variable to store the libcloud EC2 client.


`from libcloud.compute.types import Provider`

`from libcloud.compute.providers import get_driver`

`client = get_driver(Provider.EC2)`

Next, we will need to define some local variables to store the credentials to be used. 

`ACCESS_ID = '<ENTER ACCESS ID HERE>'`

`SECRET_KEY = '<ENTER YOUR SECRET KEY HERE>'`

Once that is set up, you can define your EC2 driver with the region you prefer.

`ec2_driver = client(ACCESS_ID, SECRET_KEY, region="us-east-1")`

To test the connection, you can request the available EC2 sizes and print them out using:

`print (driver.list_sizes())`

To view your existing nodes, you can leverage

`nodes = driver.list_nodes()`

`print(nodes)`
`[<Node: uuid=ec666f44f5fe597924877a590a3dbdc7a1222e7d, state=RUNNING>]`

To create a node, you will need to define some criteria on what type you would like.

`desired_size = 't1.micro'`

`desired_image = 'ami-26ebbc5c'`

The next two commands will store a local copy of available sizes and images, respectively.
`sizes = driver.list_sizes()`

`images = driver.list_images()`

Now, to store the id in the required format to call create_node.

`size = [s for s in sizes if s.id == desired_size][0]`

`image = [i for i in images if i.id == desired_image][0]`

Now to call create_node with our local variables to build a T1.micro Redhat instance.

`node = driver.create_node(name="IU Cloud Computing", image=image, size=size)`

Last, notice when node is printed, the status is listed as PENDING. This is because there are additional tasks you must take with SSH keys. You can use your browser to review EC2 and finalize and there are additional guides that can show you how to automate that aspect as well.

`print(node)`
`<name=IU Cloud Computing, state=PENDING>`

There are a lot of possibilities with libcloud and for EC2, more examples can be found here.  

https://libcloud.readthedocs.io/en/latest/compute/drivers/ec2.html

To learn more about Libcloud in general and its other features, please visit http://libcloud.readthedocs.io/en/latest/
