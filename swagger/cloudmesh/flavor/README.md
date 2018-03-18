# Swagger Cloud and Big Data Rest Service

## Objective :

This REST API is intended to allow users to request which flavor of OpenStack is in use.
* See https://docs.openstack.org/horizon/latest/admin/manage-flavors.html

The REST service should conform to Swagger/OpenAPI 2.0 specification. 

Credit for framing the how on this to Shagufta Pathan.

## Implementation :
* The basics of the REST service is defined in the YAML document `flavor.yaml` file
* The server-side code has been generated using Swagger Codegen
