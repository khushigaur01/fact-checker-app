import fitz
import re


def extract_text_from_pdf(pdf_file):

    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def extract_claims(text):

    lines = text.split("\n")

    claims = []

    patterns = [
        r"\d+%",
        r"\$\d+",
        r"\d{4}",
        r"million",
        r"billion",
        r"crore",
        r"lakh"
    ]

    for line in lines:

        for pattern in patterns:

            if re.search(pattern, line, re.IGNORECASE):

                clean_line = line.strip()

                if len(clean_line) > 15:
                    claims.append(clean_line)

                break

    unique_claims = list(set(claims))

    return unique_claims