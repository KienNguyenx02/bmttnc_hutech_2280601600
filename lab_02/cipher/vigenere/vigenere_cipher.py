class VigenereCipher:
    def __init__(self, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.alphabet = alphabet
        self.n = len(alphabet)

    def _format_key(self, text, key):
        key = key.upper()
        return (key * (len(text) // len(key))) + key[:len(text) % len(key)]

    def encrypt(self, plaintext, key):
        plaintext = plaintext.upper()
        key = self._format_key(plaintext, key)
        ciphertext = ''
        for p, k in zip(plaintext, key):
            if p in self.alphabet:
                pi = self.alphabet.index(p)
                ki = self.alphabet.index(k)
                ci = (pi + ki) % self.n
                ciphertext += self.alphabet[ci]
            else:
                ciphertext += p
        return ciphertext

    def decrypt(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        key = self._format_key(ciphertext, key)
        plaintext = ''
        for c, k in zip(ciphertext, key):
            if c in self.alphabet:
                ci = self.alphabet.index(c)
                ki = self.alphabet.index(k)
                pi = (ci - ki + self.n) % self.n
                plaintext += self.alphabet[pi]
            else:
                plaintext += c
        return plaintext
