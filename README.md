# Deepfake Detection using Deep Learning

Detects deepfake images using a custom CNN (Meso4) trained on a real/fake face dataset. The system exposes a Flask REST API and a React-based web UI where users can upload an image and get a real-time prediction. This was my undergrad final year major project.

## Project Structure

```
.
├── backend/        # Flask API + ML model (training, evaluation, inference)
└── frontend/       # React web app (upload UI + results display)
```

## How It Works

1. The model is a custom **Meso4** CNN — a 6-layer convolutional network with BatchNorm, Dropout, and a sigmoid output for binary classification (Real vs. Deepfake).
2. It was trained on a dataset of real and AI-generated face images, split into Train / Validation / Test sets.
3. The Flask backend loads the trained weights and exposes a `/predict` endpoint that accepts an image upload and returns the classification result with a confidence score.
4. The React frontend lets users upload an image, sends it to the backend via `axios`, and displays the result.

## Backend

**Stack:** Python, Flask, TensorFlow/Keras, Pillow, NumPy

**Key files:**
| File | Description |
|------|-------------|
| `app.py` | Flask server — serves the API and Jinja2 templates |
| `model.py` | Meso4 model definition (Classifier base class + Meso4 architecture) |
| `train.py` | Training script with data augmentation, trains for 40 epochs |
| `test.py` | Evaluation script — reports loss and accuracy on the test set |
| `model_weights.h5` | Saved model weights after training |
| `weights/` | Additional weight snapshots (Meso4_DF, MesoInception_DF) |
| `Dataset/` | Train / Validation / Test splits, each with `Fake/` and `Real/` subfolders |

**Run the backend:**
```bash
cd backend
pip install flask flask-cors tensorflow pillow numpy
python app.py
# Runs on http://localhost:4200
```

**Train from scratch:**
```bash
python train.py   # saves model_weights.h5
```

**Evaluate on test set:**
```bash
python test.py
```

## Frontend

**Stack:** React 18, Material UI (MUI), axios, React Router

**Key files:**
| File | Description |
|------|-------------|
| `src/App.js` | Root component with routing (Home → Result) |
| `src/components/Home.js` | Image upload form |
| `src/components/Result.js` | Displays prediction result and confidence |
| `src/components/Header.js` | App header/nav |

**Run the frontend:**
```bash
cd frontend
npm install
npm start
# Runs on http://localhost:3000
```

Make sure the backend is running first — the frontend calls `http://localhost:4200/predict`.

## Model Architecture — Meso4

Input: 256×256×3 RGB image

```
Conv2D(8, 3×3) → BN → MaxPool(2×2)
Conv2D(8, 5×5) → BN → MaxPool(2×2)
Conv2D(16, 5×5) → BN → MaxPool(2×2)
Conv2D(16, 5×5) → BN → MaxPool(4×4)
Conv2D(32, 3×3) → BN → MaxPool(2×2)
Conv2D(64, 3×3) → BN → MaxPool(2×2)
Flatten → Dropout(0.5) → Dense(64) → LeakyReLU → Dropout(0.5) → Dense(1, sigmoid)
```

Output > 0.5 → **Real**, output ≤ 0.5 → **Deepfake**

Optimizer: Adam (lr=0.001), Loss: Binary Cross-Entropy
