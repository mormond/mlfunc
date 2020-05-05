#!/bin/bash

USER=$1 
PASS=$2 
TENANT=$3
RG=$4
FUNCAPPNAME=$5

echo $USER $TENANT $RG $FUNCAPPNAME

#Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

#Grab python app package
curl  https://meobucket.blob.core.windows.net/morescripts/requirements.zip >> requirements.zip

az login --service-principal -u $USER -p $PASS -t $TENANT

az functionapp deployment source config-zip -g $RG -n $FUNCAPPNAME --src ./requirements.zip
