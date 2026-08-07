from PyPDF2 import PdfReader
from docx import Document


class FileHandler:

    @staticmethod
    def extract_text(file):

        if not file:
            return ""

        filename = file.filename.lower()

        # ==========================================
        # TXT
        # ==========================================

        if filename.endswith(".txt"):

            return file.read().decode("utf-8", errors="ignore")

        # ==========================================
        # PDF
        # ==========================================

        elif filename.endswith(".pdf"):

            reader = PdfReader(file)

            text = ""

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

            return text

        # ==========================================
        # DOCX
        # ==========================================

        elif filename.endswith(".docx"):

            document = Document(file)

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

            return text

        raise ValueError(
            "Unsupported file format."
        )