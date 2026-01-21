# EC2 System Metrics REST API

This project demonstrates how to deploy a system-level REST API on AWS EC2 and monitor it using Amazon CloudWatch.

The API exposes basic system metrics such as CPU usage, memory usage, disk usage, and uptime. It is designed to showcase cloud infrastructure skills rather than backend complexity.

---

## Architecture Overview

User → AWS Security Group → EC2 (Amazon Linux) → Flask REST API  
                                             ↓  
                                        CloudWatch Logs & Metrics

---

## Features

- REST API exposing system metrics
- Deployed on AWS EC2 (Free Tier)
- Runs as a persistent systemd service
- Secure SSH access via security groups
- CloudWatch monitoring (metrics + logs)
- Cost-aware design (instance terminated after testing)

---

## API Endpoints

| Endpoint | Description |
|--------|------------|
| `/health` | API health status |
| `/cpu` | CPU utilization |
| `/memory` | Memory usage |
| `/disk` | Disk usage |
| `/uptime` | Instance uptime |

---

## AWS Services Used

- EC2 (Compute)
- Security Groups (Networking & Security)
- IAM Role (Permissions)
- CloudWatch Metrics
- CloudWatch Logs

---

## Monitoring & Observability

CloudWatch was used to monitor:
- EC2 CPU utilization (metrics)
- Centralized application and system logs

### Sample CloudWatch Metrics
![CloudWatch CPU](screenshots/cloudwatch-cpu.png)

### Sample CloudWatch Logs
![CloudWatch Logs](screenshots/cloudwatch-logs.png)

---

## Deployment Summary

1. Launched an EC2 instance using Amazon Linux
2. Installed Python, Flask, and psutil
3. Deployed the API and configured it as a systemd service
4. Configured CloudWatch Agent for centralized logging
5. Verified metrics and logs in CloudWatch UI

> The EC2 instance was terminated after validation to avoid unnecessary cloud costs.

---

## Purpose of This Project

This project was built to demonstrate:
- Cloud compute fundamentals
- Linux service management
- Secure networking practices
- Monitoring and observability using AWS

It is intended for learning and portfolio demonstration.
