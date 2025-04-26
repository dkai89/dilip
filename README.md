# 🏠 House Price Predictor - AI Model Deployment

This project demonstrates how to deploy a Machine Learning model using FastAPI, Docker, and AWS Cloud.

## 🚀 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload
```

Go to: [http://localhost:8000/docs](http://localhost:8000/docs) to test API.

## 🐳 Run with Docker

```bash
docker build -t house-price-predictor .
docker run -p 80:80 house-price-predictor
```

Then visit: [http://localhost](http://localhost)

## ☁️ How to Deploy on AWS

- Push Docker image to ECR
- Deploy container using ECS Fargate / EC2 instance / EKS Kubernetes
- Set up load balancer (optional) for public access

## 📚 Tech Stack

- Python 3.11
- FastAPI
- Docker
- AWS Cloud (EC2, ECS, ECR)
