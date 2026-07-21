import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers,models
print("TensorFlow Version:", tf.__version__)
(X_train,y_train),(X_test,y_test)=tf.keras.datasets.mnist.load_data()
print("Training Images:", X_train.shape)
print("Training Labels:", y_train.shape)


print("Testing Images:", X_test.shape)
print("Testing Labels:", y_test.shape)
# plt.imshow(X_train[0],cmap="gray")
# plt.title(f"Label:{y_train[0]}")
# plt.axis("off")
# plt.show()
