# Appli pdf 

### cette application sert à transformer les champs entrés dans un qrcode et le chiffré. Ensuite nous pouvons entrer les valeurs chiffrées du qr code et les entrer dans le template du pdf

l'objectif est de pouvoir transférer les infos d'un pdf à un autre avec pour seule connexion une liseuse de qrcode.


fonctionnalité : 

#### pdfwriter.py
classe PDFWriter:  
- remplir_pdf() fonction qui demande un pdf blanc à remplir à partir des données/texte que l'utilisateur fournit

#### cryptage.py
classe Cryptage:
- chiffrage = encode les données

#### case.py
- case = sert à identifier le nom des champs (si besoin de les modifiers)

#### pdfreader.py
PDFReader :
- extraire_infos_pdf = récupère le texte des champs  ( à modifier si besoin car si le nom est pas bon ça n'y touche pas)

main.py = interface tkinter avec la fonction pour créer un qrcode


Python 3.12.7

module important :

tkinter #interface
tkinter.filedialog pour  = askopenfilename, asksaveasfilename #ouvrir les fichiers et save
qrcode #pour les qrcode (créer et lire)
pdfrw import PdfReader, PdfWriter, PdfDict, PdfName #pdfrw pour écrire dans un pdf et le lire afin de récupérer les champs
from PyPDF2 import PdfReader # lire le pdf et prendre les champs 
from cryptography.fernet import Fernet # nécessaire pour avoir la clé et chiffrer les données

installation :
pip install pdfrw
pip install PyPDF2
pip install qrcode
pip install tkinter
pip install fernet ou pip install cryptography


limitation : 
les cases cochées ne sont pas scanable à cause du format pdf "XFA" donc il faut les séléctionner nous même

