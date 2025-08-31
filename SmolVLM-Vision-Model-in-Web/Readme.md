<p align="left">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
<img src="https://img.shields.io/badge/llama.cpp-grey?style=for-the-badge" alt="llama.cpp"/>
<img src="https://img.shields.io/badge/SmolVLM-blueviolet?style=for-the-badge" alt="SmolVLM"/>
</p>

# Real-Time AI Vision Stream with Docker

Run the **SmolVLM-500M vision language model** locally to perform real-time analysis of your camera feed.  
This project avoids complex cloud setups and third-party GUIs, providing a clear example of how to integrate a powerful multimodal AI directly into a web application.

Everything is containerized with Docker for a clean, reproducible and high-performance setup, utilizing **llama.cpp** for GPU-accelerated inference.  
This is a fun project designed to help developers explore the capabilities of running vision models locally.


<img width="2035" height="1087" alt="Screenshot 2025-08-31 200552" src="https://github.com/user-attachments/assets/98c25598-fd5b-4e64-8cb5-40e3b74a4842" />

<img width="1988" height="1058" alt="Screenshot 2025-08-31 201346" src="https://github.com/user-attachments/assets/3a3d9971-1f74-46c0-a14c-d79eba831e28" />

✨ Contributions are welcome! Feel free to fork the repo and submit a pull request if you'd like to collaborate or enhance the project further.

---

## Features
- **Live Camera Analysis**: Processes your webcam feed in real-time.  
- **Powered by SmolVLM**: Uses the efficient and powerful *SmolVLM-500M-Instruct* model.  
- **Dockerized**: Fully containerized using Docker Compose for simple, one-command setup.  
- **GPU Accelerated**: Configured to use NVIDIA GPUs via llama.cpp for fast inference.  
- **FastAPI Backend**: A lightweight Python proxy server to handle requests.  
- **Interactive Frontend**: A clean, responsive interface to provide instructions and view results.  
- **Text-to-Speech**: Vocalizes the AI's responses for a more interactive experience.  

---

## SmolVLM Model Resources
This project uses the **GGUF version of SmolVLM**, a Small Vision Language Model designed for efficiency but can use other models for better performance like Gemma.

- Hugging Face Model Card: [ggml-org/SmolVLM-500M-Instruct-GGUF](https://huggingface.co/ggml-org/SmolVLM-500M-Instruct-GGUF)  
- llama.cpp Project: [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)  

---

## Technical Details & Versions
- **Vision Language Model**: `SmolVLM-500M-Instruct-f16.gguf`  
- **Python Version**: `3.11-slim`  
- **Backend**: FastAPI + Uvicorn  
- **Inference Server**: `ghcr.io/ggerganov/llama.cpp:server`  
- **HTTP Client**: HTTPX  
- **Containerization**: Docker & Docker Compose  

---

## Directory Structure
```
SmolVLM-Vision-Model-in-Web/
├── models/
│   ├── SmolVLM-500M-Instruct-f16.gguf
│   └── mmproj-SmolVLM-500M-Instruct-f16.gguf
├── src-api/
│   ├── main.py
│   ├── requirements.txt
│   ├── index.html
│   └── Dockerfile
└── docker-compose.yml
```

---

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose (v2+).  
- An **NVIDIA GPU** with the appropriate drivers installed.  
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed to enable GPU access within Docker containers.  
- `git` for cloning the repository.  

---

## How to Run with Docker

### 1. Clone the repository
```bash
git clone https://github.com/Imran-ml/ai-lab/tree/main/SmolVLM-Vision-Model-in-Web
cd SmolVLM-Vision-Model-in-Web
```

### 2. Download the AI Models
You must download the required model files from **Hugging Face** and place them in a `models` directory.

```bash
mkdir models
```

Download the following two files into the `models` folder:
- `SmolVLM-500M-Instruct-f16.gguf`  
- `mmproj-SmolVLM-500M-Instruct-f16.gguf`  

### 3. Build and run the application
```bash
docker compose up --build
```

This command will:  
- Build the FastAPI service image  
- Pull the `llama.cpp` image  
- Start both containers  
- Load the models into your GPU memory (this may take a moment)  

### Comment this in docker compose file if you want to run on cpu

deploy:

       resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

### 4. Access the Application
Once the services are running, open your browser:  
[http://localhost:8000](http://localhost:8000)

---

## Note
- First-time model loading may take several minutes depending on your GPU.  
- Ensure your GPU drivers and CUDA toolkit are up-to-date for optimal performance.  
- To stop the services:  
  ```bash
  docker compose down
  ```

## About Author  

**Name**: Muhammad Imran Zaman  

**Company**: [DOCUFY GmbH](https://docufy.de/en/home/)  

**Role**: Lead Machine Learning Engineer  

**Professional Links**:  
- [HuggingFace](https://huggingface.co/ImranzamanML)  
- [Kaggle](https://www.kaggle.com/muhammadimran112233)  
- [LinkedIn](https://linkedin.com/in/muhammad-imran-zaman)  
- [Google Scholar](https://scholar.google.com/citations?user=ulVFpy8AAAAJ&hl=en)  
- [Medium](https://medium.com/@imranzaman-5202)  
