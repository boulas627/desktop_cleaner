# Desktop Cleaner Python Script 
This script is meant to run on your machine and organize the folders in your local file system. The user is responsible for selecting a specific folder that they would like organized and the script will do the rest of the work. Depending on the filename extension, each file in a specific folder will be sorted into one of the new folder's that would be created: 
- PowerPoints
- Excel
- Videos
- Audio
- Compressed

# ECS Terminology

Task Definition - Blueprint that describes how a docker container should launch. Settings include port, docker image, cpu shares, memory requirement, command to run, and environmental variables. 

Task - The running container with settings defined in task definition. This is an instance of the task definition. 

Service - This is used to define the long running tasks of the same task definition. This can include one running container or multiple running containers that all use the same task definition. 

Cluster - This is a logic group of EC2 instances. 

Container Instance - An EC2 instance that is part of the ECS cluster. This instance should have both docker and ecs-agent running on it. 

Please visit the following link for more information on how ECS works: 
https://medium.com/boltops/gentle-introduction-to-how-aws-ecs-works-with-example-tutorial-cea3d27ce63d 
