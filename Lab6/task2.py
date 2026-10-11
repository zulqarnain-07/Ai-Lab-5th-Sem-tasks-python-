#TASK 2


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

(train_X, train_y), (test_X, test_y) = tf.keras.datasets.fashion_mnist.load_data()

print("Training shape:", train_X.shape)
print("Testing shape: ", test_X.shape)

num_classes = 10

print("Number of classes:", num_classes)
print("Single image shape:", train_X[0].shape)
print("Training samples:", len(train_X))
print("Testing samples:", len(test_X))

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]

plt.figure(figsize=(12, 6))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(train_X[i], cmap="gray")
    plt.title(class_names[train_y[i]])
    plt.axis("off")

plt.tight_layout()
plt.show()

train_X = train_X / 255.0
test_X = test_X / 255.0

train_X = train_X.reshape(-1, 28, 28, 1)
test_X = test_X.reshape(-1, 28, 28, 1)

print("Training shape after reshaping:", train_X.shape)
print("Testing shape after reshaping: ", test_X.shape)

model = Sequential([
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(28, 28, 1)
    ),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

model.summary()

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    train_X,
    train_y,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

test_loss, test_acc = model.evaluate(
    test_X,
    test_y,
    verbose=0
)

print("\nTest Loss:", test_loss)
print("Test Accuracy:", test_acc)
print("Test Accuracy: {:.2f}%".format(test_acc * 100))

sample_images = test_X[:10]
sample_labels = test_y[:10]

predictions = model.predict(sample_images)

predicted_labels = np.argmax(predictions, axis=1)

plt.figure(figsize=(15, 7))

for i in range(10):
    plt.subplot(2, 5, i + 1)

    plt.imshow(sample_images[i].reshape(28, 28), cmap="gray")

    actual_class = class_names[sample_labels[i]]
    predicted_class = class_names[predicted_labels[i]]

    if sample_labels[i] == predicted_labels[i]:
        color = "green"
    else:
        color = "red"

    plt.title(
        "Actual: " + actual_class +
        "\nPredicted: " + predicted_class,
        color=color
    )

    plt.axis("off")

plt.tight_layout()
plt.show()

print("\nIncorrectly Classified Images:")

incorrect_count = 0

for i in range(10):
    if sample_labels[i] != predicted_labels[i]:
        incorrect_count += 1

        print(
            "Image", i + 1,
            "| Actual:", class_names[sample_labels[i]],
            "| Predicted:", class_names[predicted_labels[i]]
        )

if incorrect_count == 0:
    print("All 10 selected images were classified correctly.")
else:
    print(
        "Total incorrectly classified images:",
        incorrect_count
    )
