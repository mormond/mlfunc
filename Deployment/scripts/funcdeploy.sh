#!/bin/bash

USER=$1 
PASS=$2 
TENANT=$3
RG=$4
FUNCAPPNAME=$5
APPPACKAGEURI=$6

echo $USER $TENANT $RG $FUNCAPPNAME

#Install Azure CLI
echo 'Install Azure CLI'
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
echo '<<<DONE>>> Install Azure CLI'

#Grab python app package
echo 'Download Python app package'
curl  $APPPACKAGEURI >> apppackage.zip
echo '<<<DONE>>> Download Python app package'

echo 'Azure login'
az login --service-principal -u $USER -p $PASS -t $TENANT
echo '<<<DONE>>> Azure login'

echo 'Deploy function app'
az functionapp deployment source config-zip -g $RG -n $FUNCAPPNAME --src ./apppackage.zip
echo '<<<DONE>>> Deploy function app'

echo 'Done'