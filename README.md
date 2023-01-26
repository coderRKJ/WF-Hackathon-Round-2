# WF-Hackathon-Round-2
Find cascading application failure in a series of microservices.

## Introduction
Slides: [Microservice Monitoring.pptx](https://1drv.ms/p/s!AlmXLecu1YNMgtYKWP9xq4zN55UuGg)

The repo contains code for multiple FastAPI mock servers and a monitoring server with a dashboard (styled in Bootstrap).

This is only a demo project intended to showcase the idea for a universal monitoring service that can be used without modifying any code of the underlying microservice. 

Two convince scripts are given, one for setting up the environment and other for running all servers simultaneously.

## Instructions to Run
- Requires Python 3.11 installed in a Linux system
1. Clone this repo and `cd` into the cloned folder
1. Run `bash local_setup.sh` to setup venv and python libraries
1. Run `bash local_run.sh` to start all FastAPI backends on uvicorn servers.
1. Open `localhost:8000` to access the dashboard.
1. Pressing start triggers the front-end to send requests to all the starting mock microservice backends.
1. *Ctrl*+*C* to Stop both servers
