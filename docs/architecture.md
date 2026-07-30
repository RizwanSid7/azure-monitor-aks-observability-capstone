\# Architecture



\## Application Access Flow



User

↓

Application Gateway Public IP

↓

Application Gateway Ingress Controller

↓

Kubernetes Ingress

↓

Kubernetes Service

↓

AKS Pods

↓

Flask Application



\## CI/CD Flow



GitHub Repository

↓

Azure DevOps Pipeline

↓

Self-hosted Agent

↓

Docker Build

↓

Azure Container Registry

↓

AKS Deployment



\## Monitoring Flow



AKS Pods

↓

Container Insights / AMA Logs

↓

Azure Monitor

↓

Log Analytics Workspace

↓

KQL Queries

↓

Troubleshooting and Alert Planning



\## Key Azure Resources



\- Resource Group: rg-aks-observability-capstone

\- AKS Cluster: aks-observability-capstone

\- ACR: acrrizwanobs268

\- Log Analytics Workspace: law-aks-observability

\- Application Gateway: appgw-observability

\- Namespace: observability-demo

\- Deployment: observability-app

\- Service: observability-service

\- Ingress: observability-ingress

