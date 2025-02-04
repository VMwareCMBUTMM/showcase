import requests
import json

def handler(context, inputs):
    
    # Set Variables
    userName = inputs["__metadata"]["userName"]
    deployName = inputs["deploymentName"]
    deployId = inputs["deploymentId"]
    projectName = inputs["projectName"]
    deployStatus = inputs["status"]
    autoURL = inputs["autoURL"]
    
    # Google Chat webhook URL
    webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAKjED_eA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=sOQz6ZKVeqH2VZCCeqWfVOQfWCEp1Gooo-0hpeL3Ds0'
    
    # Your message to post
    
    message = (f"Hello from VCF Automation!\n Deployment Completed !\n Details:\n - Requested by: {userName}\n - Deployment Name: {deployName}\n - Project : {projectName}\n - Status: {deployStatus}\n - Deployment link: <{autoURL}/automation/#/service/catalog/consume/deployment/{deployId}|{deployName}>\n ")

    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    payload = {'text': message}

    response = requests.post(webhook_url, headers=headers, json=payload)
