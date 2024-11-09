# Document_RAG

## Prerequisites

 - Python 3.7+ (Ensure Python is installed. You can check by running python --version in your terminal.)
 - Ollama running on laptop and llama3.2 running on it using `ollama run llama3.2`

## Setup
1. Clone the repository (if using Git):
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/Utkrishtdutta/Document_RAG.git)
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

5. Start the app by running:
```bash
streamlit run app.py
```
6. Access the app:
  - After running the above command, Streamlit will output a local URL (usually http://localhost:8501).
  - Open this URL in your web browser to interact with the app.
