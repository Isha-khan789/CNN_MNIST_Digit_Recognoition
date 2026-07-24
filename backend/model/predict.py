import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Load model
model = tf.keras.models.load_model("digit_recognition_model.keras")


def predict_digit(image_path):

    # Open image
    image = Image.open(image_path)

    # Convert to grayscale
    image = image.convert("L")

    # Invert colors
    image = ImageOps.invert(image)

    # Convert to NumPy array
    image = np.array(image)

    # -----------------------------
    # Find the handwritten digit
    # -----------------------------
    coords = np.argwhere(image > 50)

    # If nothing is drawn
    if len(coords) == 0:
        return -1

    # Find boundaries
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    # Crop only the digit
    image = image[y_min:y_max + 1, x_min:x_max + 1]

    # -----------------------------
    # Resize
    # -----------------------------
    image = Image.fromarray(image)
    image = image.resize((28, 28))

    # Save processed image (for debugging)
    image.save("processed_image.png")

    # Convert back to NumPy
    image = np.array(image)

    # Normalize
    image = image.astype("float32") / 255.0

    # Reshape
    image = image.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(image, verbose=0)

    digit = np.argmax(prediction)

    print("Prediction Probabilities:", prediction)
    print("Predicted Digit:", digit)

    return int(digit)