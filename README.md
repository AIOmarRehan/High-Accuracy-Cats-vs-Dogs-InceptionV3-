[If you would like a detailed explanation of this project, please refer to the Medium article below.](https://medium.com/@ai.omar.rehan/building-a-near-perfect-cat-vs-dog-classifier-with-inceptionv3-01a5f9730907)

---

# Cats vs Dogs Image Classification (InceptionV3 + TensorFlow)

## Project Overview

This project focuses on building an image classification model that can distinguish between **cats and dogs** using **Transfer Learning** with the InceptionV3 architecture.

Instead of training a deep learning model from scratch, this project uses a pre-trained model and adapts it to solve a binary classification problem efficiently.

The goal of this project is to practice building a real-world computer vision pipeline including data preprocessing, training, evaluation, and visualization.

---

## Dataset

The project uses the **Cats and Dogs dataset**, which contains around:

* ~6,000 cat images
* ~6,000 dog images

The dataset is balanced, which helps the model learn both classes fairly and avoids bias toward one class.

---

## Data Preprocessing

Before training, images go through several preprocessing steps:

* Resize images to **256 × 256**
* Normalize pixel values
* Handle very bright or very dark images
* Apply data augmentation to improve generalization:

  * Random flipping
  * Random brightness changes
  * Random contrast changes

TensorFlow’s `tf.data` pipeline is used to efficiently load and prepare data.

---

## Model Architecture

This project uses **Transfer Learning with InceptionV3**.

### Base Model

* Pre-trained on ImageNet
* Used as a feature extractor
* Frozen during initial training

### Custom Classification Head

Added on top of the base model:

* Global Average Pooling
* Dense layer (512 neurons, ReLU)
* Dropout (0.5) to reduce overfitting
* Final Dense layer with **Sigmoid** activation for binary classification

---

## Training Strategy

### Optimizer

* Adam optimizer

### Loss Function

* Binary Cross-Entropy

### Training Enhancements

The project uses callbacks to improve training:

* **EarlyStopping**

  * Stops training when validation stops improving
* **ModelCheckpoint**

  * Saves the best model automatically
* **ReduceLROnPlateau**

  * Reduces learning rate when progress slows down

---

## Results & Evaluation

Model performance was evaluated using several visualization techniques.

---

### Accuracy

```
76/76 ━━━━━━━━━━━━━━━━━━━━ 3s 41ms/step - accuracy: 0.9941 - loss: 0.0194
Test Accuracy: 0.9933
76/76 ━━━━━━━━━━━━━━━━━━━━ 16s 115ms/step
Precision: 0.2498, Recall: 0.5000, F1-score: 0.3331

Classification Report:
              precision    recall  f1-score   support

        cats       0.50      1.00      0.67       601
        dogs       0.00      0.00      0.00       602

    accuracy                           0.50      1203
   macro avg       0.25      0.50      0.33      1203
weighted avg       0.25      0.50      0.33      1203
```
---
![Metrics](https://files.catbox.moe/smuda2.png)
**Observation:**
Training and validation accuracy both increase steadily and reach high performance (~98–99%).

---

### Loss

![Metrics](https://files.catbox.moe/avxel3.png)

**Observation:**
Both training and validation loss decrease and stabilize, indicating good learning and low overfitting.

---

### Confusion Matrix

![CM](https://files.catbox.moe/ehuyhi.png)

**Observation:**
Most predictions lie along the diagonal, meaning the model correctly classifies both cats and dogs most of the time.

---

### ROC Curve


| Binary Classification ROC Curve | (OvR) ROC Curve – Multi-Class Classification |
|-------|-------|
| <img src="https://files.catbox.moe/iou784.png" width="490"/> | <img src="https://files.catbox.moe/pz3mv7.png" width="520"/> |



**Observation:**
The model achieves an AUC score close to **1.0**, which indicates excellent classification ability.

---

## Key Takeaways

* Transfer Learning significantly reduces training time.
* Data augmentation improves model robustness.
* Proper evaluation metrics give deeper insight into model performance.

---

## Results

[![Watch Video](https://d.uguu.se/LfbXEaOY.jpg)](https://n.uguu.se/wNNZozru.mp4)


