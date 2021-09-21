# Rails Overview

Database --- Model --- Controller --- Router --- View

# Router

When HTTP Requests are sent to a Rails Server, they first make contact with the 
ROUTER. Which sends the request to the appropriate CONTROLLER based on the METHOD
& PATH. The ROUTER also tells the CONTROLLER which ACTION to execute. 

## Request/Response

HTTP Request goes from CLIENT to SERVER
* method (GET, PUT, PATCH, POST, DELETE)
* path (/users/1/posts/)
* query (?loc=NY&name=daniel)
* body - additional data which can come from a form. cannot be part of a GET request

HTTP Response goes from SERVER to CLIENT
* status (200 OK, 300 Redirect, 400 Client error, 500 Server error)
* body - main response

## RESTful Routes

REST: Representational State Transfer

|   HTTP Verb  |       path       | action |                    utility                   |
|:------------:|:----------------:|:------:|:--------------------------------------------:|
|      GET     |      /photos     |  index |         display a list of all photos         |
|      GET     |    /photos/new   |   new  | return an HTML form for creating a new photo |
|     POST     |      /photos     | create |         upload and create a new photo        |
|      GET     |    /photos/:id   |  show  |           display a specific photo           |
|      GET     | /photos/:id/edit |  edit  |    return an HTML form for editing a photo   |
| PATCH or PUT |    /photos/:id   | update |            update a specific photo           |
|    DELETE    |    /photos/:id   | delete |            delete a specific photo           |