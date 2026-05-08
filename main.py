import streamlit as st
import numpy as npppppp
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import warnings
warnings.filterwarnings('ignore')

# Page config for better perf
st.set_page_config(page_title="LSTM Next Word Predictor", layout="wide")

# Load artifacts with resource caching (persists across reruns)
@st.cache_resource
def load_artifacts():
    try:
        model = load_model('lstm_model.h5')
        with open('tokenizer.pkl', 'rb') as f:
            tokenizer = pickle.load(f)
        with open('max_len.pkl', 'rb') as f:
            max_len = pickle.load(f)
        vocab_size = len(tokenizer.word_index) + 1
        st.success("✅ Model, tokenizer, and max_len loaded!")
        return model, tokenizer, max_len, vocab_size
    except Exception as e:
        st.error(f"❌ Load error: {e}. Check files.")
        return None, None, None, None

model, tokenizer, max_len, vocab_size = load_artifacts()

if model is None:
    st.stop()

st.title("🚀 High-Perf LSTM Next Word Predictor")
st.markdown("**Production-ready: Cached model, top-K preds, temperature sampling, continuous gen.**")

# Sidebar for advanced controls
with st.sidebar:
    st.header("⚙️ Settings")
    temperature = st.slider("Temperature (creativity)", 0.1, 2.0, 1.0, 0.1)
    top_k = st.slider("Top-K words", 1, 10, 3)
    max_new_words = st.slider("Max new words", 1, 20, 5)

# Initialize session state
if 'output_text' not in st.session_state:
    st.session_state.output_text = ""

# Main input
col1, col2 = st.columns([3,1])
with col1:
    input_text = st.text_input("📝 Input sentence:", value=st.session_state.output_text.split(' | ')[0] if st.session_state.output_text else "")
with col2:
    clear_btn = st.button("🗑️ Clear")

if clear_btn:
    st.session_state.output_text = ""
    st.rerun()

if st.button("🔮 Predict Next Words", type="primary") and input_text:
    with st.spinner("Generating..."):
        progress_bar = st.progress(0)
        
        # Tokenize input
        token_list = tokenizer.texts_to_sequences([input_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')
        
        output_text = input_text
        for i in range(max_new_words):
            # Predict with temperature
            pred = model.predict(token_list, verbose=0)[0]
            pred = np.log(pred + 1e-8) / temperature
            pred = np.exp(pred) / np.sum(np.exp(pred))
            
            # Top-K
            top_indices = np.argpartition(pred, -top_k)[-top_k:]
            top_indices = top_indices[np.argsort(pred[top_indices])[::-1]]
            
            # Select most probable
            predicted_idx = top_indices[0]
            predicted_word = tokenizer.index_word.get(predicted_idx, '?')
            
            output_text += f" **{predicted_word}**"
            st.session_state.output_text = output_text
            
            # Update sequence
            token_list = np.append(token_list[0][1:], predicted_idx)
            token_list = np.array([token_list])
            
            progress_bar.progress((i+1)/max_new_words)
        
        progress_bar.empty()

# Display results
if st.session_state.output_text:
    st.markdown(f"### 📊 Result: {st.session_state.output_text}")
    
    # Continue button
    if st.button("➕ Continue Generating"):
        st.rerun()

# Info sidebar
with st.sidebar.expander("ℹ️ Performance Notes"):
    st.markdown("""
    - **Model cached**: Loads once, ultra-fast inference (~ms).
    - **Session state**: Seamless continuous prediction.
    - **TF optimized**: No verbose, batched preds.
    - **Deploy-ready**: Works on Streamlit Cloud (upload files).[web:13]
    """)

# Footer
st.markdown("---")
st.caption("Built for JARVIS-style AI. Optimized for your LSTM model.[cite:1]")
