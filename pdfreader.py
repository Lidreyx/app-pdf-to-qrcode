from PyPDF2 import PdfReader
class PDFReader :

"""

    le but de cette fonction est de lire un pdf afin de récupérer les informations des champs d'entrée 
    associe chaque clé (noms champs) à une valeure ( contenu des champs) afin de conserver les données
    
"""

    
    def __init__(self) :
        pass
    # fonction pour récuprer le contenu des champs d'entrés
    def extraire_infos_pdf(self, fichier_pdf)
        reader = PdfReader(fichier_pdf)
        fields = reader.get_fields()
        valeurs = {}
        #si aucun champs trouvé return
        if not fields:
            print("Aucun champ trouvé dans le PDF.")
            return valeurs
        #nom des champs d'entré utiliser le code case pour trouver le nom des champs de votre pdf et remplacez les 
        champs_texte = [
            "NOM", "PRENOM", "ORGANISME", "GRADE",
            "LIEUNAISS", "DATNAISS", "H1", "MIN1",
            "NON1", "IMMAT", "OUI1", "NON1", "VEHICULE", "GRADE2", "NOM2", "PRENOM2", "SERVICE", "TEL", "PIECE",
        ]
        #attribut chaque nom de champs à un texte
        for cle in champs_texte:
            if cle in fields:
                valeurs[cle] = fields[cle].get("/V", "").strip()


        #prise en charge des cases à cocher oui ou non
        if "OUI1" in fields and fields["OUI1"].get("/V", "") not in (None, "/OFF"):
            valeurs["pieton"] = "oui"
        elif "NON1" in fields and fields["NON1"].get("/V", "") not in (None, "/OFF"):
            valeurs["pieton"] = "non"

        if "OUI2" in fields and fields["OUI2"].get("/V", "") not in (None, "/OFF"):
            valeurs["vehicule"] = "oui"
        elif "NON2" in fields and fields["NON2"].get("/V", "") not in (None, "/OFF"):
            valeurs["vehicule"] = "non"

        return valeurs  
