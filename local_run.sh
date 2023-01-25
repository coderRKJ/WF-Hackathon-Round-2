#! /bin/bash
set -e
echo "======================================================================"
echo "Welcome to the application. It will run the application in development mode."
echo "----------------------------------------------------------------------"
if [ -d "venv" ];
then
    echo "Enabling python 3.11 virtual env"
    # Activate virtual env
    . venv/bin/activate
else
    echo "No Virtual env detected. Please run setup.sh first"
    exit 1
fi

# Stop All Servers on EXIT
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

# Start Microservice Servers on uvicorn in debug mode
uvicorn microserviceA:app --reload --port 3001 &
uvicorn microserviceB:app --reload --port 3002 &
uvicorn microserviceC:app --reload --port 3003 &
uvicorn monitor:app --reload

# Deactivate virtual env 
deactivate
