![image](https://github.com/user-attachments/assets/6f3a86d2-7689-4c37-9eee-e24b84558236)

# YOLO-Object-Detection-API---DevOps-Deployment
This project automates the deployment of a YOLO Object Detection API using Helm, Kubernetes, and implements logging and monitoring with the ELK stack (Elasticsearch, Logstash, Kibana) and Prometheus & Grafana.

## Prerequisites

- Minikube or Kubernetes Cluster
- Helm Installed
- Docker Installed
- kubectl Installed

## Setup Steps

1. Clone the Repository

    ```sh
    https://github.com/Tks-Devops/YOLO-Object-Detection-API---DevOps-Deployment.git
    cd yolo-devops
    ```

2. Start Minikube (Optional, if using Minikube)

    ```sh
    minikube start --memory=6g --cpus=2 --disk-size=20g
    ```

3. Deploy ELK Stack

    ```sh
    kubectl apply -f logging/elasticsearch/
    kubectl apply -f logging/logstash/
    kubectl apply -f logging/kibana/
    ```

4. Deploy Monitoring Stack (Prometheus & Grafana)

    ```sh
    kubectl apply -f monitoring/prometheus/
    kubectl apply -f monitoring/grafana/
    ```

5. Deploy YOLO API with Helm

    ```sh
    helm install yolo-api ./yolo-api-chart/
    ```

6. Verify Deployments

    ```sh
    kubectl get pods
    kubectl get svc
    ```

## Access Services

- YOLO API: `http://<minikube-ip>:32132`
- Kibana (ELK UI): `http://<minikube-ip>:5601`
- Grafana Dashboard: `http://<minikube-ip>:3000`
- Prometheus UI: `http://<minikube-ip>:9090`

## Screenshots
![image](https://github.com/user-attachments/assets/aa313568-59e2-4813-a9f1-a23ca08824c8)


## Troubleshooting Guide

### Elasticsearch Fails to Start:

```sh
kubectl logs -f pod/elasticsearch-xxxxx


Ensure memory and disk space are sufficient.
Grafana Not Loading:
sh

kubectl get pods -n monitoring

Restart Grafana pod if needed.
Submission Instructions

Ensure all components are running correctly.

Push the final code and documentation to GitHub:
sh

git add .
git commit -m "Final submission"
git push origin main

Code
If you want to include yolov3.weights in your project but avoid GitHub's 100MB limit, you should:

    Store the file externally (Google Drive, AWS S3, or any other cloud storage).

    Modify README.md to provide a download link.

📌 Steps to Handle Large Files in GitHub
1️⃣ Upload yolov3.weights to Cloud Storage

Choose one of these options:

    Google Drive: Upload the file and generate a public link.

    AWS S3: Upload it to an S3 bucket and create a pre-signed URL for download.

    Dropbox / Any Other Storage: Upload and share the download link.

2️⃣ Update Your README.md with Instructions

Modify your README.md to guide users on how to download the weights file. Example:

# YOLO Object Detection API - DevOps Deployment

## 📂 Download YOLO Weights

To run the object detection API, you need the `yolov3.weights` file. Since GitHub restricts file sizes over 100MB, you can download it from:

👉 **[Download yolov3.weights](https://your-cloud-storage-link.com/yolov3.weights)**  

After downloading, place it in the `yolo-api/` directory:

```bash
mkdir -p yolo-api
mv yolov3.weights yolo-api/


---

### **3️⃣ Ignore `yolov3.weights` in Git**
Since the file is too large, tell Git to ignore it:

```bash
echo "yolo-api/yolov3.weights" >> .gitignore
git add .gitignore
git commit -m "Ignore yolov3.weights file"
git push origin master

✅ Final Steps

    Upload yolov3.weights to Google Drive, S3, or any cloud storage.

    Add the download link in README.md.

    Push your repo to GitHub.

Now, users can download the model separately and still use your project. 🚀







