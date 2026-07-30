# Project Runbooks

This folder contains detailed PDF documentation for the AKS Observability Capstone project.

## Files Included

### 1. AKS_Observability_Capstone_GUI_Runbook.pdf

This PDF explains the project using Azure Portal GUI steps.

Use this runbook if you want to understand how the project was created manually from the Azure Portal, including:

- Resource Group creation
- Azure Container Registry
- AKS overview
- Application Gateway
- Container Insights
- Log Analytics
- Azure DevOps screenshots
- Portal-based validation steps

### 2. AKS_Observability_Capstone_PowerShell_Runbook.pdf

This PDF explains the same project using PowerShell, Azure CLI, Docker, kubectl, and Git commands.

Use this runbook if you want to reproduce the project using commands.

It includes:

- Project setup commands
- Docker build and run commands
- Azure CLI commands
- ACR commands
- AKS deployment commands
- Kubernetes commands
- Log Analytics / KQL commands
- Azure DevOps pipeline validation
- Cleanup commands

## Recommended Reading Order

1. Start with the main README.md file in the repository.
2. Read the GUI Runbook to understand the architecture and portal flow.
3. Read the PowerShell Runbook to reproduce the project step by step.
4. Review the screenshots folder for practical implementation proof.

## Purpose

These runbooks are added so that a new user, student, trainer, or reviewer can understand the complete project without depending only on screenshots or commands.

They explain not only what was done, but also why each component was used.
