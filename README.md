<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧠 LSTM Next Word Prediction System</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            animation: fadeInUp 1s ease-out;
        }
        
        .main-title {
            font-size: 3.5em;
            font-weight: 700;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #f9ca24);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease infinite, bounceIn 1.2s ease-out;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.3em;
            color: rgba(255,255,255,0.9);
            font-weight: 300;
            animation: fadeInUp 1s ease-out 0.3s both;
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 30px;
            margin: 20px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 25px 45px rgba(0,0,0,0.1);
            animation: slideInUp 0.8s ease-out;
            transition: all 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 35px 60px rgba(0,0,0,0.2);
        }
        
        .section-title {
            font-size: 2.2em;
            font-weight: 600;
            color: white;
            margin-bottom: 20px;
            position: relative;
            display: inline-block;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 50px;
            height: 4px;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
            border-radius: 2px;
            animation: expand 1s ease-out;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(255,255,255,0.1);
        }
        
        .feature-card:hover {
            transform: translateY(-15px) scale(1.05);
            background: rgba(255, 255, 255, 0.15);
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 15px;
            display: block;
        }
        
        .demo-input {
            background: rgba(0,0,0,0.3);
            border: 2px solid rgba(255,255,255,0.3);
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            color: white;
            font-size: 1.5em;
            text-align: center;
            font-family: 'Courier New', monospace;
            transition: all 0.3s ease;
            animation: pulse 2s infinite;
        }
        
        .demo-input::before {
            content: "➝ ";
            animation: blink 1s infinite;
        }
        
        .demo-output {
            background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
            border-radius: 15px;
            padding: 20px;
            color: white;
            font-size: 1.5em;
            font-weight: 600;
            margin-top: 10px;
            transform: scale(0);
            animation: popIn 0.6s ease-out 0.5s forwards;
        }
        
        .architecture-flow {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 40px 0;
            flex-wrap: wrap;
            gap: 20px;
        }
        
        .flow-step {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            min-width: 120px;
            position: relative;
            animation: flowIn 0.8s ease-out forwards;
            opacity: 0;
        }
        
        .flow-step:nth-child(1) { animation-delay: 0.1s; }
        .flow-step:nth-child(2) { animation-delay: 0.2s; }
        .flow-step:nth-child(3) { animation-delay: 0.3s; }
        .flow-step:nth-child(4) { animation-delay: 0.4s; }
        .flow-step:nth-child(5) { animation-delay: 0.5s; }
        
        .flow-arrow {
            font-size: 2em;
            color: #4ecdc4;
            animation: bounce 2s infinite;
        }
        
        .code-block {
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            color: #00ff88;
            overflow-x: auto;
            position: relative;
        }
        
        .code-block::before {
            content: '$ ';
            color: #ff6b6b;
        }
        
        .table-container {
            overflow-x: auto;
            margin: 20px 0;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            overflow: hidden;
        }
        
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }
        
        th {
            background: rgba(255,255,255,0.2);
            font-weight: 600;
        }
        
        .future-features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .future-item {
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            color: white;
            font-weight: 500;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .future-item:hover {
            transform: translateY(-5px) rotate(2deg);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }
        
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 30px;
            color: rgba(255,255,255,0.8);
        }
        
        /* Animations */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes slideInUp {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes bounceIn {
            0% { transform: scale(0.3); opacity: 0; }
            50% { transform: scale(1.05); }
            70% { transform: scale(0.9); }
            100% { transform: scale(1); opacity: 1; }
        }
        
        @keyframes expand {
            from { width: 0; }
            to { width: 50px; }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }
        
        @keyframes popIn {
            0% { transform: scale(0); opacity: 0; }
            70% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(1); }
        }
        
        @keyframes flowIn {
            from { opacity: 0; transform: translateX(-50px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        
        @media (max-width: 768px) {
            .main-title { font-size: 2.5em; }
            .architecture-flow { flex-direction: column; }
            .flow-step { min-width: 100%; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="main-title">🧠 LSTM Next Word Prediction</h1>
            <p class="subtitle">🚀 Deep Learning | NLP | Streamlit App</p>
        </div>

        <div class="glass-card">
            <h2 class="section-title">🌟 Project Overview</h2>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.1em; text-align: center;">
                A powerful <strong>Next Word Prediction system</strong> built using <strong>LSTM networks</strong>. 
                Demonstrates how machines understand text sequences and predict the most probable next word.
            </p>
        </div>

        <div class="glass-card">
            <h2 class="section-title">✨ Key Features</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <span class="feature-icon">⚡</span>
                    <h3>Smart Prediction</h3>
                    <p>Context-aware next word prediction</p>
                </div>
                <div class="feature-card">
                    <span class="feature-icon">🖥️</span>
                    <h3>Real-Time UI</h3>
                    <p>Interactive Streamlit interface</p>
                </div>
                <div class="feature-card">
                    <span class="feature-icon">🧠</span>
                    <h3>LSTM Powered</h3>
                    <p>Deep learning sequence modeling</p>
                </div>
                <div class="feature-card">
                    <span class="feature-icon">📦</span>
                    <h3>Pre-trained</h3>
                    <p>Load and run instantly</p>
                </div>
            </div>
        </div>

        <div class="glass-card">
            <h2 class="section-title">🧪 Live Demo</h2>
            <div class="demo-input">
                Machine learning is
            </div>
            <div class="demo-output">
                ➤ Machine learning is <strong>amazing</strong>!
            </div>
        </div>

        <div class="glass-card">
            <h2 class="section-title">🖥️ System Architecture</h2>
            <div class="architecture-flow">
                <div class="flow-step">📝<br>User Input</div>
                <div class="flow-arrow">➝</div>
                <div class="flow-step">🔤<br>Tokenizer</div>
                <div class="flow-arrow">➝</div>
                <div class="flow-step">📏<br>Padding</div>
                <div class="flow-arrow">➝</div>
                <div class="flow-step">🧠<br>LSTM Model</div>
                <div class="flow-arrow">➝</div>
                <div class="flow-step">✨<br>Prediction</div>
            </div>
        </div>

        <div class="glass-card">
            <h2 class="section-title">📂 Project Structure</h2>
            <pre class="code-block">
lstm_model.h5         # Trained LSTM model
tokenizer.pkl         # Saved tokenizer  
max_len.pkl           # Max sequence length
app.py                # Streamlit UI
Word_prediction.ipynb # Training notebook
README.md             # Documentation
            </pre>
        </div>

        <div class="glass-card">
            <h2 class="section-title">▶️ Quick Start</h2>
            <div class="code-block">
pip install tensorflow streamlit numpy
            </div>
            <div class="code-block">
streamlit run app.py
            </div>
        </div>

        <div class="glass-card">
            <h2 class="section-title">📊 Model Specs</h2>
            <div class="table-container">
                <table>
                    <tr><th>Layer</th><th>Details</th></tr>
                    <tr><td>Embedding</td><td>Dimension: 100</td></tr>
                    <tr><td>LSTM</td><td>Units: 150</td></tr>
                    <tr><td>Output</td><td>Softmax + Adam</td></tr>
                    <tr><td>Loss</td><td>Sparse Categorical Crossentropy</td></tr>
                </table>
            </div>
        </div>

        <div class="glass-card">
            <h2 class="section-title">🚀 Future Enhancements</h2>
            <div class="future-features">
                <div class="future-item">🔥 Top-K Predictions</div>
                <div class="future-item">🤖 Transformer Models</div>
                <div class="future-item">🎤 Voice Input</div>
                <div class="future-item">☁️ Cloud Deploy</div>
                <div class="future-item">📱 Mobile UI</div>
            </div>
        </div>

        <div class="footer">
            <p><strong>👨‍💻 Author:</strong> Shashank Singh | <strong>⭐</strong> Star on GitHub!</p>
            <p>Inspired by Google Autocomplete & AI Writing Assistants</p>
            <p><em>🚀 Build. Learn. Improve. Repeat.</em></p>
        </div>
    </div>
</body>
</html>
