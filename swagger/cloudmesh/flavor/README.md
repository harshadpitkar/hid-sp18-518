# Swagger Cloud and Big Data Rest Service

## Objective :

This REST API is intended to allow users to request which flavor of OpenStack is in use.
* See https://docs.openstack.org/horizon/latest/admin/manage-flavors.html

The REST service should conform to Swagger/OpenAPI 2.0 specification. 

Credit for framing the how on this to Shagufta Pathan.

## Implementation :
* The basics of the REST service is defined in the YAML document `localhost.yaml` file
* POST operation has been implemented to post the command, username and hostname
* The server-side code has been generated using Swagger Codegen
* Modules like `subprocess` and `flask` have been used for the actual implementation


## Execution Details :
* Make sure you have swagger-codegen-cli.jar installed in your working directory
* git clone the swagger directory
* On your terminal, using the Makefile provided run the following commands:
  * `make service`
  * `make start`
  * You should see a message like this:
  ``` 
  Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
  ```
* On another terminal to test the service, run:
    * `make test`
    
* To kill the service, run:
  * `make stop`
  
* To clean the directories, run:
  * `make clean`
  
* To create a docker image and build the image, simple run:
  * `make container`
  
