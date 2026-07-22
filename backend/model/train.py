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
plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_train[i],cmap="gray")
    plt.title(y_train[i])
    plt.axis("off")
plt.tight_layout()
plt.show()    
print("Before plt.show()")
plt.show()
print("After plt.show()")

# NORMALIZE
X_train=X_train.astype("float32")/255.0
X_test = X_test.astype("float32") / 255.0

# reshape
X_train=X_train.reshape(-1,28,28,1)
X_test=X_test.reshape(-1,28,28,1)

# summary
print("Training Images:", X_train.shape)
print("Training Labels:", y_train.shape)

print("Testing Images:", X_test.shape)
print("Testing Labels:", y_test.shape)

print("Pixel Range:", X_train.min(), "to", X_train.max())

# model train
model=models.Sequential()

# input layer
model.add(layers.Input(shape=(28,28,1)))
# first convolution layer
model.add(
    layers.Conv2D(
        filters=32,
        activation="relu",
        kernel_size=(3,3)
    )
)
model.add(
    layers.MaxPooling2D(pool_size=(2,2))
)
model.add(
    layers.Conv2D(
        filters=64,
        kernel_size=(3,3),
        activation="relu"
    )
)
model.add(
    layers.MaxPooling2D(pool_size=(2,2))
)
model.add(layers.Flatten())

model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))

model.summary()
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
history=model.fit(
    X_train,
    y_train,
    epochs=5,
    validation_data=(X_test, y_test)
)
# evaluate mode
test_loss,test_accuracy=model.evaluate(X_test,y_test)

print("\nTest Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# make prediction
predictions=model.predict(X_test)
print("\n Predicted Digit:",np.argmax(predictions[0]))
print("Actual digit:",y_test[0])

# display prediction
plt.figure(figsize=(12,6))
for i in range(10):
    plt.subplot(2,5,i+1)

    plt.imshow(X_test[i], cmap="gray")

    prediction = np.argmax(predictions[i])

    plt.title(f"P:{prediction}  A:{y_test[i]}")

    plt.axis("off")
plt.tight_layout()
plt.show()

# ========================================
# 11. Save Model
# ========================================

model.save("digit_recognition_model.keras")

print("\nModel Saved Successfully!")