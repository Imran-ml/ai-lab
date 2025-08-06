<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx"/>
  <img src="https://img.shields.io/badge/Ollama-grey?style=for-the-badge" alt="Ollama"/>
  <img src="https://img.shields.io/badge/GPT--3-blueviolet?style=for-the-badge" alt="GPT-OSS"/>
</p> 


# GPT-OSS Chatbot with Docker

Run OpenAI’s open-sourced **GPT-OSS models (117B / 21B)** locally using Docker inside your own codebase. This project avoids third-party GUIs like Open WebUI or LM Studio to help you learn how to use GPT-based models directly in your applications.

Everything is containerized with Docker for a clean, reproducible setup. This is a fun side project designed to help others explore **running powerful language models locally**. 

✨ **Contributions are welcome!**  
Feel free to **fork the repo** and submit a **pull request** if you'd like to collaborate or enhance the project further. 


## Features

* **Simple Chat Interface:** Clean frontend to interact with the chatbot.
* **Powered by GPT-OSS:** Uses OpenAI's open GPT model (117B or 21B).
* **Dockerized:** Fully containerized using Docker Compose.
* **FastAPI Backend:** Handles the API and logic.
* **Ollama Integration:** Use Ollama to serve GPT-OSS models locally.

---

## 🔗 GPT-OSS Resources

OpenAI released the GPT-OSS models under Apache 2.0. Here's the learning path:

1. Intro to GPT-OSS: https://openai.com/index/introducing-gpt-oss  
2. Model Card & Specs: https://openai.com/index/gpt-oss-model-card/  
3. Dev Overview: https://cookbook.openai.com/topic/gpt-oss  
4. vLLM Setup Guide: https://cookbook.openai.com/articles/gpt-oss/run-vllm  
5. Harmony Format (I/O schema): https://github.com/openai/harmony  
6. PyTorch Reference Code: https://github.com/openai/gpt-oss?tab=readme-ov-file#reference-pytorch-implementation  
7. Community Site: https://gpt-oss.com/
8. Ollama: https://ollama.com/library/gpt-oss
9. HuggingFace: https://huggingface.co/openai/gpt-oss-20b

---

## Technical Details & Versions

* **Language Model:** GPT-OSS (117B or 21B)
* **Python:** 3.11-slim  
* **Backend:** FastAPI + Uvicorn  
* **Frontend Web Server:** `nginx:alpine`  
* **Serving:** `ollama/ollama` image  
* **HTTP Client:** HTTPX  
* **Containerization:** Docker & Docker Compose

---

## Directory Structure

gpt-oss-chatbot-dockerized/

├── backend/  
│   ├── main.py  
│   └── requirements.txt  
├── frontend/  
│   └── index.html  
├── docker-compose.yml  
└── Dockerfile  

---

## Prerequisites

* [Docker](https://www.docker.com/get-started)  
* Docker Compose (usually included with Docker Desktop)

---

## How to Run with Docker

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Imran-ml/gpt-oss-app-open-source
    cd gpt-oss-app-open-source
    ```

2.  **Navigate to the project directory:**
    Make sure you are in the `gpt-oss-app-open-source`.

3.  **Build and run the application using Docker Compose:**
    * Build the backend Docker image based on `Dockerfile`.
    * Pull the `ollama/ollama` image and the `nginx:alpine` image.
    * Start all defined services (Ollama, backend, frontend).
    * The `ollama` service is configured to automatically pull the **gpt-oss** model upon starting. This might take some time during the first run as the model is downloaded. From docker compsoe, in this line "sh -c "ollama serve & sleep 5 && ollama pull gpt-oss && tail -f /dev/null"" you can replace gpt-oss with gpt-oss:120b if you want 120 B model!

    ```bash
    docker-compose up --build
    ```

    You will see logs from all the containers in your terminal.

4.  **Access the Chatbot:**
    Once the services are up and running:
    * Open your web browser and go to: `http://localhost:8080` to interact with the chatbot.
    * The backend API is accessible at `http://localhost:8000`.
    * The Ollama API is at `http://localhost:11434`.

## Usage

1.  Open `http://localhost:8080` in your browser.
2.  The chat interface should load.
3.  Type your message in the input field and press Enter or click the send button to chat with the **gpt-oss** model.

## About Author
  **Name**: Muhammad Imran Zaman

  **Company**: [DOCUFY GmbH](https://docufy.de/en/home/)

  **Role**: Lead Machine Learning Engineer

  **Professional Links**:
    - HuggingFace: [Profile](https://huggingface.co/ImranzamanML)
    - Kaggle: [Profile](https://www.kaggle.com/muhammadimran112233)
    - LinkedIn: [Profile](linkedin.com/in/muhammad-imran-zaman)
    - Google Scholar: [Profile](https://scholar.google.com/citations?user=ulVFpy8AAAAJ&hl=en)
    - Medium: [Profile](https://medium.com/@imranzaman-5202)
    
- **Project Repository**: [GitHub Repo](https://github.com/Imran-ml/gpt-oss-app-open-source)
