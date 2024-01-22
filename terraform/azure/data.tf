data "azurerm_resource_group" "example" {
  name = var.azure_config.resource_group_name
}

data "azurerm_virtual_network" "example" {
  name                = var.azure_config.virtual_network_name
  resource_group_name = data.azurerm_resource_group.example.name
}

data "azurerm_subnet" "example" {
  name                 = var.azure_config.subnet_name
  virtual_network_name = data.azurerm_virtual_network.example.name
  resource_group_name  = data.azurerm_resource_group.example.name
}
