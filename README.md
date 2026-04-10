# DeploySentry
____________________________________
DeploySentry is an entry-level DevOps project that demonstrates CI/CD automation,
containerized deployment, monitoring, and basic recovery mechanisms.

## Tech Stack
________________________________
- Python (Flask)
- Docker
- Kubernetes
- GitHub Actions
- Prometheus
- Bash

## Features
________________________
- CI/CD pipeline triggered on GitHub push
- Dockerized application
- Kubernetes deployment and service
- Application health endpoint
- Monitoring configuration
- Rollback automation

## Workflow
_______________________________
1. Code is pushed to GitHub
2. CI pipeline builds Docker image
3. Application is deployed to Kubernetes
4. Monitoring tracks application health
5. Rollback script can restore last stable deployment

## Architecture
_______________________
User → CI/CD Pipeline → Application Service → Monitoring Service → Metrics Controller

## New Features
___________________
Added monitoring service for tracking CPU and memory usage
Implemented centralized metrics collection
Introduced basic alerting system
Added retry logic for fault tolerance
Implemented logging for debugging and traceability

## Learning Outcomes (UPDATED)
_____________________________
Understanding CI/CD workflow basics
Monitoring and observability concepts
Fault tolerance and retry mechanisms
Multi-service communication using Docker

# LIPSA PATTANAIK | ITER SOA UNIVERSITY

## Run Locally
_______________________________________
```bash
docker build -t deploysentry .
docker run -p 5000:5000 deploysentry


