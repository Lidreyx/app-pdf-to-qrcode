import tkinter as tk #nécessaire pour créer l'interface graphique, à installer.
from tkinter.filedialog import askopenfilename, asksaveasfilename #nécessaire pour ouvrir les fenêtres de sélection de fichiers, à installer.
import qrcode #nécessaire pour générer les QR code, à installer.
import csv #nécessaire pour transformer en csv, à installer.
from tkinter import filedialog, messagebox


# import des script nécessaire
from pdfreader import PDFReader #appel de la classe PDFReadr
from cryptage import Cryptage #appel de la classe Cryptage pour chiffrer et déchiffrer les données
from pdfwriter import PDFWriter #appel de la classe PDFWriter pour remplir les pdf à partir des données extraites du texte (ou du texte déchiffré)
crypto = Cryptage() #initialisation de la classe Cryptage pour pouvoir utiliser ses fonctions de chiffrement et déchiffrement
reader = PDFReader() #initialisation de la classe PDFReader pour pouvoir utiliser ses fonctions d'extraction de données à partir des pdf
writer = PDFWriter()#initialisation de la classe PDFWriter pour pouvoir utiliser ses fonctions de remplissage de pdf à partir des données extraites du texte (ou du texte déchiffré)


# Fonction pour générer un QR code à partir d'un PDF
def generer_qr():
    #trouver le fichier pdf (ne fonctionne que pour les fiches visiteurs sinon modifier les champs dans pdfreader.py)
    fichier_pdf = askopenfilename(
        title="Choisir un PDF",
        filetypes=[("PDF", "*.pdf")]
    )
    if not fichier_pdf: #failsafe si aucun fichier
        return

    #recherches des champs dans le pdf et extraction de leurs valeurs

    valeurs = reader.extraire_infos_pdf(fichier_pdf) #appel de la fonction d'extraction de données du pdf dans pdfreader.py
    if not valeurs: #failsage si aucune donnée n'est trouvée dans le pdf
        print("Aucune donnée trouvée.")
        return

    contenu = ";".join(f"{k}={v}" for k, v in valeurs.items()) # formatage des données extraite en texte simple
    contenu_chiffre = crypto.chiffrer(contenu) #appel de la fonction de chiffrement pour chiffrer le texte

    fichier_qr = asksaveasfilename( #enregistrement du QR code généré 
        title="Enregistrer QR code",
        defaultextension=".png",
        filetypes=[("PNG", "*.png")]
    )
    if not fichier_qr: #si l'utilisateur annule la sauvegarde du QR code, on arrête la fonction
        return

    # on met le contenu chiffré dans le QR code et on l'enregistre
    img = qrcode.make(contenu_chiffre) #génération du QR code à partir du texte chiffré
    img.save(fichier_qr)

    print("QR code enregistré :", fichier_qr)


    #fonction pour remplir un pdf à partir d'un texte (ou texte déchiffré) contenant les données à insérer dans le pdf
def remplir_depuis_texte():
    texte = zone_texte.get("1.0", "end").strip() 

    # Étape 1 : tenter de déchiffrer
    try:
        texte = crypto.dechiffrer(texte)
        print("Texte déchiffré :", texte)
    except:
        print("Le texte n'est pas chiffré ou la clé est incorrecte")

    # Étape 2 : convertir en dictionnaire
    donnees = dict(
        p.split("=", 1)
        for p in texte.split(";")
        if "=" in p and p.strip() != ""
    )
     # Affichage des données extraites pour vérification
    print("DONNEES =", donnees)
    donnees = {k: str(v) for k, v in donnees.items() if v not in ("", None)}
    print("DONNEES filtrées = ", donnees)

    modele = askopenfilename(title="Choisir le PDF modèle")
    if not modele:
        return

    # Choix du fichier de sortie
    sortie = asksaveasfilename(
        title="Enregistrer le PDF rempli",
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")]
    )
    if not sortie:
        return

    writer.remplir_pdf(modele, sortie, donnees)



def exporter_csv(): # transformer le texte du qrcode en csv 
    # Récupère le texte depuis ta zone de texte
    contenu = zone_texte.get("1.0", "end").strip()
    try:
        #appel de la fonction de déchiffrement dans cryptage.py
        contenu = crypto.dechiffrer(contenu) # on déchiffre le texte avant tout (nécéssaire pour récupérer les données)
        print("Texte déchiffré :", contenu) # on s'assure d'avoir le bon contenue et la bonne clé 
    except:
        print("Le texte n'est pas chiffré ou la clé est incorrecte") 

    if not contenu:
        messagebox.showwarning("Attention", "Le texte est vide.")
        return

    # Choix du fichier CSV à créer
    fichier = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("Fichier CSV", "*.csv")]
    )

    if not fichier:
        return

    # Conversion du texte en CSV
    lignes = contenu.split("\n")

    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        for ligne in lignes:
            writer.writerow(ligne.split(";"))

    messagebox.showinfo("Succès", "Le fichier CSV a été créé.")


#configuration de l'interface graphique avec tkinter
root = tk.Tk()
root.title("Gestion PDF & QR")

tk.Button(root, text="Générer QR code chiffré", command=generer_qr).pack(pady=10)

zone_texte = tk.Text(root, height=10, width=60)
zone_texte.pack(pady=10)
tk.Button(root, text="Remplir PDF depuis texte", command=remplir_depuis_texte).pack(pady=10)

bouton_csv = tk.Button(root, text="Exporter en CSV", command=exporter_csv)
bouton_csv.pack(pady=5)


root.mainloop()
