import pdb
import qrcode


def qr_code_generator(strings='Hello World'):
    img = qrcode.make(strings)
    return img


def main():
    img = qr_code_generator()
    img.save('test.png')



if __name__ == '__main__':
    main()
