import streamlit as st
import requests

st.set_page_config(page_title="CV Extractor", layout="centered")


if "cv_result" not in st.session_state:
    st.session_state["cv_result"] = None


page = st.sidebar.radio("Navigation", ["Upload", "Résultat"])


if page == "Upload":
    st.title("Uploader un CV")
    
    uploaded_file = st.file_uploader("Choisissez un fichier PDF ou DOCX", type=["pdf", "docx"])
    
    if uploaded_file:
        if st.button("Analyser le CV"):
            with st.spinner("Analyse en cours..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    response = requests.post("http://backend:8000/api/v1/upload-cv", files=files)
                    response.raise_for_status()
                    st.session_state["cv_result"] = response.json()
                    st.success("Analyse terminée ! Passez à la page 'Résultat' pour voir le CV.")
                except Exception as e:
                    st.error(f"Erreur lors de l'analyse : {e}")


elif page == "Résultat":
    st.title("Résultat de l'analyse du CV")
    
    if st.session_state["cv_result"]:
        data = st.session_state["cv_result"]
        
        first_name = st.text_input("Prénom", value=data.get("first_name", ""))
        last_name  = st.text_input("Nom", value=data.get("last_name", ""))
        email      = st.text_input("Email", value=data.get("email", ""))
        phone      = st.text_input("Téléphone", value=data.get("phone", ""))
        degree     = st.text_input("Diplôme", value=data.get("degree", ""))
        
       
        st.session_state["cv_result"].update({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "degree": degree
        })
        
       
        st.download_button(
            label="Télécharger en JSON",
            data=str(st.session_state["cv_result"]),
            file_name="cv_result.json"
        )
    else:
        st.info("Aucun CV analysé pour le moment. Veuillez d'abord uploader un fichier sur la page Upload.")
