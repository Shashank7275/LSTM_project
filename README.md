<h1 align="center">🧠 LSTM Next Word Prediction System</h1>

<h3 align="center">🚀 Deep Learning | NLP | Streamlit App</h3>

<p align="center">
A powerful <b>Next Word Prediction system</b> built using <b>LSTM (Long Short-Term Memory)</b> networks.
</p>

<hr>

<h2>🌟 Project Overview</h2>

<p>
This project uses <b>Natural Language Processing (NLP)</b> and <b>Deep Learning</b> 
to predict the next word in a sentence.
</p>

<ul>
<li>Data preprocessing</li>
<li>Tokenization</li>
<li>Sequence generation</li>
<li>LSTM model training</li>
<li>Real-time prediction via Streamlit</li>
</ul>

<hr>

<h2>🎯 Key Features</h2>

<ul>
<li>✨ Smart Text Prediction</li>
<li>⚡ Real-Time UI (Streamlit)</li>
<li>🧠 Deep Learning Powered (LSTM)</li>
<li>📦 Pre-trained Model Support</li>
<li>📊 Efficient Text Processing</li>
<li>🔁 Scalable Architecture</li>
</ul>

<hr>

<h2>🖥️ System Architecture</h2>

<pre>
User Input ➝ Tokenizer ➝ Sequence Padding ➝ LSTM Model ➝ Predicted Word
</pre>

<hr>

<h2>📂 Project Structure</h2>

<pre>
├── lstm_model.h5
├── tokenizer.pkl
├── max_len.pkl
├── app.py
├── Word_prediction.ipynb
└── README.md
</pre>

<hr>

<h2>⚙️ How It Works</h2>

<h4>1️⃣ Data Preprocessing</h4>
<ul>
<li>Convert text to lowercase</li>
<li>Remove unwanted characters</li>
</ul>

<h4>2️⃣ Tokenization</h4>
<ul>
<li>Words → Numerical sequences</li>
</ul>

<h4>3️⃣ Sequence Generation</h4>
<ul>
<li>Create n-gram sequences</li>
</ul>

<h4>4️⃣ Padding</h4>
<ul>
<li>Ensure equal input length</li>
</ul>

<h4>5️⃣ Model Training</h4>
<ul>
<li>Train LSTM on sequences</li>
</ul>

<h4>6️⃣ Prediction</h4>
<ul>
<li>Predict next word using probabilities</li>
</ul>

<hr>

<h2>🧪 Example</h2>

<b>Input:</b>
<pre>Machine learning is</pre>

<b>Output:</b>
<pre>Machine learning is amazing</pre>

<hr>

<h2>📊 Model Architecture</h2>

<pre>
Embedding Layer → LSTM Layer → Dense Layer (Softmax)
</pre>

<ul>
<li><b>Embedding Dimension:</b> 100</li>
<li><b>LSTM Units:</b> 150</li>
<li><b>Loss:</b> Sparse Categorical Crossentropy</li>
<li><b>Optimizer:</b> Adam</li>
</ul>

<hr>

<h2>📈 Workflow</h2>

<pre>
Text Data
   ↓
Tokenization
   ↓
Sequence Creation
   ↓
Padding
   ↓
LSTM Training
   ↓
Prediction Output
</pre>

<hr>

<h2>▶️ Run the Project</h2>

<h4>🔧 Install Dependencies</h4>

<pre><code>pip install tensorflow streamlit numpy</code></pre>

<h4>▶️ Start App</h4>

<pre><code>streamlit run app.py</code></pre>

<hr>

<h2>📓 Training the Model</h2>

<p>Use <b>Word_prediction.ipynb</b> for:</p>

<ul>
<li>Data loading</li>
<li>Preprocessing</li>
<li>Model building</li>
<li>Training & saving</li>
</ul>

<hr>

<h2>📌 File Descriptions</h2>

<table border="1" cellpadding="8" cellspacing="0">
<tr>
<th>File</th>
<th>Description</th>
</tr>
<tr>
<td>lstm_model.h5</td>
<td>Trained deep learning model</td>
</tr>
<tr>
<td>tokenizer.pkl</td>
<td>Text → sequences</td>
</tr>
<tr>
<td>max_len.pkl</td>
<td>Sequence length</td>
</tr>
<tr>
<td>app.py</td>
<td>Streamlit UI</td>
</tr>
<tr>
<td>Word_prediction.ipynb</td>
<td>Training notebook</td>
</tr>
</table>

<hr>

<h2>🚀 Future Improvements</h2>

<ul>
<li>🔥 Top-K Predictions</li>
<li>🤖 Transformer models (GPT / BERT)</li>
<li>🎤 Voice input</li>
<li>☁️ Cloud deployment</li>
<li>📱 Mobile UI</li>
</ul>

<hr>

<h2>🧠 Learning Outcomes</h2>

<ul>
<li>NLP fundamentals</li>
<li>Sequence modeling</li>
<li>LSTM networks</li>
<li>Streamlit deployment</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p><b>Shashank Singh</b></p>

<hr>

<h2>⭐ Support</h2>

<p>
👉 Star ⭐ the repo <br>
👉 Share with others
</p>

<hr>

<h2>💡 Inspiration</h2>

<ul>
<li>Google Autocomplete</li>
<li>Smartphone keyboards</li>
<li>AI writing assistants</li>
</ul>

<hr>

<p align="center"><b>🚀 Build. Learn. Improve. Repeat.</b></p>
