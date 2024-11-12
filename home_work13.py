import enchant


class CaesarsCipher:
    """Класс для реализации шифра Цезаря.

    """
    def __init__(self):
        """Инициализатор класса
        """
        self.characters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           'abcdefghijklmnopqrstuvwxyz1234567890 !?.')

    def encrypt(self, message: str, key: int) -> str:
        """Метод для шифрования текста шифром Цезаря.

        Args:
            message: Исходная строка.
            key: Ключ (смещение).

        Returns:
            Зашифрованная строка.
        """
        encrypted_message = ""
        for char in message:
            if char in self.characters:
                index = (self.characters.index(char) + key) % len(
                    self.characters)
                encrypted_message += self.characters[index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message: str, key: int) -> str:
        """Метод для дешифрования текста шифром Цезаря.

        Args:
            message: Зашифрованная строка.
            key: Ключ (сие).

        Returns:
            Расшифрованная строка.
        """
        decrypted_message = ""
        for char in message:
            if char in self.characters:
                index = (self.characters.index(char) - key) % len(
                    self.characters)
                decrypted_message += self.characters[index]
            else:
                decrypted_message += char
        return decrypted_message

    def find_key(self, message: str) -> str:
        """Метод поиска ключа дешифровки для зашифрованного текста.

        Args:
            message: Текст для расшифровки.

        Returns:
            Ключ и расшифрованный текст.
        """
        dictionary = enchant.Dict("en_US")
        flag = 0
        for key in range(len(self.characters)):
            decrypted = self.decrypt(message, key)
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
                break
        return f'Key {key}: {decrypted}'

    @staticmethod
    def write_in_file(path: str, output: str):
        """Функция для записи в файл.

        Args:
            path: Путь к файлу.
            output: Текст для записи в файл.
        """
        with open(f'{path}\\outputfile.txt', 'a', encoding='utf-8') as file:
            file.write(f'{output}\n')

if __name__ == '__main__':
    cipher = CaesarsCipher()
    message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    path = input('Введите путь к файлу: ')
    cipher.write_in_file(path, cipher.find_key(message))
    key = 3
    original_message = "The vacation was a success"
    encrypted = cipher.encrypt(original_message, key)
    cipher.write_in_file(path, encrypted)
    decrypted = cipher.decrypt(encrypted, key)
    cipher.write_in_file(path, decrypted)
    print(f'Результат работы программы можно увидеть в файле: '
          f'{path}\\outputfile.txt')
