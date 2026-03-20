from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName
class PDFWriter :
    def __init__(self) :
        pass    
    # focntion qui remplie les champs de pdf avec le texte données
    def remplir_pdf(self, modele_pdf, sortie_pdf, donnees):
        pdf = PdfReader(modele_pdf)

        for page in pdf.pages:
            annotations = page.Annots
            if not annotations:
                continue

            for annot in annotations:
                if annot.Subtype == PdfName.Widget and annot.T: #récupérons le noms des champs 
                    key = annot.T[1:-1]  # enlever parenthèses


                    #si le champs existe dans les données on entre leur valeurs dans le champs
                    if key in donnees:
                        value = donnees[key]

                    # --- Gestion des cases à cocher ---
                        if value.lower() in ("oui", "yes", "on", "true", "1"):
                            annot.V = PdfName("Yes")
                            annot.AS = PdfName("Yes")
                        elif value.lower() in ("non", "no", "off", "false", "0"):
                            annot.V = PdfName("Off")
                            annot.AS = PdfName("Off")
                        else:
                        # --- Champ texte normal ---
                            annot.V = value
                            annot.AP = None  # forcer le rendu

        PdfWriter().write(sortie_pdf, pdf)
