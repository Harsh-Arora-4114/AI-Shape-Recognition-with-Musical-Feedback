#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 13:08:27 2018

@author: keyur-r
"""

# CNN classifier

# Building architecture of our CNN classifier
# FIX: Use the modern tensorflow.keras namespace for all components
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import CSVLogger, EarlyStopping
# FIX: Removed 'from tensorflow.keras.models import save_model' as .save() is the preferred method
# FIX: Removed Input import as Sequential models don't need explicit Input layers


# Initialising the CNN
classifier = Sequential()

# Define image dimensions
IMG_SIZE = (28, 28)
INPUT_SHAPE = IMG_SIZE + (3,) # (28, 28, 3)

# Step - 1 Convolution
# FIX: Sequential models don't need explicit Input layer - specify input_shape in first layer
# FIX: Change Convolution2D to Conv2D and update the kernel_size syntax to (3, 3)
classifier.add(Conv2D(
    16, (3, 3), activation='relu', input_shape=INPUT_SHAPE))

# Step - 2 Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step - 3 Flattening
classifier.add(Flatten())

# Step - 4 Full connection -> First layer input layer then hidden layer
# and last softmax layer
# FIX: Removed deprecated 'kernel_initializer' argument
classifier.add(Dense(56, activation='relu'))
# Output layer with 3 classes
classifier.add(Dense(3, activation='softmax')) 

# Compiling the CNN
classifier.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# Image Preprocessing
# Add error handling for missing directories
train_dir = 'shapes/train'
test_dir = 'shapes/test'

if not os.path.exists(train_dir):
    raise FileNotFoundError(f"Training directory not found: {train_dir}")
if not os.path.exists(test_dir):
    raise FileNotFoundError(f"Test directory not found: {test_dir}")

train_datagen = ImageDataGenerator(
    rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory(
    train_dir, target_size=IMG_SIZE, batch_size=32, class_mode='categorical') # Increased batch_size for efficiency
#X_images, y_labels = training_set.filenames, training_set.classes
test_set = test_datagen.flow_from_directory(
    test_dir, target_size=IMG_SIZE, batch_size=32, class_mode='categorical') # Increased batch_size for efficiency

# Logging the training of models
csv_logger = CSVLogger('log.csv', append=True, separator=';')
early_stopping_monitor = EarlyStopping(patience=5)

# NOTE: steps_per_epoch and validation_steps should be calculated using batch_size
# len(filenames) / batch_size, but using len(filenames) is acceptable for small datasets with batch_size=1
# However, since I changed batch_size to 32, I'll calculate it properly.
BATCH_SIZE = training_set.batch_size
steps_per_epoch = max(1, training_set.samples // BATCH_SIZE)  # Ensure at least 1 step
validation_steps = max(1, test_set.samples // BATCH_SIZE)  # Ensure at least 1 step

print(f"Training samples: {training_set.samples}")
print(f"Test samples: {test_set.samples}")
print(f"Steps per epoch: {steps_per_epoch}")
print(f"Validation steps: {validation_steps}")


# FIX: Replace deprecated 'fit_generator' with the standard 'fit'
# Note: In TensorFlow 2.x, steps_per_epoch and validation_steps are optional
# but recommended for better control
print("\nStarting training...")
model_info = classifier.fit(training_set, 
                            steps_per_epoch=steps_per_epoch, 
                            epochs=25, 
                            validation_data=test_set,
                            validation_steps=validation_steps, 
                            callbacks=[csv_logger, early_stopping_monitor],
                            verbose=1)
print("\nTraining completed!")

# Save the model after training. .keras is the modern default format.
# FIX: Removed the redundant .h5 save and the deprecated save_model import/call.
print("\nSaving model...")
classifier.save('drawing_classification.keras')
print("Model saved as 'drawing_classification.keras'")