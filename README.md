# mlfunc

A project designed to demonstrate how a machine learning solution can be packaged as a Managed Application via the Azure Marketplace.

* https://docs.microsoft.com/en-us/azure/marketplace/
* https://docs.microsoft.com/en-us/azure/azure-resource-manager/managed-applications/overview

The Python code is heavily based on https://github.com/benc-uk/batcomputer - thanks to @benc-uk - converted to Azure Functions.

The application itself consists of three functions:
```
/Info
/Params
/Predict
```

More interesting is the `Deployment` folder. This contains the artefacts necessary to publish the solution as a Managed Application in the Azure Marketplace:
```
/nestedtemplates
  vmtemplate.json         - ARM template for a boostrap VM to deploy the functions code to App Service
/scripts
  funcdeploy.sh           - Custom script extension bash script to gather and deploy the Python app
  [apppackage.zip]        - Required but not included in this repo, the zipped Python app package
createUiDefinition.json   - UI elements for Azure Portal, required for a Marketplace Managed Application
mainTemplate.json         - Main ARM template which orchestrated the deployment
```
A deployment consists of an App Service Plan (Linux, consumption plan), App Service (Functions app), Storage Account and the deployment VM and it's dependencies (VNET, Disk, Public IP address etc)

The ARM template makes use of Key Vault to retrieve the secrets needed for deployment:
```
VM Secrets                - - to execute the post deployment bash script
  Username
  Password
Service Principal Secrets   - to deploy the Python app package to App Service
  Username
  Password
  TenantId
```
