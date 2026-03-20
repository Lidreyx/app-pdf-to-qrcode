# crypto.py

from cryptography.fernet import Fernet

#clé AES b"irV6l0r7WT7JAdS1dxNUCUiOQAie34HAyCIcIUWYcJU="

class Cryptage:
    CLE_FERNET = b"irV6l0r7WT7JAdS1dxNUCUiOQAie34HAyCIcIUWYcJU="

    def __init__(self):
        self.cipher = Fernet(self.CLE_FERNET)

    def chiffrer(self, texte: str) -> str:
        return self.cipher.encrypt(texte.encode()).decode()

    def dechiffrer(self, texte_chiffre: str) -> str:
        return self.cipher.decrypt(texte_chiffre.encode()).decode()
