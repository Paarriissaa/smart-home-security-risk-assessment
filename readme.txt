Intelligent Platform for Smart Home Security Risk Prediction and Compliance Assessment

Project Description

This is an intelligent platform for assessing the security risks and compliance of Smart Home security systems built as a follow-up on undergraduate research of information security issues in smart homes.

The platform utilizes Machine Learning algorithms, cybersecurity concepts, and compliance frameworks to assess the security of smart home devices and make recommendations for improvement.

Users fill in a questionnaire concerning the security of their smart home devices and the system will predict the security risk level, compute compliance score, identify security factors and provide a downloadable security assessment report.

Motivation

There is growing adoption of smart home technologies and emergence of related privacy and cybersecurity issues.

Many people do not have proper tools for understanding whether their smart devices conform to accepted security standards and current data protection requirements.

This project solves that problem by creating an interactive security assessment tool.

Objectives
To predict the risk levels of smart home devices security
Assessing compliance with international security frameworks
Creating recommendations based on security
Using Machine Learning for security assessment
Improving explainability using feature importance techniques
Creation of an interactive web-based dashboard
System Architecture
System Architecture

User Inputs
↓

Security Feature Collection
↓

Machine Learning Prediction
↓

Compliance Evaluation
↓

Risk Interpretation
↓

PDF Report Generation

Dataset Design

A synthetic dataset of 3000 records of smart home devices has been created.

Device Categories
Camera
Smart Lock
Thermostat
Smart Speaker
Smart Sensor
Security Indicators
Password Changed
Password Strength
Multi-Factor Authentication
Firmware Updates
WiFi Security
Guest Network
Remote Access Security
Communication Encryption
Data Encryption
Manufacturer Reputation
Security Logging
Permission Review
Data Minimization
Risk Categories
Critical
High
Medium
Low
Very Low
Machine Learning Pipeline
Data Generation

Synthetic dataset creation using security profiles.

Data Preprocessing
Label Encoding
Train/Test Split
Feature Engineering
Explainable AI

Analysis of feature importance for decision explanations.

Top security factors:

Password Strength
Update Frequency
WiFi Security
Multi-Factor Authentication
Latest Firmware
Compliance Assessment

The platform checks device compliance to the following standards:

GDPR

Focus:

Data Encryption
Communication Security
Permission Management
Data Minimization

NIST Cybersecurity Framework

Focus:

Authentication
Updates
Logging
Access Control

Focus:

Secure Configuration
Encryption
Device Hardening
Dashboard Features

Security Risk Prediction

Prediction of security risk for devices using Machine Learning.

Security Score

Score calculation in range 0–100.

Compliance Evaluation

Evaluation against:

GDPR
NIST
ETSI

Security Recommendations

Personalized recommendations generation.
Security Recommendations

Create recommendations based on individual user.

Explainable Dashboard

Visualize feature importance.

PDF Report Export

Export PDF security report.

Screenshots
Dashboard


Risk Prediction


Compliance Assessment


Feature Importance Visualization


PDF Report


Project Structure

SmartHomeSecurityProject/

├── app.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore

├── data/
├── models/
├── outputs/
├── screenshots/
└── training/
Installation

Install dependencies:

pip install -r requirements.txt

Launch application:

streamlit run app.py
Technologies
Python
Streamlit
Pandas
NumPy
Scikit-Learn
Matplotlib
Joblib
ReportLab
Future Improvements
Use of real-world IoT datasets
SHAP explainability
Real-time security monitoring
Analysis of multi-device household
Deployment on cloud platform

---

 Academic Background

This work was undertaken as the final thesis project for the BSc degree in Computer Engineering.

The study covers the areas of smart home information security, risk assessment, machine learning predictive modeling, and security and data protection frameworks.

This is the application of knowledge of cybersecurity, data analysis, and software development into an integrated system.