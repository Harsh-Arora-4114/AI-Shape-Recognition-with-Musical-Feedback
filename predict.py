#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated version with pygame audio support for Python 3.13
"""

import numpy as np
import cv2
import argparse
import os

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, accuracy_score
from myutil import probas_to_classes

# --- AUDIO SECTION: USING PYGAME (supports mp3) ----------------
import pygame

def play_sound(file_path):
    """Plays an audio file using pygame."""
    if not os.path.exists(file_path):
        print(f"Sound file not found: {file_path}")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        print(f"Playing sound: {file_path}")

        # Wait until music finishes
        while pygame.mixer.music.get_busy():
            pass

    except Exception as e:
        print(f"Error playing sound: {e}")
# ----------------------------------------------------------------


# Load the model
model_path = 'drawing_classification.keras'
try:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' not found.")
    model = load_model(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

label = {0: "Circle", 1: "Square", 2: "Triangle"}


def predict_one(file_name):
    """Predicts the class of a single image file."""
    img = cv2.imread(file_name)
    if img is None:
        print(f"Error loading image: {file_name}")
        return None

    img = cv2.resize(img, (28, 28))
    img = np.reshape(img, [1, 28, 28, 3])
    img = img / 255.0

    probabilities = model.predict(img, verbose=0)
    classes = np.argmax(probabilities, axis=1)[0]

    category = label[classes]
    print(f"\nAnd {file_name} is the {category}")
    return category


def predict_dataset(input_dir):
    """Predicts classes for a dataset."""
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Directory not found: {input_dir}")

    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(
        input_dir,
        target_size=(28, 28),
        class_mode='categorical',
        batch_size=32,
        shuffle=False
    )

    if test_generator.samples == 0:
        raise ValueError("No images found in directory.")

    steps = int(np.ceil(test_generator.samples / test_generator.batch_size))
    predict = model.predict(test_generator, steps=steps, verbose=1)
    return predict, test_generator


def main():
    parser = argparse.ArgumentParser(description="Shape Classification CNN")
    parser.add_argument('--testdata', action='store_true')
    parser.add_argument('--validationdata', action='store_true')
    parser.add_argument('--image', help="Input image file for prediction")
    args = parser.parse_args()

    on_dataset = False
    input_dir = None

    if args.testdata:
        on_dataset = True
        input_dir = "shapes/test"

    elif args.validationdata:
        on_dataset = True
        input_dir = "shapes/validation"

    if on_dataset:
        try:
            predict, test_generator = predict_dataset(input_dir)
            y_pred = probas_to_classes(predict)
            y_true = test_generator.classes

            cm = confusion_matrix(y_true, y_pred)
            ac = accuracy_score(y_true, y_pred)

            print("\n--- Model Evaluation ---")
            print("Confusion Matrix:\n", cm)
            print("\nAccuracy: {:.4f}".format(ac))
            print("------------------------\n")

        except Exception as e:
            print(f"Error: {e}")
            exit(1)

    elif args.image:
        category = predict_one(args.image)

        if category:
            audio_dir = os.path.join(os.path.dirname(__file__), 'audio')
            sound_file = os.path.join(audio_dir, f"{category}.mp3")

            if os.path.exists(sound_file):
                play_sound(sound_file)
            else:
                print(f"Audio file not found: {sound_file}")


if __name__ == '__main__':
    main()
