import tkinter as tk
from tkinter.filedialog import askopenfilename
from pdfrw import PdfReader, PdfName

def inspecter_pdf():
    root = tk.Tk()
    root.withdraw()

    fichier = askopenfilename(
        title="Choisir un PDF à inspecter",
        filetypes=[("PDF", "*.pdf")]
    )

    if not fichier:
        print("Aucun fichier sélectionné.")
        return

    print("\n--- Inspection du PDF ---")
    print("Fichier :", fichier)

    pdf = PdfReader(fichier)

    for page_num, page in enumerate(pdf.pages, start=1):
        annots = getattr(page, "Annots", None)
        if not annots:
            continue

        print(f"\nPage {page_num} :")

        for annot in annots:
            if not annot.T:
                continue

            nom = annot.T[1:-1]
            print(f"\nChamp trouvé : {nom}")
            print("  Type :", annot.Subtype)
            print("  Valeur actuelle :", annot.V)

            # Vérifier AP
            if hasattr(annot, "AP") and annot.AP:
                apparences = list(annot.AP.keys())
                print("  Apparences possibles :", apparences)

                if "/Yes" in apparences or "/On" in apparences:
                    print("  → C'est une CASE À COCHER")
                elif len(apparences) > 1:
                    print("  → Probablement un BOUTON RADIO")
            else:
                print("  Pas d'apparence (champ texte ou XFA)")

    print("\n--- Fin de l’inspection ---\n")


inspecter_pdf()
