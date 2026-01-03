
```markdown
# Multimodal Real Estate Price Predictor

This project implements a Multimodal Regression Pipeline to predict property market values. It combines **tabular data** (housing features like bedrooms, sqft) with **satellite imagery** (visual environmental context) to train a deep learning model.

## 📂 Project Structure
Ensure your Google Drive folder is organized as follows:
```text
My Drive/
└── Real_Estate_Project/
    ├── train(1).xlsx          # Training dataset
    ├── test.xlsx              # Test dataset
    ├── images/                # Folder for satellite images (created automatically)
    ├── submission.csv         # Final output file
    ├── best_model.keras       # Saved model (created during training)
    └── processed_data.pkl     # Preprocessed data checkpoint

```

---

## 🚀 Setup & Installation

### Step 1: Google Drive Setup

1. Create a folder named `Real_Estate_Project` in your Google Drive.
2. Upload the `train(1).xlsx` and `test.xlsx` datasets into this folder.

### Step 2: Initialize Google Colab

1. Open [Google Colab](https://colab.research.google.com/) and create a new notebook.
2. **Mount Google Drive** by running the following code in the first cell:

```python
from google.colab import drive
drive.mount('/content/drive')
print("Setup complete!")

```

### Step 3: Install Dependencies

Install the required libraries (PyTorch, OpenCV, etc.) by running:

```python
!pip install -q torch torchvision opencv-python-headless

```

---

## 📊 Phase 1: Exploratory Data Analysis (EDA)

Perform EDA to understand the distribution of the data. Analyze key features like price, square footage, and correlations before moving to the deep learning pipeline.

---

## 🌍 Phase 2: Data Acquisition (Satellite Imagery)

We use the **Mapbox Static Images API** to download satellite images based on the `lat` (Latitude) and `long` (Longitude) of each property.

1. **Get API Key:** Go to [Mapbox.com](https://www.mapbox.com/), create an account, and generate a public API Access Token.
2. **Create Image Folder:** Create a folder named `images` inside your project directory.
3. **Run Data Fetcher:**
* Insert the code from `data_fetcher.py` into a cell.
* **Update the `MAPBOX_TOKEN**` variable with your own key.
* Run the cell. This will programmatically download images for both train and test datasets.



---

## 🛠 Phase 3: Data Preprocessing

1. Insert the code from `preprocessing.ipynb`.
2. Run the cell to perform data cleaning, feature scaling, and image processing.
3. **Outcome:** This saves a `processed_data.pkl` file to your Drive. This checkpoint allows you to skip preprocessing in future runs.

> **⚠️ IMPORTANT: GPU Setup**
> Before moving to the next step, you **must** enable GPU acceleration.
> 1. Go to **Runtime** > **Change runtime type**.
> 2. Select **T4 GPU** under Hardware accelerator.
> 3. Click **Save**.
> 4. If prompted, click **"Run all"** to re-initialize the environment.
> 
> 

---

## 🧠 Phase 4: Model Training

1. Insert the code from `model_training.ipynb`.
2. **Run the training loop.** * *Note:* This process reads images directly from Google Drive, which may result in a training time of **approx. 1-2 hours**. Please keep your browser open and laptop on during this duration.
* *Optimization Tip:* For faster training, you can modify the code to copy images to the local Colab runtime (`/content/`) before training.


3. **Outcome:** The best performing model will be automatically saved as `best_model.keras` in your project folder.

---

## 🔮 Phase 5: Prediction & Inference

1. Insert the code from `test_prediction.ipynb`.
2. Run the cell.
3. **Outcome:**
* The script loads `best_model.keras`.
* It generates predictions for the `test.xlsx` dataset.
* A final file named `test_prediction.csv` is saved to your project folder.



### Using New Data

To predict prices for a completely new dataset (apart from `test.xlsx`):

1. Ensure the new Excel file is in the Drive folder.
2. Run the **Data Fetcher** step to download images for the new coordinates.
3. Run the **Test Prediction** step, pointing it to the new filename.

```

```
