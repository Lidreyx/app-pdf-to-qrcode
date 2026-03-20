# ui_app.py

import tkinter as tk
from tkinter import ttk
from pdfreader import PDFReader
from pdfwriter import remplir_pdf


class ApplicationUI(tk.Tk):
    """
    Interface graphique principale de l'application PDF.
    """

    def __init__(self):
        super().__init__()

        self.title("Application PDF")
        self.geometry("400x300")

        # Instances des classes
        self.reader = PDFReader()
        self.filler = remplir_pdf()

        # Boutons
        ttk.Button(self, text="Inspecter un PDF", command=self.reader.inspecter).pack(pady=10)
        ttk.Button(self, text="Remplir un PDF", command=self.remplir).pack(pady=10)

    def remplir(self):
        """Exemple de remplissage PDF."""
        donnees = {
            "NOM": "Dupont",
            "PRENOM": "Jean",
            "GRADE": "Caporal",
        }

        self.filler.remplir("data/modele.pdf", "data/sortie.pdf", donnees)
