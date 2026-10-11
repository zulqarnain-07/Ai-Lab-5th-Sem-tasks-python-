
import os
import numpy as np
import tensorflow as tf
import kagglehub
import matplotlib.pyplot as plt

from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping

path = kagglehub.dataset_download("abdallahalidev/plantvillage-dataset")

data_dir = None

for root, dirs, files in os.walk(path):
    if os.path.basename(root).lower() == "color":
        data_dir = root
        break

if data_dir is None:
    raise FileNotFoundError("Could not find the color dataset folder.")

print("Dataset path:", data_dir)

img_size = (128, 128)
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=img_size,
    batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=img_size,
    batch_size=batch_size
)

class_names = train_ds.class_names
num_classes = len(class_names)

print("Number of classes:", num_classes)
print("Classes:", class_names)

train_ds = train_ds.map(
    lambda x, y: (x / 255.0, y)
)

val_ds = val_ds.map(
    lambda x, y: (x / 255.0, y)
)

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

model = models.Sequential([
    layers.Input(shape=(128, 128, 3)),

    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10,
    callbacks=[early_stop]
)

loss, accuracy = model.evaluate(val_ds)

print("Validation Loss:", round(loss, 4))
print("Validation Accuracy:", round(accuracy * 100, 2), "%")

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("CNN Plant Disease Detection")
plt.legend()
plt.show()


model.save("plant_disease_model.keras")
print("Model saved successfully!")

image_path = input("Enter the path of a leaf image: ")

if os.path.isfile(image_path):
    img = tf.keras.utils.load_img(
        image_path,
        target_size=img_size
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)
    predicted_index = np.argmax(prediction[0])

    print("Predicted Class:", class_names[predicted_index])
    print("Confidence:", round(
        float(prediction[0][predicted_index]) * 100, 2
    ), "%")

    plt.imshow(img)
    plt.title(class_names[predicted_index])
    plt.axis("off")
    plt.show()
else:
    print("Image file not found. Please check the path.")
