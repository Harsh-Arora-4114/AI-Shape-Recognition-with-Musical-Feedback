# **AI Shape Recognition with Musical Feedback**

## **Overview**

This project focuses on classifying simple geometric shapes—**Circle, Triangle, and Square**—using **Convolutional Neural Networks (CNNs)**. Shape classification is a fundamental computer vision task that helps build intelligent systems for image recognition, educational tools, and UI automation.
The model is trained on custom or publicly available image datasets and accurately identifies shapes using deep learning techniques.

---

## **Objectives**

* Build a deep learning model to classify **three geometric shapes**.
* Apply image preprocessing and CNN-based feature extraction.
* Achieve high accuracy on custom shape datasets.
* Provide a simple and scalable pipeline for further expansion (e.g., more shapes, real-time recognition).

---

## **Key Features**

* **Data Preprocessing:** Image resizing, scaling, and augmentation.
* **CNN Architecture:** Multi-layer convolutional model to extract shape features.
* **Model Training:** Efficient training using Adam optimizer.
* **Prediction Pipeline:** Supports single-image prediction through a `.py` script.
* **Expandability:** Easily add new classes (e.g., rectangle, star, polygon).

---

## **Technologies Used**

| Category             | Tools / Libraries          |
| -------------------- | -------------------------- |
| Programming Language | Python                     |
| Deep Learning        | TensorFlow / Keras         |
| Data Processing      | NumPy, Pandas              |
| Image Handling       | OpenCV, Pillow             |
| Visualization        | Matplotlib                 |
| Environment          | Jupyter Notebook / VS Code |

---

## **Dataset**

The dataset consists of images of **Circles, Triangles, and Squares**, organized into subfolders:

```
shapes/
 ├── Circle/
 ├── Triangle/
 └── Square/
```

Each image is labeled according to its folder.
You may use:

* Custom hand-drawn images
* Synthetic shapes
* Public datasets from Kaggle

Images are preprocessed to **128×128 pixels** and normalized before training.

---

## **Project Workflow**

### **1. Data Collection & Preprocessing**

* Image resizing
* Pixel normalization
* Train-test-validation split

### **2. Exploratory Data Analysis (EDA)**

* Class distribution
* Sample visualization
* Image quality inspection

### **3. CNN Model Development**

* Convolution + ReLU layers
* Max-pooling
* Dense layers with softmax output

### **4. Model Training & Evaluation**

* Loss/accuracy tracking
* Confusion matrix
* Classification accuracy

### **5. Prediction Pipeline**

* A `predict.py` script accepts an image path
* Outputs predicted class: **circle / triangle / square**

---

## **Sample Results**

* **Accuracy achieved:** 95–99% (dataset dependent)
* **Classes:** Circle, Triangle, Square
* **Key insights:**

  * Circles are easiest to classify due to curvature
  * Triangles & squares need strong edge detection
  * CNN learns shape contours effectively

---

## **Applications**

* Educational sketch recognition tools
* Real-time shape detection

---

## **How to Run**

### **1. Clone the repository**

```
git clone https://github.com/yourusername/Shape-Classification-CNN.git
cd Shape-Classification-CNN
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

### **3. Train the model**

```
python train.py
```

### **4. Predict using an image**

```
python predict.py path/to/image.png
```

---

## **Future Scope**

* Add softmax confidence visualization
* Add more shapes (Rectangle, Star, Hexagon)
* Integrate a **drawing canvas UI** using Tkinter
* Add audio feedback (pygame) for each predicted shape
* Deploy as a web app using Flask / Streamlit

---

## License

This project is licensed under the MIT License.

## **Author**

Developed by **Harsh Arora**
---
