# Azure Queue Terraform and Python Integration Project

This project uses Terraform to set up resources in Azure, specifically a storage account, and includes Python scripts (`publisher.py` and `receiver.py`) to interact with the storage account.

## Prerequisites

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- Python 3.7+
- Required Python packages (install via `pip` as shown below)

## Azure CLI Login

Before running any Terraform commands, log in to your Azure account:

az login

This will prompt you to authenticate your Azure account in the default browser. After logging in, you will be able to manage your Azure resources via the CLI.

Terraform Commands

Initialize Terraform
Initialize the project directory to download the necessary provider plugins:

terraform init

Plan the Deployment
Generate a plan for the deployment, which shows the actions Terraform will take:

terraform plan

Apply the Deployment
Deploy the infrastructure as defined in the main.tf file:

terraform apply

Confirm the deployment by typing yes when prompted. This command will provision the specified resources in your Azure account.
Destroy the Deployment
To remove the resources created by Terraform, use the following command:

terraform destroy

This will delete the resources from your Azure account after confirmation.
Retrieving the Storage Account Connection String

After deploying the resources, you need the connection string for the Azure Storage account to interact with it via the Python scripts. Run the following command to retrieve the connection string:

az storage account show-connection-string --name <your_storage_account_name> --resource-group <your_resource_group>

Replace <your_storage_account_name> and <your_resource_group> with your actual storage account name and resource group. Copy the connection string from the output.

Updating the Python Scripts with Connection String

Once you have the connection string, add it directly to the publisher.py and receiver.py scripts by replacing the placeholder <your_connection_string> with the actual connection string.

Example:

In both publisher.py and receiver.py, find the placeholder for the connection string and update it like this:

connection_string = "<your_connection_string>"

Replace <your_connection_string> with the actual connection string retrieved from the Azure CLI command above.

Python Scripts
Installing Dependencies

The Python scripts require certain packages to interact with Azure. Install them using:

pip install azure-storage-blob


Usage

Publisher Script
The publisher.py script sends data to the storage account. Ensure the connection string is updated as described above.
Example usage:

python publisher.py

Receiver Script
The receiver.py script retrieves or processes data from the storage account. Ensure the connection string is updated as described above.
Example usage:

python receiver.py

Project Structure

main.tf - Terraform configuration file for setting up the Azure resources.
publisher.py - Python script to publish data to the Azure Storage account.
receiver.py - Python script to retrieve and process data from the Azure Storage account.