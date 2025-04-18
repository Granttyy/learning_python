text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            
            key_char = key[key_index % len(key)]
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

vigenere(text, custom_key)
# The code above is a simple implementation of the Vigenère cipher, which is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. The key is repeated to match the length of the message, and each letter in the message is shifted by the corresponding letter in the key. The code also handles spaces in the message.