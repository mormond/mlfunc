#!/bin/bash

PARAM1=$1
echo 'hello' $PARAM1

#Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

#az functionapp deployment source config-zip -g test1 -n funcappqzyw7bgokigew --src ../requirements.zip
