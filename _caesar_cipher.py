import sys


def main():
    in_txt = str(input('Please input text to cipher:'))
    out_txt = []
    print('Input: ', in_txt)
    try:
        _cipherkey = int(input('Please input cipher key (-25 - 25)'))
        _cipherkey = _cipherkey % 26 if _cipherkey > 0 else _cipherkey % -26
    except:
        print('Unknown value, exiting...')
        sys.exit(-1)
    print('Key: ', _cipherkey)
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
    print(''.join(map(str, out_txt)))


if __name__ == '__main__':
    main()
