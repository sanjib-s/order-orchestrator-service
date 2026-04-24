# Order Orchestrator Service

A production-style sample microservice repository that demonstrates how to build, containerize, and deploy an application service to Kubernetes using both **Helm Charts** and **raw Kubernetes manifests**.

This repository is designed to showcase a complete application deployment lifecycle including:

- FastAPI-based microservice
- Docker containerization
- Kubernetes deployment manifests
- Helm chart packaging
- Horizontal Pod Autoscaling (HPA)
- Service exposure using Kubernetes Service
- Ingress routing configuration


---

#  Table of Contents

- Overview
- Project Structure
- Application Details
- API Endpoints
- Docker Build
- Kubernetes Deployment
- Helm Deployment
- Autoscaling (HPA)
- Ingress Routing
- Local Development
- Future Enhancements

---

# Overview

The **Order Orchestrator Service** is a lightweight API service built using **FastAPI** that accepts customer order requests and returns an order response.

This repository acts as a **reference project** for deploying modern microservices into Kubernetes environments using enterprise-ready deployment patterns.

---

# Project Structure

```text
order-orchestrator-service/
│── app/
│   └── main.py
│
│── Dockerfile
│── requirements.txt
│
│── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
│
│── helm/
│   └── orders-service/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── ingress.yaml
│       └── hpa.yaml
│
└── README.md

# Deployment

Docker build & Run

docker build -t order-orchestrator-service .

RUN Locally
docker run -p 8000:8000 order-orchestrator-service

Install all kubernetes Manifests
kubectl apply -f k8s/

Helm Deployment
helm install orders-service ./helm/orders-service
