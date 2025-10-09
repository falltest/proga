def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    cifr = set('1234567890')
    bukv = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    for c in plaintext:
        if c in cifr or c not in bukv:
            ciphertext += c
            continue
        new_ind = ord(c) + shift
        if c == c.upper():
            new_ind -= ord('A')
            if new_ind >= 26:
                new_ind %= 26
                ciphertext += chr(new_ind + ord('A'))
            else:
                ciphertext += chr(new_ind + ord('A'))
        if c == c.lower():
            new_ind -= ord('a')
            if new_ind >= 26:
                new_ind %= 26
                ciphertext += chr(new_ind + ord('a'))
            else:
                ciphertext += chr(new_ind + ord('a'))
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    bukv = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    for c in ciphertext:
        if c not in bukv:
            plaintext += c
            continue
        new_ind = ord(c) - shift
        if c == c.upper():
            new_ind -= ord('A')
            if new_ind < 0:
                new_ind = ord('Z') - abs(new_ind) + 1
                plaintext += chr(new_ind)
            else:
                plaintext += chr(new_ind + ord('A'))
        if c == c.lower():
            new_ind -= ord('a')
            if new_ind < 0:
                new_ind = ord('z') - abs(new_ind) + 1
                plaintext += chr(new_ind)
            else:
                plaintext += chr(new_ind + ord('a'))
    return plaintext

print(encrypt_caesar("Python3.6"))