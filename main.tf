provider "azurerm" {
  features {}
  subscription_id = "80a83f89-1022-4491-8116-5505e640a105"
}

resource "azurerm_resource_group" "cloudrisedev" {
  name     = "queue-storage-demo"
  location = "East US"
}

resource "azurerm_storage_account" "cloudrisedev" {
  name                     = "cloudrisedevaccount"
  resource_group_name      = azurerm_resource_group.cloudrisedev.name
  location                 = azurerm_resource_group.cloudrisedev.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
} 

resource "azurerm_storage_queue" "cloudrisedev" {
  name                 = "cloudrisedev-messages-queue"
  storage_account_name = azurerm_storage_account.cloudrisedev.name
}
