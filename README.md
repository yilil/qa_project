# RAG Q&A Demo

## How to use this codebase

### Step 1 - Environment Setup
`conda env create -f environment.yml`

`conda activate rag_qna`

### Step 2 - Data Initialisation
`python3 init.py`

### Step 3 - Start Server

`python3 manage.py runserver`

## Note
Other things you need to do include:

(1) Initial migration of the database

(2) Save Django Secrete Key as an environment variable. You could generate a new key by running:
- `from django.core.management.utils import get_random_secret_key`
- `print(get_random_secret_key())`

(3) Save Google API Key as an environment variable