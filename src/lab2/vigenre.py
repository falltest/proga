def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    while len(keyword) < len(plaintext):
        keyword *= 2
    keyword = keyword[:len(plaintext)]

    for i, c in enumerate(plaintext):
        k = keyword[i]
        if c.isupper():
            shift = ord(k.upper()) - ord('A')
            idx = (ord(c) - ord('A') + shift) % 26
            ciphertext += chr(idx + ord('A'))
        elif c.islower():
            shift = ord(k.lower()) - ord('a')
            idx = (ord(c) - ord('a') + shift) % 26
            ciphertext += chr(idx + ord('a'))
        else:
            ciphertext += c
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    while len(keyword) < len(ciphertext):
        keyword *= 2
    keyword = keyword[:len(ciphertext)]

    for i, c in enumerate(ciphertext):
        k = keyword[i]
        if c.isupper():
            shift = ord(k.upper()) - ord('A')
            idx = (ord(c) - ord('A') - shift) % 26
            plaintext += chr(idx + ord('A'))
        elif c.islower():
            shift = ord(k.lower()) - ord('a')
            idx = (ord(c) - ord('a') - shift) % 26
            plaintext += chr(idx + ord('a'))
        else:
            plaintext += c
    return plaintext