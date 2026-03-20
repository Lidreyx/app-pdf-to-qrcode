from PyPDF2 import PdfReader
class PDFReader :
    
    def __init__(self) :
        pass

    def extraire_infos_pdf(self, fichier_pdf):
        reader = PdfReader(fichier_pdf)
        fields = reader.get_fields()
        valeurs = {}

        if not fields:
            print("Aucun champ trouvé dans le PDF.")
            return valeurs
    
        champs_texte = [
            "NOM", "PRENOM", "ORGANISME", "GRADE",
            "LIEUNAISS", "DATNAISS", "H1", "MIN1",
            "NON1", "IMMAT", "OUI1", "NON1", "VEHICULE", "GRADE2", "NOM2", "PRENOM2", "SERVICE", "TEL", "PIECE",
        ]

        for cle in champs_texte:
            if cle in fields:
                valeurs[cle] = fields[cle].get("/V", "").strip()


    
        if "OUI1" in fields and fields["OUI1"].get("/V", "") not in (None, "/OFF"):
            valeurs["pieton"] = "oui"
        elif "NON1" in fields and fields["NON1"].get("/V", "") not in (None, "/OFF"):
            valeurs["pieton"] = "non"

        if "OUI2" in fields and fields["OUI2"].get("/V", "") not in (None, "/OFF"):
            valeurs["vehicule"] = "oui"
        elif "NON2" in fields and fields["NON2"].get("/V", "") not in (None, "/OFF"):
            valeurs["vehicule"] = "non"

        return valeurs  