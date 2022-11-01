def cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts a Caeser cipher.
    Parameters
    ---
    text: string
        Input string for encrypting or decrypting. 
    shift: integer
        Integer value indicating the number of shift for each alphabet.
    encrypt: bool
        Boolean value determining whether the function encrypts or decrypts text. Defaults to 'True', use false to decrypt. 
    Returns
    ---
    new_text: string
        the encrypted or decrypted new text

    Examples
    ---
    Encryption:
    >>> cipherpkg.cipher('text', 5, encrypt = True)
    'yjCy'
    Decryption:
    >>> cipherpkg.cipher('yjCy', 5, encrypt = False)
    'text'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text