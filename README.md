**LSTM Project**

# 🧠 LSTM Next Word Prediction

This project is a **Deep Learning-based Next Word Prediction system** that uses an **LSTM (Long Short-Term Memory)** model to predict the next word in a sentence.

It works similar to **autocomplete features** used in mobile keyboards and search engines.

---

## 🚀 Features

* 🔤 Predicts the next word based on input text
* 🧠 Built using LSTM (RNN-based architecture)
* ⚡ Real-time predictions using Streamlit UI
* 💾 Pre-trained model support
* 📚 Easy to understand and beginner-friendly

---

## 📂 Project Structure

```
├── lstm_model.h5        # Trained LSTM model
├── tokenizer.pkl        # Saved tokenizer
├── max_len.pkl          # Maximum sequence length
├── main.py               # Streamlit UI
├── Word_prediction.ipynb # Model training notebook
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

1. 📚 Text data is collected and cleaned
2. 🔤 Tokenizer converts words into numbers
3. 📏 Sequences are padded to equal length
4. 🧠 LSTM model is trained on sequences
5. 🎯 Model predicts the next word using probability

---

## 🧪 Example

**Input:**

```
I love deep learning
```

**Output:**

```
I love deep learning models
```

---

## ▶️ Run the Project

### 1️⃣ Install Dependencies

```bash
pip install tensorflow streamlit numpy
```

---

### 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 🧠 Model Details

* Architecture: LSTM Neural Network
* Framework: TensorFlow / Keras
* Loss Function: Sparse Categorical Crossentropy
* Optimizer: Adam

---

## 📓 Training

You can train the model using:

👉 `Word_prediction.ipynb`

This notebook includes:

* Data preprocessing
* Tokenization
* Sequence generation
* Model training

---

## 📌 Files Explained

* **lstm_model.h5** → Trained deep learning model
* **tokenizer.pkl** → Converts text to sequences
* **max_len.pkl** → Stores max sequence length
* **main.py** → Streamlit UI for prediction
* **Word_prediction.ipynb** → Training notebook

---

## 🔥 Future Improvements

* Add top-k predictions (multiple suggestions)
* Improve dataset for better accuracy
* Use Transformer models (GPT-like)
* Deploy on cloud (Render / HuggingFace)

---

## 🤝 Contributing

Feel free to fork this repository and improve it!

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Shashank Singh

---

⭐ If you like this project, don’t forget to star the repo!

