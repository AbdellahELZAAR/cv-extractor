CV Extractor 🎯
Description

CV Extractor est une application entièrement développée en Python permettant d’extraire automatiquement les informations clés d’un CV : Prénom, Nom, Email, Téléphone et Diplôme.


Le projet se compose de :

un backend FastAPI pour le traitement et l’extraction des données,

un frontend Streamlit pour l’interface utilisateur, 

et peut être lancé localement ou via Docker.

📑 Sommaire

Structure du projet

Partie A – Backend (FastAPI)

Partie B – Pipeline d’extraction

Partie C – Frontend (Streamlit)

Partie D – Docker

Installation locale

Lancement Docker

Tests unitaires

Exemples d’API


###############################################################################
⚡ Backend (FastAPI)
Stack utilisée : 
FastAPI
Uvicorn
PyPDF2 / PDFPlumber
python-docx
regex (re)
Pydantic
Endpoint principal :
POST /api/v1/upload-cv
Entrée : fichier PDF ou DOCX
Sortie : JSON contenant les informations extraites

Exemple de réponse :

{
  "first_name": "Alain",
  "last_name": "Bernard",
  "email": "alain.bernard@gmail.com",
  "phone": "+33612345678",
  "degree": "Master Informatique"
}
###############################################################################à
⚡ Frontend (Streamlit)
Pages principales :
Upload/
Upload de fichiers PDF / DOCX
Bouton “Analyser le CV”
Appel POST vers le backend
Loader via st.spinner
Résultat/
Affichage des champs modifiables : Prénom, Nom, Email, Téléphone, Diplôme
Bouton “Télécharger en JSON”
##############################################################################à
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
# Lancer le backend
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
# Lancer le frontend
streamlit run frontend/app.py
#############################################################################
🐳 Lancement via Docker
docker compose -f docker/docker-compose.yml up --build
Backend (FastAPI) : http://localhost:8000
Frontend (Streamlit) : http://localhost:8501
#############################################################################
🧪 Tests unitaires
cd cv-extractor
pytest
Les tests sont réalisés avec pytest et couvrent l’extraction de :
Email
Téléphone
Diplôme
Prénom / Nom
############################################################################
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
