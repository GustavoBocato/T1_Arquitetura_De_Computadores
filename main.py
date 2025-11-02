from decryptor import Decryptor
from reader import Reader
from PermutationDecryption import PermutationDecryption

def main():
    
    r = Reader()
    pd = PermutationDecryption(r.read())
    pd.decipher()

    
if __name__ == "__main__":
    main()


