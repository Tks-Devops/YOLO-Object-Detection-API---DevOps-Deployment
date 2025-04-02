# YOLO-Object-Detection-API---DevOps-Deployment
This project automates the deployment of a YOLO Object Detection API using Helm, Kubernetes, and implements logging and monitoring with the ELK stack (Elasticsearch, Logstash, Kibana) and Prometheus &amp; Grafana.

Prerequisites

Minikube or Kubernetes Cluster

Helm Installed

Docker Installed

kubectl Installed
Setup Steps

1. Clone the Repository

git clone https://github.com/yourusername/yolo-devops.git
cd yolo-devops
Setup Steps

1. Clone the Repository

git clone https://github.com/yourusername/yolo-devops.git
cd yolo-devops

2. Start Minikube (Optional, if using Minikube)
minikube start --memory=6g --cpus=2 --disk-size=20g

3. Deploy ELK Stack
kubectl apply -f logging/elasticsearch/
kubectl apply -f logging/logstash/
kubectl apply -f logging/kibana/

4. Deploy Monitoring Stack (Prometheus & Grafana)
kubectl apply -f monitoring/prometheus/
kubectl apply -f monitoring/grafana/

5. Deploy YOLO API with Helm
helm install yolo-api ./yolo-api-chart/

6. Verify Deployments
kubectl get pods
kubectl get svc

Access Services

YOLO API: http://<minikube-ip>:32132

Kibana (ELK UI): http://<minikube-ip>:5601

Grafana Dashboard: http://<minikube-ip>:3000

Prometheus UI: http://<minikube-ip>:9090

 Screenshots




Troubleshooting Guide

Elasticsearch Fails to Start:

kubectl logs -f pod/elasticsearch-xxxxx
Ensure memory and disk space are sufficient.

Grafana Not Loading:

kubectl get pods -n monitoring

Restart Grafana pod if needed.

Submission Instructions

Ensure all components are running correctly.

Push the final code and documentation to GitHub:

git add .
git commit -m "Final submission"
git push origin main

