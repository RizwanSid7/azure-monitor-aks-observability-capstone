\# AKS Observability Platform with Azure Monitor and Container Insights



\## Submitted By



Rizwan Siddiqui



\## Project Overview



This project demonstrates an end-to-end Azure DevOps and AKS observability workflow.



The goal of this project is to deploy a containerized Flask application on Azure Kubernetes Service and monitor it using Azure Monitor, Container Insights, Log Analytics, KQL queries, and alert rule planning.



The project also includes Azure Container Registry, Application Gateway Ingress Controller, GitHub, Azure DevOps pipeline, and a self-hosted Azure DevOps agent.



\## Architecture Flow



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

Azure Kubernetes Service  

↓  

Kubernetes Deployment + Service  

↓  

Application Gateway Ingress  

↓  

Azure Monitor + Container Insights  

↓  

Log Analytics Workspace + KQL Queries  



\## Azure Resources Used



\- Resource Group

\- Azure Container Registry

\- Azure Kubernetes Service

\- Log Analytics Workspace

\- Azure Monitor / Container Insights

\- Application Gateway

\- Application Gateway Ingress Controller

\- Azure DevOps Pipeline

\- Self-hosted Azure DevOps Agent



\## Application Endpoints



| Endpoint | Purpose |

|---|---|

| / | Home page |

| /health | Health check |

| /error | Generates application error log |

| /cpu | Generates CPU load |

| /crash | Simulates pod crash/restart |



\## Kubernetes Components



\- Namespace: observability-demo

\- Deployment: observability-app

\- Replicas: 2

\- Service: observability-service

\- Ingress: observability-ingress

\- Image: acrrizwanobs268.azurecr.io/observability-app:latest



\## CI/CD Pipeline



The Azure DevOps pipeline performs:



1\. Checkout source code from GitHub

2\. Build Docker image using Dockerfile

3\. Push image to Azure Container Registry

4\. Tag image with Build ID and latest tag



A self-hosted agent was used because Microsoft-hosted parallelism was not available in the tenant.



\## Observability Implementation



Container Insights was enabled on AKS using the monitoring add-on.



Monitoring validation included:



\- AKS node status

\- Pod status

\- Application logs using kubectl

\- Container Insights add-on verification

\- AMA / monitoring pods verification

\- KQL query testing from Log Analytics

\- Error log generation using /error endpoint

\- CPU load generation using /cpu endpoint

\- Pod restart testing using /crash endpoint



\## KQL Queries Used



\### Container Logs



```kql

ContainerLogV2

| where TimeGenerated > ago(24h)

| where PodNamespace == "observability-demo"

| project TimeGenerated, PodName, ContainerName, LogMessage

| order by TimeGenerated desc

```



\### Error Logs



```kql

ContainerLogV2

| where TimeGenerated > ago(24h)

| where PodNamespace == "observability-demo"

| where LogMessage contains "ERROR"

| project TimeGenerated, PodName, ContainerName, LogMessage

| order by TimeGenerated desc

```



\### Pod Inventory



```kql

KubePodInventory

| where TimeGenerated > ago(24h)

| where Namespace == "observability-demo"

| summarize arg\_max(TimeGenerated, \*) by PodName

| project TimeGenerated, Namespace, PodName, PodStatus, ContainerRestartCount

```



\### CPU and Memory Metrics



```kql

Perf

| where TimeGenerated > ago(24h)

| where ObjectName == "K8SContainer"

| where CounterName in ("cpuUsageNanoCores", "memoryWorkingSetBytes")

| summarize AvgValue=avg(CounterValue) by CounterName, bin(TimeGenerated, 5m)

| order by TimeGenerated desc

```



\## Troubleshooting Performed



| Issue | Root Cause | Fix |

|---|---|---|

| Docker daemon error locally | Docker Desktop was not running | Started Docker Desktop |

| Azure CLI not found in Git Bash | Azure CLI path not available in Git Bash | Used PowerShell for Azure commands |

| MFA login issue | Azure CLI required MFA | Used device code login |

| InvalidImageName in AKS pod | Wrong image path in deployment YAML | Updated image path to ACR image |

| Application Gateway timeout | Ingress annotation/reconciliation issue | Re-applied ingress annotation |

| Pipeline queued | Self-hosted agent was not running | Configured and started local Azure DevOps agent |

| Docker daemon error in pipeline | Docker Desktop not running on agent machine | Started Docker Desktop and reran pipeline |

| ACR authentication error | Service connection credentials issue | Updated ACR Docker Registry service connection |



\## Final Outcome



The project successfully demonstrates:



\- Containerized application deployment

\- AKS workload deployment

\- Application Gateway based external access

\- ACR image build and push

\- Azure DevOps pipeline execution

\- Self-hosted agent usage

\- Container Insights enablement

\- KQL-based observability approach

\- Error, CPU load, and crash simulation for monitoring demo



\## Repository



GitHub Repository:  

https://github.com/RizwanSid7/azure-monitor-aks-observability-capstone


## Detailed Project Runbooks

Detailed PDF documentation is available in the `docs/runbooks` folder.

| File | Purpose |
|---|---|
| `AKS_Observability_Capstone_GUI_Runbook.pdf` | Azure Portal GUI-based implementation guide |
| `AKS_Observability_Capstone_PowerShell_Runbook.pdf` | PowerShell, Azure CLI, Docker, kubectl, and Git command-based implementation guide |

These runbooks explain the project purpose, prerequisites, implementation steps, screenshots, troubleshooting, cost considerations, production best practices, and cleanup process.
