resource "azurerm_network_interface" "_" {
  name                = "gumshoe-nic"
  location            = data.azurerm_resource_group._.location
  resource_group_name = data.azurerm_resource_group._.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = data.azurerm_subnet._.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "_" {
  name                = "gumshoe"
  resource_group_name = data.azurerm_resource_group._.name
  location            = data.azurerm_resource_group._.location
  size                = "Standard_F2"
  admin_username      = "gum"
  network_interface_ids = [
    azurerm_network_interface._.id,
  ]

  admin_ssh_key {
    username   = "gum"
    public_key = tls_private_key._.public_key_openssh
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}

resource "tls_private_key" "_" {
    algorithm = "RSA"
    rsa_bits = 4096
}