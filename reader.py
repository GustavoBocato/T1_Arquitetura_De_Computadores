class Reader:

    def __init__(self):
    
        self.cipher = ""

    def read(self):

        with open("cifra.txt") as f:

           self.cipher = "".join([chr(int(b, 2)) for b in f.read().split()])

        return self.cipher

        
        

        

        

        