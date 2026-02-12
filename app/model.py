import tensorflow as tf
import numpy as np
from PIL import Image

# Load your trained CNN model
model = tf.keras.models.load_model(
    "saved_model/InceptionV3_Dogs_and_Cats_Classification.h5",
    compile=False
)

# Same label order you used when training (from LabelEncoder)
CLASS_NAMES = ["Cat", "Dog"]

def preprocess_image(img: Image.Image, target_size=(256, 256)):

    img = img.convert("RGB")  # ensure 3 channels
    img = img.resize(target_size)
    img = np.array(img).astype("float32") / 255.0  # normalize
    img = np.expand_dims(img, axis=0)  # (1, 256, 256, 3)
    return img

def predict(img: Image.Image):
    # Apply preprocessing
    input_tensor = preprocess_image(img)  # (1, 256, 256, 3)

    # Model prediction (sigmoid output)
    prob = float(model.predict(input_tensor)[0][0])  # probability of class 1 (Dog) or class 0 (Cat)

    # Determine label based on 0.5 threshold
    if prob >= 0.5:
        label = CLASS_NAMES[1]  # "Dog"
    else:
        label = CLASS_NAMES[0]  # "Cat"

    # Confidence and probability dictionary
    confidence = prob if label == CLASS_NAMES[1] else 1 - prob
    prob_dict = {
        CLASS_NAMES[0]: 1 - prob,
        CLASS_NAMES[1]: prob
    }

    return label, confidence, prob_dict