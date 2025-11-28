Shape Classifier (Deep Learning) : Is that image a triangle or a square or a circle using CNN/Deep Learning.
==================

There are a lot of different types of shapes and it is important to be able to differentiate between them.

In this project, We have created deep convolution neural network to classify different drawing images and tag them as a triangle, square or a circle.

First we are training our model using training dataset with 3 main classes.

After that we will save our trained model into a h5 file.

We will use this pretrained model to predict our custom images(single) or image set(multiple images) from test dataset.

We are visulizing accuracy and loss of validation after each epoch using matplotlib library.

There is another dataset to practice with four categorical shapes. 


Installation
==================

To start with project just follow the few steps:

1. Navigate to the project directory:
   ```
   cd shape-classifier-cnn
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
   
This will install python libraries required for Deep Learning like TensorFlow and Keras.

**NOTE:** We are using Python 3 in this project. Python 3.7 or higher is recommended.


How to run this project
==================================================

### Step 1: Train the Model (Optional - model may already be trained)

The first step is to train the model using the training dataset. If `drawing_classification.keras` already exists, you can skip this step.

```
python cnn.py
```

This will:
- Train the CNN model on the training dataset
- Save the trained model as `drawing_classification.keras`
- Generate training logs in `log.csv`

**Note:** Training may take some time depending on your hardware.

### Step 2: Run Predictions

After training (or if the model already exists), you can run predictions in three ways:

#### Option A: Predict a single image
```
python predict.py --image <path-to-your-image>
```

Example:
```
python predict.py --image shapes/test/circles/drawing(100).png
```

This will:
- Classify the image as Circle, Square, or Triangle
- Play an audio file corresponding to the predicted shape (if available)

#### Option B: Evaluate on test dataset
```
python predict.py --testdata
```

This will:
- Classify all images in the `shapes/test` directory
- Display a confusion matrix
- Show the overall accuracy score

#### Option C: Evaluate on validation dataset
```
python predict.py --validationdata
```

This will:
- Classify all images in the `shapes/validation` directory
- Display a confusion matrix
- Show the overall accuracy score

### Troubleshooting

- **If you get "Model file not found" error**: Run `python cnn.py` first to train the model
- **If you get import errors**: Make sure all dependencies are installed: `pip install -r requirements.txt`
- **If audio doesn't play**: The audio files (Circle.mp3, Square.mp3, Triangle.mp3) should be in the `audio` folder. Audio playback requires WAV format for simpleaudio, but MP3 files are detected and a message will be shown.

Authors
==================

* **Keyur Rathod (keyur.rathod1993@gmail.com)**

License
==================

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
