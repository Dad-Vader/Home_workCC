import enchant


class CaesarsCipher:
    def __init__(self):
        self.characters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           'abcdefghijklmnopqrstuvwxyz1234567890 !?.')

    def encrypt(self, message, key):
        encrypted_message = ""
        for char in message:
            if char in self.characters:
                index = (self.characters.index(char) + key) % len(
                    self.characters)
                encrypted_message += self.characters[index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message, key):
        decrypted_message = ""
        for char in message:
            if char in self.characters:
                index = (self.characters.index(char) - key) % len(
                    self.characters)
                decrypted_message += self.characters[index]
            else:
                decrypted_message += char
        return decrypted_message


cipher = CaesarsCipher()
message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
dictionary = enchant.Dict("en_US")
flag = 0
for key in range(len(cipher.characters)):
    decrypted = cipher.decrypt(message, key)
    word_list = decrypted.split(' ')
    if len(word_list) > 1:
        count = 0
        for word in word_list:
            if count > 2:
                flag = 1
                break
            try:
                if dictionary.check(word):
                    count += 1
                else:
                    break
            except ValueError:
                break
    if flag == 1:
        print(f"Key {key}: {decrypted}")
        break


key = 3
original_message = "The vacation was a success"
encrypted = cipher.encrypt(original_message, key)
print(encrypted)
decrypted = cipher.decrypt(encrypted, key)
print(decrypted)
