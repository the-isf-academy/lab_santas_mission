# helpers.py
from PyPDF2 import PdfReader, PasswordType   


# ----------------------------------------------------- #
# Here are a few useful functions! 
# You'll need to use these to win the prize. 
# You may even need to write one or two of your own to finish the mission.
#  
# ----------------------------------------------------- #

def caesar_cipher(plain_text, encryption_key ):
    # returns the plain_text encrypted by the encryption key number

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""

    for letter in plain_text: 
        letter = letter.lower()
        if letter != " ":
            letter_index = alphabet.index(letter)
            letter_encrypted_index = letter_index + encryption_key
            letter_encrypted_index = letter_encrypted_index%26
            cipher_text += alphabet[letter_encrypted_index]
        
        else:
            cipher_text += letter

    return cipher_text

def break_pdf(decryption_key, pdf_file):
    # returns True if the password decrypts the pdf file
    reader = PdfReader(pdf_file) 

    if reader.decrypt(decryption_key) == PasswordType.OWNER_PASSWORD:
        return True

    return False



