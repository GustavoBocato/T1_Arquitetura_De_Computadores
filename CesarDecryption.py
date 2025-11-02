import string

class CesarDecryption:

    alphabet = string.ascii_uppercase

    def __init__(self, cipher):

        self.cipher = cipher

    def decipher(self):

        for i in range(0, len(self.alphabet)):

            message = self.cipher

            for j in range(0, len(message)):

                if(message[j] in self.alphabet):

                    message = message[:j] + chr((((ord(message[j]) - 65) + i)%len(self.alphabet)) + 65) + message[j+1:]

            print(message)
            print()
            print("-----------------------------------------------------------------")
            print()

