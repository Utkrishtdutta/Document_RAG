# Document_RAG

## Prerequisites

 - Python 3.7+ (Ensure Python is installed. You can check by running python --version in your terminal.)

## Setup
1. Clone the repository (if using Git):
```bash
git clone https://github.com/Utkrishtdutta/Document_RAG.git
cd Document_RAG
```
2. Create a virtual environment (recommended):
```bash
python -m venv .venv
```
3. Activate the virtual environment:
  - On Windows:
    ```bash
    .venv\Scripts\activate
    ```
4. Install dependencies:
 ```bash
 pip install -r requirements.txt
 ```
5. Before running download and configure Ollama (https://ollama.com/).
   - ON CMD terminal type `ollama pull llama3.2` to download llama 3.2 locally.
   - To run llama 3.2 type `ollama run llama3.2`.

6. Start the app by running:
```bash
streamlit run app.py
```
7. Access the app:
  - After running the above command, Streamlit will output a local URL (usually http://localhost:8501).
  - Open this URL in your web browser to interact with the app.
