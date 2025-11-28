# How to Run the Shape Classification Project

## Quick Start Commands

### Step 1: Install Dependencies (First Time Only)
```powershell
pip install -r requirements.txt
```

### Step 2: Train the Model (If model doesn't exist)
```powershell
python cnn.py
```

### Step 3: Run Predictions

**Option A: Predict a single image**
```powershell
python predict.py --image shapes/test/circles/drawing(100).png
```

**Option B: Evaluate on test dataset**
```powershell
python predict.py --testdata
```

**Option C: Evaluate on validation dataset**
```powershell
python predict.py --validationdata
```

---

## Complete Example Workflow

```powershell
# 1. Navigate to project directory (if not already there)
cd "C:\Users\arora\OneDrive\Documents\Shape Classification cnn Project\shape-classifier-cnn"

# 2. Install dependencies (first time only)
pip install -r requirements.txt

# 3. Train the model (skip if drawing_classification.keras already exists)
python cnn.py

# 4. Test on a single image
python predict.py --image shapes/test/circles/drawing(100).png

# OR evaluate on entire test set
python predict.py --testdata
```

---

## Troubleshooting

- **"Model file not found"** → Run `python cnn.py` first
- **"Module not found"** → Run `pip install -r requirements.txt`
- **"Directory not found"** → Make sure `shapes/train` and `shapes/test` folders exist


