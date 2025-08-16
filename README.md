# Hotel Reservation Prediction - MLOps Project  

## Overview  
This project implements an end-to-end **Hotel Reservation Prediction System** using **MLOps best practices**. The workflow covers data ingestion, preprocessing, model training, experiment tracking, CI/CD automation, and deployment on Google Cloud Run.  

The goal is to predict whether a hotel reservation will be honored or canceled using structured data and scalable MLOps pipelines.  

---

## Features  
- **Data Storage**: Raw and processed datasets stored in Google Cloud Storage (GCP Bucket).  
- **Data Ingestion & Processing**: Implemented in Jupyter Notebooks and automated scripts.  
- **Model Training & Experiment Tracking**: Managed using MLflow to ensure reproducibility.  
- **Version Control**: Code versioning via GitHub, data versioning supported.  
- **CI/CD Pipeline**: Automated builds with Jenkins, containerized using Docker.  
- **Deployment**: Production-ready Flask app deployed on Google Cloud Run.  

---

## Highlights  
- Explored multiple ML models.  
- **Random Forest** gave the best performance but was too large in size.  
- **LightGBM (LGBM)** was chosen for deployment due to smaller size and comparable accuracy.  
- End-to-end reproducible MLOps workflow implemented.  

---

## Tech Stack  
- **Programming & Frameworks**: Python, Flask, Scikit-learn  
- **Frontend**: HTML, CSS (for basic UI)  
- **MLOps Tools**: MLflow, Docker, Jenkins, Git & GitHub  
- **Cloud**: Google Cloud Platform (GCP), Cloud Storage, Cloud Run  

---

## Project Workflow  
1. **Database Setup** – Google Cloud Buckets  
2. **Project Setup** – Defined folder structure and modular code  
3. **Data Ingestion** – Scripts for importing raw datasets  
4. **Data Processing** – Preprocessing and cleaning  
5. **Model Training** – Training ML models and selecting the best performer  
6. **Experiment Tracking** – MLflow for metrics and artifacts  
7. **Pipeline Building** – Automated training pipeline  
8. **Data & Code Versioning** – GitHub integration  
9. **CI/CD Deployment** – Docker + Jenkins for automation  
10. **App Building & Deployment** – Flask app deployed on Google Cloud Run  

---
## Live Preview Demo

<img width="1919" height="1077" alt="Screenshot 2025-08-16 091717" src="https://github.com/user-attachments/assets/9df48669-7bf1-405f-8c20-ab44b5231aab" />


---

## Installation & Setup  

Clone the repository:  
```bash
git clone https://github.com/logicbyavishek/HOTEL-RESERVATION-PREDICTION.git
cd HOTEL-RESERVATION-PREDICTION
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
python application.py


