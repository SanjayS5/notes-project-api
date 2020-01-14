# notes-project-api
The backend for a cloud-based note taking app hosted on AWS

This is the entire API for the note taking app. The architecture involves Lambda functions 
that are connected to API Gateway, requiring the use of Cognito authorisation. 

The API contains the standard CRUD operations (the lambda functions contain these), each one linked to DynamoDB. 

The frontend will be in a second repository.
