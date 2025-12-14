CV Extractor
🎯 Description

CV Extractor est une application full Python permettant d’extraire automatiquement les informations clés d’un CV : Prénom, Nom, Email, Téléphone et Diplôme. Le projet se compose de : un backend FastAPI pour le traitement et l’extraction des données, un frontend Streamlit pour l’interface utilisateur, et peut être lancé localement ou via Docker.

## 📑 Sommaire
- [Structure du projet](#-structure-du-projet)  
- [Partie A – Backend (FastAPI)](#-partie-a--backend-fastapi)  
- [Partie B – Pipeline d’extraction](#-partie-b--pipeline-dextraction)  
- [Partie C – Frontend (Streamlit)](#-partie-c--frontend-streamlit)  
- [Partie D – Docker](#-partie-d--docker)  
- [Installation locale](#-installation-locale)  
- [Lancement Docker](#-lancement-via-docker)  
- [Tests unitaires](#-tests-unitaires)  
- [Exemples d’API](#-exemples-dapi)  

📂 Structure du projet
cv-extractor/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── pdf_parser.py
│   │   ├── docx_parser.py
│   │   └── extractor.py
│   ├── models/
│   │   └── cv_result.py
│   ├── utils/
│   │   ├── regex_patterns.py
│   │   └── name_extractor.py
│   └── tests/
│       └── test_extractor.py
├── frontend/
│   ├── app.py
│   └── requirements.txt
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
└── README.md

⚡Backend (FastAPI)
Stack utilisée
FastAPI
Uvicorn
PyPDF2 / PDFPlumber
python-docx
regex (re)
Pydantic
Endpoint principal
POST /api/v1/upload-cv
Entrée : fichier PDF ou DOCX
Sortie : JSON contenant les informations extraites

{
  "first_name": "Alain",
  "last_name": "Bernard",
  "email": "alain.bernard@gmail.com",
  "phone": "+33612345678",
  "degree": "Master Informatique"
}

⚡Frontend (Streamlit)
Pages principales

Page 1 – Upload : Upload de fichiers PDF / DOCX, bouton “Analyser le CV”, appel POST vers le backend, loader via st.spinner
Page 2 – Résultat : Affichage des champs modifiables : Prénom, Nom, Email, Téléphone, Diplôme, bouton “Télécharger en JSON”
#########################################################################################################################à
💻 Installation locale
git clone <repo_url>
cd cv-extractor
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
streamlit run frontend/app.py
############################################################################################################
🐳 Lancement via Docker
docker compose -f docker/docker-compose.yml up --build


Accéder aux services : Backend (FastAPI) : http://localhost:8000
, Frontend (Streamlit) : http://localhost:8501
##############################################################################################################
🧪 Tests unitaires
lancer la commande dans le dossier /cv_extracor
pytest


Les tests sont réalisés avec pytest et couvrent : extraction email, téléphone, diplôme et nom/prénom.
###############################################################################################################
📝 Exemples d’API
curl -X POST "http://localhost:8000/api/v1/upload-cv" -F "file=@mon_cv.pdf"


Réponse JSON :

{
  "first_name": "Alain",
  "last_name": "Bernard",
  "email": "alain.bernard@gmail.com",
  "phone": "+33612345678",
  "degree": "Master Informatique"
}
