# ⚡ High-Voltage Power Line Monitoring System

[Streamlit App](https://lep-detector-mvp-v2.streamlit.app/) 
> **🎯 Click the badge above or [click here](https://lep-detector-mvp-v2.streamlit.app/) to try the Live Demo!**

An automated AI-driven solution for monitoring power line infrastructure using state-of-the-art object detection models. This project focuses on identifying power towers, insulators, and detecting potential structural defects.
<p><h2>Detection examples</h2></p>
<p>
<img src="detection_example/1.jpg" width="250">
<img src="detection_example/1_det.jpg" width="250">
  </p>
  <p>
<img src="detection_example/2.JPG" width="250">
<img src="detection_example/2_det.jpg" width="250">
</p>

## 🚀 Overview
Manual inspection of power lines is dangerous and time-consuming. This project demonstrates how Computer Vision can automate the process, providing real-time detection and health monitoring of critical electrical infrastructure.

### Key Features
* **Multi-Object Detection:** Real-time localization of transmission towers and insulators.
* **Fault Identification:** Specifically trained to recognize damaged components and environmental risks.
* **Dual-Model Comparison:** Implementation and testing of both **YOLOv11n** and the latest **YOLOv11m** architectures.
* **Interactive Web UI:** A user-friendly Streamlit interface for quick image inference and testing.
* **Django Backend:** Scalable architecture for future API integration and data management.

## 📊 Model Performance & Comparison

I evaluated two versions of the YOLO (You Only Look Once) architecture to find the optimal balance between inference speed and detection accuracy.

| Metric | YOLOv8n (Baseline) | YOLOv11n (Optimized) |
| :--- | :---: | :---: |
| **GFLOPs** | **6.6** | 71.4 |
| **Precision** | 0.7581 | **0.8527** |
| **Recall** | 0.6555 | **0.7816** |
| **mAP@50** | 0.6977 | **0.8356** |
| **mAP@50-95** | 0.5043 | **0.6258** |
| **speed inference** | **0.7ms** | 3.0ms |

Training and testing were conducted on GPU (NVIDIA GeForce RTX 4090)

<img width="1389" height="590" alt="image" src="https://github.com/user-attachments/assets/60f783d1-0675-456f-9a86-ea7a488ef197" />

### 📈 Comparative Analysis: YOLOv11n vs YOLOv11m  
The training results demonstrate a clear advantage of the **YOLOv11n** architecture for this specific dataset:  
- **Higher Precision & Recall:** YOLOv11m shows more stable growth and reaches higher peak values compared to YOLOv11n.  
- **Superior mAP Performance:** The mAP@50 metrics confirm that YOLOv11m provides better overall localization and classification accuracy for power line components.

## 🛠 Tech Stack
* **Frameworks:** Python 3.10, PyTorch, Django 5.2.
* **Computer Vision:** Ultralytics YOLOv11, OpenCV.
* **Deployment:** Streamlit Cloud (Demo), Mamba (Environment).

## 📂 Project Structure
```text
├── ml_models/           # Pre-trained weights (.pt) for v11n and v11m
├── streamlit_demo/      # Interactive demo application
├── lep_project/         # Django project core & detector app
├── requirements.txt     # Python dependencies for cloud deployment
├── packages.txt         # Linux system dependencies
└── environment.yml      # Mamba/Conda environment configuration
```

## 💻 Getting Started
1. Clone and Setup
```
git clone https://github.com/StasevichStas/LEP_detector_backend.git
cd lep_project

mamba env create -f environment.yml
mamba activate lep_monitoring
```
2. Run Streamlit Demo
```
streamlit run lep_project/streamlit_demo/app.py
```
The screenshot below shows the model selection and the result of power line detection.
<img width="1799" height="874" alt="image" src="https://github.com/user-attachments/assets/14d37c99-800e-4e02-8769-a09b9df6f115" />


4. Run Django Backend
```
cd lep_project
python manage.py migrate
python manage.py runserver
```
