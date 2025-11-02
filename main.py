from decryptor import Decryptor
from reader import Reader
from PermutationDecryption import PermutationDecryption

def main():
    
    r = Reader()
    cifra = r.read()
    print("Cifra original:")
    print()
    print(cifra)
    print()
    pd = PermutationDecryption(r.read())
    pd.decipher()

    
if __name__ == "__main__":
    main()


