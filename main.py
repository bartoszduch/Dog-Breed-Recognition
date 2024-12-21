import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import load_img, img_to_array


def load_data_from_directory(directory, image_size):
    images = []
    labels = []
    for label in os.listdir(directory):
        label_dir = os.path.join(directory, label)
        if os.path.isdir(label_dir):
            for filename in os.listdir(label_dir):
                img_path = os.path.join(label_dir, filename)
                img = load_img(img_path, target_size=image_size)
                img_array = img_to_array(img) / 255.0  # Normalizacja obrazów
                images.append(img_array)
                labels.append(label)
    return np.array(images), np.array(labels)

def build_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

image_size = (150, 150)
num_classes = 10
data_directory = 'data_directory'
new_data_directory = 'new_data_directory'  # Nowe dane testowe


images, labels = load_data_from_directory(data_directory, image_size)

model = build_model(input_shape=(image_size[0], image_size[1], 3), num_classes=num_classes)

# Trenowanie modelu na danych treningowych
model.fit(images, labels, epochs=10, validation_split=0.2)


new_images, new_labels = load_data_from_directory(new_data_directory, image_size)

loss, accuracy = model.evaluate(new_images, new_labels)
print("Loss:", loss)
print("Accuracy:", accuracy)
