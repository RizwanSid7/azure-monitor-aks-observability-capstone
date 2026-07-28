# KQL Queries for AKS Observability

## 1. Container Logs

Query:
ContainerLogV2
| where TimeGenerated > ago(30m)
| project TimeGenerated, PodName, ContainerName, LogMessage
| order by TimeGenerated desc

Purpose:
This query is used to check recent container logs from AKS pods.

## 2. Error Logs

Query:
ContainerLogV2
| where TimeGenerated > ago(1h)
| where LogMessage contains "ERROR"
| project TimeGenerated, PodName, ContainerName, LogMessage
| order by TimeGenerated desc

Purpose:
This query helps identify application-level error logs from containers.

## 3. Pod Restart Count

Query:
KubePodInventory
| where TimeGenerated > ago(1h)
| summarize Restarts=max(ContainerRestartCount) by PodName
| order by Restarts desc

Purpose:
This query helps detect unstable pods that are restarting frequently.

## 4. CPU Usage

Query:
Perf
| where ObjectName == "K8SContainer"
| where CounterName == "cpuUsageNanoCores"
| summarize AvgCPU=avg(CounterValue) by bin(TimeGenerated, 5m), InstanceName

Purpose:
This query helps monitor CPU usage of AKS containers.

## 5. Memory Usage

Query:
Perf
| where ObjectName == "K8SContainer"
| where CounterName == "memoryWorkingSetBytes"
| summarize AvgMemory=avg(CounterValue) by bin(TimeGenerated, 5m), InstanceName

Purpose:
This query helps monitor memory usage of AKS containers.
