import os
import sys
import subprocess
import threading
import time
import webbrowser

# Check for a custom environment flag to know if Streamlit was already launched.
if os.environ.get("STREAMLIT_AUTO_BROWSER") is None:
    # Set the flag and re-launch using Streamlit.
    new_env = os.environ.copy()
    new_env["STREAMLIT_AUTO_BROWSER"] = "true"
    # Launch the Streamlit server (this process will run app.py under Streamlit)
    subprocess.Popen(["streamlit", "run", __file__], env=new_env)
    sys.exit()

def open_browser_once():
    """Wait a bit for the server to start, then open the browser once."""
    time.sleep(2)  # Adjust delay if needed
    webbrowser.open("http://localhost:8501")

# Use a simple flag file in memory to prevent multiple browser opens.
# (Note: With Streamlit's auto-reloading, this may still trigger on reloads.)
if not os.environ.get("BROWSER_ALREADY_OPENED"):
    os.environ["BROWSER_ALREADY_OPENED"] = "true"
    threading.Thread(target=open_browser_once, daemon=True).start()

# --- Streamlit App Code ---
import streamlit as st

st.title("Welcome to My Streamlit App")
st.header("Hello, Streamlit!")
st.write("This app automatically opens the front end in your browser upon running.")
