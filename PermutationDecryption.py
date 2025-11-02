import string
import random
from ngram_score import ngram_score
from collections import Counter

class PermutationDecryption:

    alphabet = string.ascii_uppercase
    ngram_score = ngram_score()

    def __init__(self, message):

        self.message = message
        self.current_permutation = self.generate_first_permutation()
        self.best_permutation = self.current_permutation
        self.best_score = self.ngram_score.score(self.permutate_message(self.best_permutation))

    def permutate_message(self, permutation):

        table = str.maketrans(self.alphabet, permutation)
        return self.message.translate(table)
    
    def generate_all_mutations(self, permutation):

        all_mutations = []
        original_permutation = permutation

        for i in range(0, 26):

            for j in range(i + 1, 26):

                c = permutation[i]
                permutation = permutation[:i] + permutation[j] + permutation[i+1:]
                permutation = permutation[:j] + c + permutation[j+1:]

                all_mutations.append(permutation)
                permutation = original_permutation

        return all_mutations

    def improve_score(self):

        improved = False
        allMutations = self.generate_all_mutations(self.current_permutation)

        for mutation in allMutations:

            candidate_score = self.ngram_score.score(self.permutate_message(mutation))

            if candidate_score > self.best_score:

                improved = True
                self.current_permutation = mutation
                self.best_permutation = mutation
                self.best_score = candidate_score

        return improved
        
    def decipher(self):

        count = 0

        while(count < 1000):

            if(self.improve_score()):

                count += 1

                print()
                print("------")
                print(self.permutate_message(self.best_permutation))
                print(self.best_score)
                print("Permutation: " + self.best_permutation)
                print("------")
                print()


            else:

                char_list = list(self.alphabet)
                random.shuffle(char_list)
                self.current_permutation = "".join(char_list)

    def generate_first_permutation(self) -> str:
        """
        Generates an initial alphabet permutation based on frequency analysis.
        The most frequent letter in the ciphertext is mapped to 'E', the second to 'T', etc.
        
        Returns a 26-letter string permutation such that:
        'A' maps to permutation[0], 'B' to permutation[1], ...
        """
        ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Count ciphertext frequencies
        cipher_text = self.message
        freqs = Counter([c for c in cipher_text if c.isalpha()])

        # Sort cipher letters by frequency (descending)
        sorted_cipher = sorted(ALPHABET, key=lambda c: freqs.get(c, 0), reverse=True)

        # Create mapping: cipher's most frequent -> 'E', etc.
        mapping = {}
        for i, c in enumerate(sorted_cipher):
            if i < len(ENGLISH_FREQ_ORDER):
                mapping[c] = ENGLISH_FREQ_ORDER[i]
            else:
                mapping[c] = c  # fallback, should never happen

        # Build permutation string: position of letter A = mapping['A'], etc.
        permutation = ''.join(mapping[c] for c in ALPHABET)
        return permutation



        




        

    

        
    
        