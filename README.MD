## 🎯 Description

**CV Extractor** est une application full Python permettant d’extraire automatiquement les informations clés d’un CV :  
**Prénom, Nom, Email, Téléphone et Diplôme**.  

Le projet se compose de :  
- un **backend FastAPI** pour le traitement et l’extraction des données,  
- un **frontend Streamlit** pour l’interface utilisateur,  
- et peut être lancé **localement ou via Docker**.

###########################################################à

## 📑 Sommaire

- [Structure du projet](#-structure-du-projet)
- [Backend (FastAPI)](#-partie-a--backend-fastapi)
- [Frontend (Streamlit)](#-partie-c--frontend-streamlit)
- [Installation locale](#-💻-installation-locale)
- [Lancement Docker](#-🐳-lancement-via-docker)
- [Tests unitaires](#-🧪-tests-unitaires)
- [Exemples d’API](#-📝-exemples-dapi)


##########################################################
## 📂 Structure du projet

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


###############################################
## ⚡ Partie A – Backend (FastAPI)

### Stack
- FastAPI
- Uvicorn
- PyPDF2 / PDFPlumber
- python-docx
- regex (`re`)
- Pydantic

### Endpoint principal

**POST /api/v1/upload-cv**  

**Entrée** : fichier PDF ou DOCX  
**Sortie JSON** :

```json
{
  "first_name": "Alain",
  "last_name": "Bernard",
  "email": "alain.bernard@gmail.com",
  "phone": "+33612345678",
  "degree": "Master Informatique"
}

######################################################

⚡ Partie C – Frontend (Streamlit)
PAGES :
PAGE 1 : Upload
Upload PDF / DOCX
Bouton “Analyser le CV”
Appel POST vers le backend
Loader via st.spinner

PAGE 2 : Résultat
Affichage des champs modifiables :
Prénom
Nom
Email
Téléphone
Diplôme
Bouton “Télécharger en JSON”


#####################################################
💻 Installation locale
Cloner le projet :
git clone <repo_url>
cd cv-extractor
Créer un environnement virtuel :
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

********************************************
Installer les dépendances :
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

********************************************
Lancer le backend :
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

*************************************************
Lancer le frontend :
streamlit run frontend/app.py

######################################################
🐳 Lancement via Docker
Construire et lancer les containers :
docker compose -f docker/docker-compose.yml up --build

Accéder aux services :
Backend (FastAPI) : http://localhost:8000
Frontend (Streamlit) : http://localhost:8501
#######################################################
🧪 Tests unitaires
Les tests sont réalisés avec pytest et vérifient notamment :

Extraction email
Extraction téléphone
Extraction diplôme
Extraction nom / prénom

Depuis la racine cv-extractor/ ;Executer la commade :
pytest

###########################################################
📝 Exemples d’API
Upload d’un CV :

curl -X POST "http://localhost:8000/api/v1/upload-cv" \
  -F "file=@mon_cv.pdf"
Réponse :

json
Copier le code
{
  "first_name": "Alain",
  "last_name": "Bernard",
  "email": "alain.bernard@gmail.com",
  "phone": "+33612345678",
  "degree": "Master Informatique"
}