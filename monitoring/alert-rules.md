# Azure Monitor Alert Rules

## Alert 1: High CPU Usage

Purpose:
Detect high CPU usage in AKS containers.

Condition:
Container CPU usage crosses the defined threshold.

Demo Use:
Trigger the /cpu endpoint and observe CPU spike in Container Insights.

## Alert 2: High Memory Usage

Purpose:
Detect high memory usage in AKS containers.

Condition:
Container memory working set crosses the defined threshold.

Demo Use:
Monitor memory trend from Container Insights and Log Analytics.

## Alert 3: Pod Restart Alert

Purpose:
Detect unstable application behavior when pods restart repeatedly.

Condition:
Container restart count increases within a short time window.

Demo Use:
Trigger the /crash endpoint and check pod restart count.

## Alert 4: Application Error Logs

Purpose:
Detect application-level errors from container logs.

Condition:
Log message contains ERROR.

Demo Use:
Trigger the /error endpoint and query logs using Log Analytics.
