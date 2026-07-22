import tensorflow as tf
import numpy as np
from PIL import Image
from PIL import ImageOps

# Load the trained model only once
model = tf.keras.models.load_model("digit_recognition_model.keras")


def predict_digit(image_path):
    """
    Predicts the handwritten digit from an image.
    """
    
    # Open image
    image = Image.open(image_path)

    
    # Convert to grayscale
    image = image.convert("L")
   
    image = ImageOps.invert(image)
    # Resize to MNIST size
    image = image.resize((28, 28))
    image.save("processed_image.png")

    # Convert image to NumPy array
    image = np.array(image)

    # Normalize pixel values (0-255 -> 0-1)
    image = image.astype("float32") / 255.0

    # Add channel dimension
    image = image.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(image)

    # Get digit with highest probability
    digit = np.argmax(prediction)

    return int(digit)