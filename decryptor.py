from reader import Reader
from PermutationDecryption import PermutationDecryption

class Decryptor:

    def __init__(self):

        reader = Reader()
        self.cipher = reader.read()
        
    def decipher(self):

        pd = PermutationDecryption(self.cipher)
        pd.decipher()




    

    