variable "azure_config" {
  description = "Configuration to deploy Gumshoe to Azure"
  type        = object({
    resource_group_name   = string
    virtual_network_name  = string
    subnet_name           = string
  })
}
