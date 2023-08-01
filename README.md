# Project Description

A voting application running on Kubernetes monitored with Prometheus and ELK and deployed automatically with github actions.

![Screenshot](screenshots/hld-proyecto-final.jpg)

# Application Flow

![Screenshot](screenshots/Proyecto-Final-AppOrder.jpg)

# Deployment Architecture

The deployment consists of the following:

1 - Infrastructure as Code (IaC) with Terraform. See [IaC README.md](https://github.com/KeepCodingCloudDevops7/kc7-equipo5/blob/main/terraform/README.md)
  - An AWS EKS cluster deployed in different AZ.
  - Application Load Balancer with least-privilege policies.
  - Helm charts that deploy
    - AWS ALB
    - AWS EBS
    - kube-metrics
    - Prometheus
    - Grafana
    - Vertical Pod Autoscaler
    - Cluster Autoscaler
    - ArgoCD

2 - Git Operations (GitOps).
  - Image build and upload after committing to the application folder in the `main` branch.  See [Application README.md](https://github.com/KeepCodingCloudDevops7/kc7-equipo5/blob/main/application/application-vote/README.md)
  - ArgoCD to track and deploy changes to the application.
  - Repository changes monitoring with Discord Webhooks.


![Screenshot](screenshots/discord-3.png)

3 - Automated Pipelines (GitHub Actions). See [Repository GitHub Actions](https://github.com/KeepCodingCloudDevops7/kc7-equipo5/actions)
  - IaC
    - Create AWS EKS Cluster
    - Destroy AWS EKS Cluster
    - Update DNS to AWS ALB
  - Application    
    - Build application images.
    - Upload app image to Docker Hub.
    - Updates new image to K8s application manifests.

4 - External Monitoring
  - Metrics gathering (kube-metrics and Prometheus)
  - Grafana Dashboards
  - Grafana Alerting
  
## Installation

1 - Clone this repository

2 - Deploy the EKS cluster. See [IaC README.md](https://github.com/KeepCodingCloudDevops7/kc7-equipo5/blob/main/terraform/README.md)

3 - Wait for a few minutes and make your vote at: http://vote.omai.ltd/

4 - See the results at: http://result.omai.ltd/

5 - **OPTIONAL**. Monitor the Cluster Resources at [Grafana Dashboards](http://grafana.omai.ltd/dashboards)


# Folder Structure

```
├── kc7-equipo5/
│   ├── .github
│   │   ├── .workflows
│   │   │   ├── <git hub actions>.yml
│   ├── application
│   │   │   ├── application-vote/
│   │   │   ├── performance-test/
│   ├── app-k8s-resources
│   │   │   ├── app/
│   ├── terraform/
│   │   ├── eks/
│   │   ├── helm/
│   │   ├── networking/
│   │   ├── security/
│   │   ├── service-files/
│   │   │   ├── application-vote/
│   │   │   ├── cluster-autoscaler/
│   │   │   ├── grafana/
│   │   │   ├── vertical-pod-autoscaler/
│   ├── screenshots
```
