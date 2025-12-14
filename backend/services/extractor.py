import re



def extract_name_from_header(text: str):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    if not lines:
        return None, None

    first_line = lines[0]
    words = first_line.split()

    if 2 <= len(words) <= 3 and all(w.isalpha() for w in words):
        return words[0].title(), words[-1].title()

    return None, None


def extract_name_from_email(email: str):
    if not email:
        return None, None

    local = email.split("@")[0]
    parts = re.split(r"[._\-]", local)

    if len(parts) >= 2:
        return parts[0].title(), parts[1].title()

    return None, None


def extract_name_from_labels(text: str):
    first = re.search(r'Prénom\s*[:\-]?\s*([A-Z][a-z]+)', text, re.IGNORECASE)
    last  = re.search(r'Nom\s*[:\-]?\s*([A-Z][a-z]+)', text, re.IGNORECASE)

    return (
        first.group(1).title() if first else None,
        last.group(1).title() if last else None
    )


def extract_name_from_caps(text: str):
    for line in text.splitlines():
        if line.isupper():
            words = line.split()
            if 2 <= len(words) <= 3:
                return words[0].title(), words[-1].title()
    return None, None



def extract_info(text: str) -> dict:
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    phone_match = re.search(r'(\+?\d{10,15})', text)
    degree_match = re.search(
        r'(Master|Licence|Bachelor|Doctorat|PhD)[^\n]*',
        text,
        re.IGNORECASE
    )

    email = email_match.group(0) if email_match else None
    phone = phone_match.group(0) if phone_match else None
    degree = degree_match.group(0) if degree_match else None

   
    first_name, last_name = extract_name_from_header(text)

    if not first_name:
        fn, ln = extract_name_from_email(email)
        first_name = fn
        last_name = ln

    if not first_name:
        fn, ln = extract_name_from_labels(text)
        first_name = fn
        last_name = ln

    if not first_name:
        fn, ln = extract_name_from_caps(text)
        first_name = fn
        last_name = ln

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "degree": degree,
    }
