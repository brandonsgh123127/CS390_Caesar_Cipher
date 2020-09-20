import sys
def main():
    in_txt = str(input('Please input text to cipher:'))
    out_txt = []
    print('Input: ',in_txt)
    try:
        _cipherkey = int(input('Please input cipher key (-25 - 25)')) % 26
    except:
        print('Unknown value, exiting...')
        sys.exit(-1)
    print('Key: ', _cipherkey)
    for i in in_txt:
        out_txt.append(chr(ord(i)+_cipherkey))
    print(''.join(map(str,out_txt)))

if (__name__ == '__main__'):
    main()