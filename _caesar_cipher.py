import sys
'''
Caesar Cipher Implementation
Author: Brandon Spada & Leonardo Pegeas
'''
def main():
    in_txt = str(input('Please input text to cipher: '))
    out_txt = []
    print('Input: ', in_txt)
    # Verify key is correct
    try:
        _cipherkey = int(input('Please input cipher key: '))
        _cipherkey = _cipherkey % 26 if _cipherkey > 0 else _cipherkey % -26
    except:
        print('Unknown value, exiting...')
        sys.exit(-1)
    print('Key: ', _cipherkey)
    '''
    For each letter in the input text, shift ascii number by value of cipher key,
    then append to a list that will contain new values.
    '''
    for i in in_txt:
        # Space stays the same
        if ord(i) == 32:
            out_txt.append(chr(ord(i)))
        # Lower Case letter boundaries
        elif ord(i) + _cipherkey < 97 and 97 <= ord(i) <= 122:
            out_txt.append(chr(ord(i) + _cipherkey + 26))
        elif ord(i) + _cipherkey > 122 and 97 <= ord(i) <= 122:
            out_txt.append(chr(ord(i) + _cipherkey - 26))
        # Upper case letter boundaries
        elif ord(i) + _cipherkey > 90 and 65 <= ord(i) <= 90:
            out_txt.append(chr(ord(i) + _cipherkey + 26))
        elif ord(i) + _cipherkey < 65 and 65 <= ord(i) <= 90:
            out_txt.append(chr(ord(i) + _cipherkey + 26))
        else:
            out_txt.append(chr(ord(i) + _cipherkey))
    print('Encrypted: ', ''.join(map(str, out_txt)))

    '''
    Decryption phase: TO BE IMPLEMENTED:
                        We have encryption variable key, just get opposite value of key and apply another loop
                        to reverse encryption.
    '''


if __name__ == '__main__':
    main()
