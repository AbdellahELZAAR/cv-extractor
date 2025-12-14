def extract_name(text: str):
    lines = text.strip().split("\n")

    for line in lines:
        clean = line.strip()
        if len(clean.split()) == 2 and clean.isalpha() is False:
            parts = clean.split()
            if parts[0].istitle() and parts[1].istitle():
                return parts[0], parts[1]

    return None, None
