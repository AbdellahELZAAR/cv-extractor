from backend.services.extractor import extract_info


def test_extract_email():
    text = "Contact: abdellah.elzaar@gmail.com"
    result = extract_info(text)
    assert result["email"] == "abdellah.elzaar@gmail.com"


def test_extract_phone():
    text = "Téléphone: +33650969518"
    result = extract_info(text)
    assert result["phone"] == "+33650969518"


def test_extract_degree():
    text = "Diplôme: Doctorat en Intelligence Artificielle"
    result = extract_info(text)
    assert "Doctorat" in result["degree"]


def test_extract_name_from_email():
    text = "Email: abdellah.elzaar@gmail.com"
    result = extract_info(text)
    assert result["first_name"] == "Abdellah"
    assert result["last_name"] == "Elzaar"
