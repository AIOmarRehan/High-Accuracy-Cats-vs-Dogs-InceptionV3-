# Cats vs Dogs Classifier - Gradio Deployment Guide

## Overview

This project has been configured with a **Gradio web interface** for easy deployment. The UI allows users to upload images and get instant predictions about whether they contain a cat or a dog.

---

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Required packages listed in `requirements.txt`

### Setup Instructions

#### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

**Key packages:**
- `gradio` - Web UI framework
- `tensorflow` - Deep learning framework
- `pillow` - Image processing
- `numpy` - Numerical computing

#### 2. Run the Gradio Application

**Option A: Using the run script**
```bash
cd InceptionV3_Dogs_and_Cats_Classification
python run_gradio.py
```

**Option B: Direct Python execution**
```bash
cd InceptionV3_Dogs_and_Cats_Classification/app
python gradio_app.py
```

#### 3. Access the Interface
Once running, open your browser and navigate to:
```
http://localhost:7860
```

---

## Features

**Image Upload** - Upload images in any common format (JPG, PNG, etc.)  
**Webcam Support** - Capture images directly from your webcam  
**Real-time Predictions** - Get instant classification results  
**Confidence Scores** - View confidence percentages for each class  
**Probability Distribution** - See full probability breakdown (Cat vs Dog)  
**Responsive Design** - Beautiful, mobile-friendly interface  

---

## Project Structure

```
InceptionV3_Dogs_and_Cats_Classification/
├── app/
│   ├── main.py              # Original FastAPI backend
│   ├── model.py             # Model loading & preprocessing
│   └── gradio_app.py        # Gradio web interface (NEW)
├── saved_model/
│   └── InceptionV3_Dogs_and_Cats_Classification.h5  # Trained model
├── run_gradio.py            # Application launcher script (NEW)
├── requirements.txt         # Python dependencies
└── HOW TO USE IT.txt       # Original documentation
```

---

## Technical Details

### Model Information
- **Architecture:** InceptionV3 (Transfer Learning)
- **Input Size:** 256×256 pixels
- **Classes:** Cat, Dog
- **Output:** Classification + Confidence + Probabilities

### Preprocessing Pipeline
The model uses the following preprocessing (handled by `model.py`):
1. Convert image to RGB (3 channels)
2. Resize to 256×256 pixels
3. Normalize pixel values (0-1 range)
4. Prepare for inference

### Prediction Process
1. Image is preprocessed
2. Model outputs probability for Dog class
3. Threshold applied (0.5) to determine final class
4. Confidence and probability distributions calculated

---

## Deployment Options

### Local Testing
```bash
python run_gradio.py
```
- Access at: `http://localhost:7860`

### Public Sharing (Optional)
To make the interface publicly accessible:
```python
# In gradio_app.py, change the launch call:
demo.launch(share=True)  # Generates a temporary public URL
```

### Docker Deployment (Optional)
Create a `Dockerfile` in the project root:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run_gradio.py"]
```

Build and run:
```bash
docker build -t cats-dogs-classifier .
docker run -p 7860:7860 cats-dogs-classifier
```

---

## Example Usage

1. **Open the interface** in your browser (http://localhost:7860)
2. **Click "Upload Image"** and select a photo containing a cat or dog
3. **Click "Classify Image"** button
4. **View Results:**
   - Predicted Class (Cat or Dog)
   - Confidence percentage
   - Cat probability
   - Dog probability

---

## Troubleshooting

### Issue: Model not found
**Solution:** Ensure the `saved_model/` folder is in the project root directory.

### Issue: Port 7860 already in use
**Solution:** Change the port in `run_gradio.py` or `gradio_app.py`:
```python
demo.launch(server_port=7861)  # Use a different port
```

### Issue: Slow predictions
**Solution:** This is normal for the first prediction (model initialization). Subsequent predictions will be faster.

### Issue: CUDA/GPU not detected
**Solution:** The app will work with CPU. For GPU acceleration, ensure NVIDIA CUDA and cuDNN are installed.

---

## Files Overview

| File | Purpose |
|------|---------|
| `app/gradio_app.py` | Main Gradio web interface |
| `run_gradio.py` | Application launcher (recommended) |
| `app/model.py` | Model loading and preprocessing |
| `app/main.py` | Original FastAPI backend (optional) |
| `saved_model/*.h5` | Trained InceptionV3 model |
| `requirements.txt` | Python package dependencies |

---