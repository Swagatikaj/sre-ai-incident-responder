# 🚨 SRE AI Incident Responder

> An AI-powered Site Reliability Engineering platform built from scratch — featuring automated incident detection, real-time monitoring, and AI-driven root cause analysis.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Docker](https://img.shields.io/badge/Docker-29.3.1-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.35.1-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Phase 1 — Foundation](#phase-1--foundation)
- [Phase 2 — Docker + Kubernetes](#phase-2--docker--kubernetes)
- [Phase 3 — CI/CD Pipeline](#phase-3--cicd-pipeline) *(coming soon)*
- [Phase 4 — Terraform + AWS](#phase-4--terraform--aws) *(coming soon)*
- [Phase 5 — Observability](#phase-5--observability) *(coming soon)*
- [Phase 6 — ELK Stack + APM](#phase-6--elk-stack--apm) *(coming soon)*
- [Phase 7 — Kubernetes Mastery](#phase-7--kubernetes-mastery) *(coming soon)*
- [Phase 8 — AI Integration](#phase-8--ai-integration) *(coming soon)*
- [How to Run Locally](#how-to-run-locally)
- [How to Run on Kubernetes](#how-to-run-on-kubernetes)
- [API Endpoints](#api-endpoints)
- [Key SRE Concepts Demonstrated](#key-sre-concepts-demonstrated)

---

## 📖 Project Overview

This project simulates a **real-world SRE platform** built entirely from scratch using industry-standard tools. It demonstrates:

- Containerizing a Python application with Docker
- Deploying and managing workloads on Kubernetes
- Implementing CI/CD pipelines with GitHub Actions and Jenkins
- Provisioning infrastructure with Terraform
- Full observability with Prometheus, Grafana, and ELK Stack
- AI-powered incident diagnosis using the Claude API

**Built by:** Swagatika Joshi
**Purpose:** SRE/DevOps portfolio project demonstrating real-world skills
**Environment:** Mac M3, iTerm, Minikube (local Kubernetes)

---

## 🏗️ Architecture

```
                        ┌─────────────────────────────┐
                        │      GitHub Repository       │
                        │   sre-ai-incident-responder  │
                        └────────────┬────────────────┘
                                     │ git push
                                     ▼
                        ┌─────────────────────────────┐
                        │    GitHub Actions / Jenkins  │
                        │    CI/CD Pipeline            │
                        │    → run tests               │
                        │    → build Docker image      │
                        │    → deploy to K8s           │
                        └────────────┬────────────────┘
                                     │ deploy
                                     ▼
                        ┌─────────────────────────────┐
                        │      Kubernetes Cluster      │
                        │         (Minikube)           │
                        │  ┌─────────┐  ┌─────────┐   │
                        │  │  Pod 1  │  │  Pod 2  │   │
                        │  │Flask app│  │Flask app│   │
                        │  └─────────┘  └─────────┘   │
                        │         NodePort:8080         │
                        └──────┬──────────────┬────────┘
                               │              │
                    ┌──────────▼──┐    ┌──────▼──────────┐
                    │ Prometheus  │    │   ELK Stack      │
                    │ + Grafana   │    │ Logs + APM       │
                    └──────┬──────┘    └──────────────────┘
                           │ alert
                           ▼
                    ┌──────────────┐
                    │  Claude AI   │
                    │  API         │
                    │  → diagnose  │
                    │  → suggest   │
                    └──────────────┘
```

---

## 🛠️ Tech Stack

| Category | Tool | Purpose |
|----------|------|---------|
| Language | Python 3.9 | Application development |
| Framework | Flask 3.0.0 | Web application framework |
| Testing | Pytest | Automated testing |
| Containerization | Docker 29.3.1 | Container packaging |
| Container Runtime | Colima | Docker runtime on Mac |
| Orchestration | Kubernetes 1.35.1 | Container orchestration |
| Local K8s | Minikube | Local Kubernetes cluster |
| CI/CD | GitHub Actions | Automated testing + build |
| CI/CD | Jenkins | Deployment pipeline |
| IaC | Terraform | Infrastructure as Code |
| Cloud | AWS Free Tier | Cloud infrastructure |
| Metrics | Prometheus | Metrics collection |
| Visualization | Grafana | Dashboards + alerts |
| Logging | ELK Stack | Log aggregation |
| APM | Elastic APM | Application performance |
| AI | Claude API | Incident diagnosis |
| Version Control | Git + GitHub | Source control |

---

## 📁 Project Structure

```
sre-ai-incident-responder/
├── app/
│   ├── templates/
│   │   └── index.html          # UI dashboard
│   ├── __init__.py
│   └── main.py                 # Flask application
├── kubernetes/
│   ├── configmap.yaml          # App configuration
│   ├── deployment.yaml         # K8s deployment (2 replicas)
│   ├── hpa.yaml                # Horizontal Pod Autoscaler
│   ├── rbac.yaml               # Role-based access control
│   ├── secret.yaml             # Sensitive credentials
│   └── service.yaml            # NodePort service
├── tests/
│   └── test_main.py            # Pytest test suite
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions pipeline
├── conftest.py                 # Pytest configuration
├── Dockerfile                  # Container definition
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignore rules
```

---

## 🚀 Phase 1 — Foundation

### What was built
A Python Flask web application with 3 endpoints, automated tests, and GitHub repository setup.

### Tools used
- Python 3.9, Flask 3.0.0, Pytest, Git, GitHub

### Key commands

```bash
# Clone the repository
git clone https://github.com/Swagatikaj/sre-ai-incident-responder.git
cd sre-ai-incident-responder

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app/main.py

# Run tests
pytest tests/ -v
```

### Key files
- `app/main.py` — Flask application with 3 endpoints
- `tests/test_main.py` — Automated test suite
- `requirements.txt` — Python dependencies
- `conftest.py` — Pytest path configuration

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns dashboard UI |
| `/health` | GET | Health check endpoint |
| `/simulate-error` | GET | Randomly returns 200 or 500 |

### SRE concepts learned
- Health check endpoints (used by Kubernetes liveness probes)
- Automated testing as quality gates
- Error simulation for incident testing

---

## 🐳 Phase 2 — Docker + Kubernetes

### What was built
Containerized the Flask app with Docker, deployed to a local Kubernetes cluster with 2 replicas, auto-scaling, RBAC, and self-healing.

### Tools used
- Docker 29.3.1, Colima, Minikube, kubectl

### Docker commands

```bash
# Install Docker and Colima (Mac)
brew install docker docker-compose colima

# Start Colima (Docker runtime for Mac)
colima start

# Build Docker image
docker build -t sre-ai-app:v1 .

# Run container locally
docker run -d -p 8080:8080 sre-ai-app:v1

# Check running containers
docker ps

# View container logs
docker logs <container-id>

# Stop container
docker stop <container-id>
```

### Kubernetes commands

```bash
# Start Minikube cluster
minikube start --driver=docker

# Load Docker image into Minikube
minikube image load sre-ai-app:v1

# Deploy all manifests
kubectl apply -f kubernetes/

# Check all resources
kubectl get all

# Check pods
kubectl get pods

# Check logs
kubectl logs <pod-name>

# Describe a pod (detailed info)
kubectl describe pod <pod-name>

# Access app via browser
minikube service sre-ai-app-service --url

# Rolling update to new version
kubectl set image deployment/sre-ai-app sre-ai-app=sre-ai-app:v2
kubectl rollout status deployment/sre-ai-app

# Self healing test (delete a pod, watch it restart)
kubectl delete pod <pod-name>
kubectl get pods
```

### Key files
- `Dockerfile` — Container definition
- `kubernetes/deployment.yaml` — 2 replicas, liveness + readiness probes
- `kubernetes/service.yaml` — NodePort service on 8080
- `kubernetes/configmap.yaml` — Non-sensitive app config
- `kubernetes/secret.yaml` — Sensitive credentials (base64 encoded)
- `kubernetes/rbac.yaml` — ServiceAccount, Role, RoleBinding
- `kubernetes/hpa.yaml` — Auto-scale 2-5 pods based on CPU

### Kubernetes manifest reference

**`kubernetes/deployment.yaml`** — key concepts:
```yaml
replicas: 2                    # always run 2 copies
imagePullPolicy: Never         # use local image
livenessProbe:                 # restart if unhealthy
  httpGet:
    path: /health
readinessProbe:                # remove from traffic if not ready
  httpGet:
    path: /health
resources:
  requests:
    memory: "64Mi"             # guaranteed resources
    cpu: "100m"
  limits:
    memory: "128Mi"            # maximum allowed
    cpu: "200m"
```

**`kubernetes/rbac.yaml`** — key concepts:
```yaml
# Principle of least privilege
# App can only READ pods, services, configmaps
# Cannot modify or delete anything
verbs: ["get", "list", "watch"]
```

**`kubernetes/hpa.yaml`** — key concepts:
```yaml
minReplicas: 2                 # never go below 2
maxReplicas: 5                 # never go above 5
averageUtilization: 70         # scale up if CPU > 70%
```

### SRE concepts demonstrated
- **Self healing** — K8s automatically restarts crashed pods
- **High availability** — 2 replicas, no single point of failure
- **Zero downtime deployment** — rolling updates
- **Resource management** — CPU/memory requests and limits
- **Security** — RBAC with least privilege principle
- **Health checks** — liveness and readiness probes
- **Auto scaling** — HPA scales pods based on CPU

---

## 🔄 Phase 3 — CI/CD Pipeline

### GitHub Actions ✅
- Auto runs tests on every push to main
- Auto builds Docker image if tests pass
- Quality gate — build job only runs if test job passes
- View pipeline: GitHub repo → Actions tab

### Jenkins ⏳ coming soon
- Deployment pipeline
- Auto deploy to Kubernetes

---

## ☁️ Phase 4 — Terraform + AWS *(coming soon)*

- Infrastructure as Code with Terraform
- AWS Free Tier resources
- LocalStack for local AWS simulation
- `terraform destroy` for clean teardown

---

## 📊 Phase 5 — Observability *(coming soon)*

- Prometheus for metrics collection
- Grafana dashboards and alerts
- SLO/SLI tracking
- Alertmanager for notifications

---

## 📋 Phase 6 — ELK Stack + APM *(coming soon)*

- Elasticsearch for log storage
- Logstash for log processing
- Kibana for log visualization
- Elastic APM for request tracing

---

## ⚡ Phase 7 — Kubernetes Mastery *(coming soon)*

Break and fix scenarios:
- Pod crash and recovery
- Service unreachable debugging
- High CPU/memory handling
- Rolling updates and rollbacks
- ConfigMap live updates
- Ingress, Helm, Namespaces

---

## 🤖 Phase 8 — AI Integration *(coming soon)*

- Claude API integration
- Automatic log analysis on alerts
- AI-generated root cause analysis
- Suggested remediation steps

---

## 💻 How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/Swagatikaj/sre-ai-incident-responder.git
cd sre-ai-incident-responder

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run app
python app/main.py

# 5. Open browser
open http://localhost:8080

# 6. Run tests
pytest tests/ -v
```

---

## ☸️ How to Run on Kubernetes

```bash
# 1. Start Colima
colima start

# 2. Start Minikube
minikube start --driver=docker

# 3. Build and load image
docker build -t sre-ai-app:v1 .
minikube image load sre-ai-app:v1

# 4. Deploy everything
kubectl apply -f kubernetes/

# 5. Get URL
minikube service sre-ai-app-service --url

# 6. Verify everything running
kubectl get all
```

---

## 🔑 Key SRE Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| High Availability | 2 pod replicas always running |
| Self Healing | K8s restarts crashed pods automatically |
| Zero Downtime Deploy | Rolling update strategy |
| Health Checks | Liveness + readiness probes on /health |
| Auto Scaling | HPA scales 2-5 pods based on CPU |
| Security | RBAC with least privilege |
| Secret Management | K8s secrets for sensitive data |
| Config Management | ConfigMap for app configuration |
| Observability | Prometheus + Grafana (coming soon) |
| AI Operations | Claude API for incident diagnosis |

---

## 👩‍💻 Author

**Swagatika Joshi**
SRE/DevOps Engineer

> *"Built this project to demonstrate real-world SRE skills by combining infrastructure automation, observability, and AI-powered incident response."*

---

## 📄 License

MIT License — feel free to use this project as a reference for your own learning!
