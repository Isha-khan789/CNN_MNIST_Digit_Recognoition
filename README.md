#  CNN Handwritten Digit Recognition

A full-stack AI web application that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Users can draw a digit on a canvas, and the model predicts it in real time.

##  Features

- Draw digits on an interactive canvas
- CNN model built with TensorFlow & Keras
- Real-time digit prediction
- Flask REST API
- Responsive React + Tailwind CSS frontend

## Tech Stack

**Frontend**
- React.js
- Tailwind CSS
- Axios
- HTML5 Canvas

**Backend**
- Flask
- TensorFlow
- Keras
- NumPy
- Pillow

## Model Performance

- Training Accuracy: **99.49%**
- Validation Accuracy: **99.10%**
- Test Accuracy: **99.10%**

##  Project Structure

```text
backend/
├── app.py
├── predict.py
├── train.py
└── digit_recognition_model.keras

frontend/
├── src/
└── package.json
```

##  Run the Project

### Backend

```bash
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
npm install
npm run dev
```



## 👨‍💻 Author

**Isha Khan**

⭐ If you found this project useful, consider giving it a star!
