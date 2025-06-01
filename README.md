# Image Moderation API

A secure, scalable Image Moderation API built with FastAPI, MongoDB, and Docker. This project implements a RESTful API to detect and block harmful or unwanted imagery, featuring bearer token authentication, admin-only token management, and usage tracking.

---

## 🚀 Quick Start

1. **Download and Unzip**:  
   Clone or download the repository and unzip it.

2. **Run the Project**:  
   Navigate to the project directory and run the following command to build and start the containers:  
   ```bash
   docker-compose up --build

3. **Access the Frontend**:
    Open your browser and go to:
   ```bash
    http://localhost:8080/
   ```
    Use the initial admin token:
   ```bash
    admintoken123
   ```

## Folder Structure
```bash
Image-moderation/
│
├── backend/
│   ├── app/
│   │   ├── auth.py                   # Token authentication logic
│   │   ├── image_moderation_backend.py  # Core backend logic for image moderation
│   │   ├── models.py                 # Token management (insert, delete, validate)
│   │   ├── moderation.py             # Image classification models and logic
│   │   └── .gitkeep                  # Placeholder file for empty directories
│   ├── Dockerfile                    # Backend Docker image configuration
│   ├── requirements.txt              # Backend Python dependencies
│   └── .env                          # Environment variables configuration
│
├── frontend/
│   ├── app/
│   │   ├── image_moderation_frontend.py  # Core frontend logic
│   │   └── .gitkeep                  # Placeholder file for empty directories
│   ├── Dockerfile                    # Frontend Docker image configuration
│   └── requirements.txt              # Frontend Python dependencies
│
├── docker-compose.yml                # Docker compose configuration
└── README.md                         # Project documentation
```

## Code Overview

- **`auth.py`**: Manages bearer token authentication, ensuring secure access to the API.  
- **`models.py`**: Contains logic for token management, including operations like inserting, deleting, and validating tokens.  
- **`moderation.py`**: Implements the image classification models used for moderation.

## Image Moderation Models

This project leverages two pre-trained models from Hugging Face for image classification:

1. **Falconsai/nsfw_image_detection**  
A model specifically designed for NSFW (Not Safe For Work) image detection. It classifies images into categories like "safe" or "unsafe," making it ideal for filtering harmful content. This model is lightweight and efficient for real-time moderation tasks.

2. **Facebook/deit-base-patch16-224**  
A vision transformer model (Data-efficient Image Transformer) pre-trained on ImageNet. It excels in general image classification tasks and is used here for fine-grained analysis of image content. The model processes images in 224x224 patches, providing robust feature extraction for moderation purposes.

These models work together to ensure accurate detection of harmful or unwanted imagery, balancing speed and precision.
