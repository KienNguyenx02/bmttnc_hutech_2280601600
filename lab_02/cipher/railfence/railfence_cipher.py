class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = ['' for _ in range(num_rails)]
        direction = 1
        row = 0

        for char in plain_text:
            rails[row] += char
            row += direction

            if row == 0 or row == num_rails - 1:
                direction *= -1

        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        pattern = ['' for _ in range(len(cipher_text))]
        direction = 1
        row = 0

        for i in range(len(cipher_text)):
            pattern[i] = row
            row += direction
            if row == 0 or row == num_rails - 1:
                direction *= -1

        rail_lengths = [pattern.count(r) for r in range(num_rails)]
        rails = []
        index = 0
        for length in rail_lengths:
            rails.append(cipher_text[index:index+length])
            index += length

        rail_pointers = [0] * num_rails
        result = ''
        for r in pattern:
            result += rails[r][rail_pointers[r]]
            rail_pointers[r] += 1

        return result
