# 🚀 Flask Chatbot - Deployed on Google Cloud Run

This is a simple chatbot built using **Python, Flask, and Google Cloud Run**. The chatbot responds to basic user inputs using `if-elif-else` statements.

## 🌟 Features
- Built with **Flask** as a REST API
- Supports **basic chatbot responses**
- Deployable on **Google Cloud Run** using Docker

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### **2️⃣ Install Dependencies**
Make sure you have **Python 3.10+** installed, then install dependencies:
```sh
pip install -r requirements.txt
```

### **3️⃣ Run Locally**
Start the Flask chatbot server:
```sh
python app.py
```

#### **Test Locally with `curl`**
Open a new terminal and run:
```sh
curl -X POST http://127.0.0.1:8080/chat -H "Content-Type: application/json" -d '{"message": "Hello"}'
```
Expected Response:
```json
{"response": "Hi there! How can I help you today?"}
```

---

## 🚀 Deployment to Google Cloud Run

### **1️⃣ Enable Google Cloud Services**
Login to Google Cloud and enable Cloud Run:
```sh
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com
```

### **2️⃣ Build and Push Docker Image**
```sh
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/chatbot
```

### **3️⃣ Deploy to Cloud Run**
```sh
gcloud run deploy chatbot --image gcr.io/YOUR_PROJECT_ID/chatbot --platform managed --region us-central1 --allow-unauthenticated
```

### **4️⃣ Get Your Live URL**
After deployment, Cloud Run will return a public URL like:
```
https://chatbot-xyz-uc.a.run.app
```
Use this URL to access your chatbot!

---

## 📁 Project Structure
```
📂 Chatbot-Project/
 ├── 📄 app.py           # Main Flask API
 ├── 📄 requirements.txt # Dependencies
 ├── 📄 Dockerfile       # Deployment Config
 ├── 📄 .gitignore       # Ignore unnecessary files
 ├── 📄 README.md        # Documentation
```

---

## 📜 License
This project is open-source and free to use!

💡 **Need Help?** Feel free to create an issue in the repository! 😊

