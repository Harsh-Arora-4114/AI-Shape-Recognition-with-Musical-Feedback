# How to Run and Predict - Quick Guide

## Prerequisites

1. **Activate the virtual environment** (if using one):
   ```powershell
   cd shape-classifier-cnn
   .\venv\Scripts\activate
   ```

2. **Install dependencies** (if not already installed):
   ```powershell
   pip install -r requirements.txt
   ```

3. **Install audio library** (for sound playback):
   ```powershell
   pip install playsound
   ```

4. **Make sure the model exists**: The file `drawing_classification.keras` should be in the `shape-classifier-cnn` folder.
   - If it doesn't exist, train the model first: `python cnn.py`

---

## Three Ways to Run Predictions

### Method 1: Predict a Single Image (with audio!)

**Command:**
```powershell
python predict.py --image "path/to/your/image.png"
```

**Examples:**
```powershell
# Predict a test image
python predict.py --image "shapes/test/circles/drawing(100).png"

# Predict a square
python predict.py --image "shapes/test/squares/drawing(16).png"

# Predict a triangle
python predict.py --image "shapes/test/triangles/drawing(1).png"
```

**What it does:**
- Classifies the image as Circle, Square, or Triangle
- Plays an audio file (Circle.mp3, Square.mp3, or Triangle.mp3) from the `audio` folder
- Shows the prediction result

---

### Method 2: Evaluate on Test Dataset

**Command:**
```powershell
python predict.py --testdata
```

**What it does:**
- Classifies all images in the `shapes/test` directory
- Shows a confusion matrix
- Displays the overall accuracy score

---

### Method 3: Evaluate on Validation Dataset

**Command:**
```powershell
python predict.py --validationdata
```

**What it does:**
- Classifies all images in the `shapes/validation` directory
- Shows a confusion matrix
- Displays the overall accuracy score

---

## Quick Start (Using Batch Files on Windows)

### Option A: Run Test Dataset
Double-click `run.bat` or run:
```powershell
.\run.bat
```

### Option B: Predict Single Image
```powershell
.\run_single_image.bat "shapes/test/circles/drawing(100).png"
```

---

## Troubleshooting

### "Model file not found" error
**Solution:** Train the model first:
```powershell
python cnn.py
```

### "Audio playback not available"
**Solution:** Install playsound:
```powershell
pip install playsound
```

### "No module named 'tensorflow'"
**Solution:** Install dependencies:
```powershell
pip install -r requirements.txt
```

### Audio files not playing
- Make sure `Circle.mp3`, `Square.mp3`, and `Triangle.mp3` are in the `audio` folder
- Install playsound: `pip install playsound`
- Check that your system volume is not muted

---

## Expected Output

### Single Image Prediction:
```
Model loaded successfully.
Attempting to play sound file: audio/Circle.mp3
Playing sound file: audio/Circle.mp3
✓ Sound played successfully!

And shapes/test/circles/drawing(100).png is the Circle
```

### Test Dataset Evaluation:
```
Model loaded successfully.
Classify images on test dataset
Found 75 images belonging to 3 classes.
...
--- Model Evaluation ---
Confusion Matrix:
 [[25  0  0]
  [ 0 25  0]
  [ 0  0 25]]

Accuracy Score: 1.0000
------------------------
```

---

## Tips

- Make sure you're in the `shape-classifier-cnn` directory when running commands
- Image paths can be relative to the current directory or absolute paths
- The model expects images to be resized to 28x28 pixels (this happens automatically)
- Audio files must be in MP3 or WAV format

