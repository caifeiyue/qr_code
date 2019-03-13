import os
import logging
import pdb

import qrcode
import qrcode.image.svg

from config import config


def qr_code_generator(strings='Hello World', factory='None'):
    # qr information
    qr = qrcode.QRCode(
        version=config['version'],
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=config['box_size'],
        border=config['border'],)
    qr.add_data(strings)
    qr.make(fit=True)

    if factory == 'None':
        img = qr.make_image(fill_color="black", back_color="white")
    else:
        img = qr.make_image(fill_color="black", back_color="white", image_factory=factory)

    return img


def svg_format(method='basic'):
    if method == 'basic':
        # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
    else:
        # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage
    return factory


def main():
    strings = 'Hello World.'
    factory = svg_format()
    img = qr_code_generator(strings, factory)
    img.save(os.path.join(config['resultpath'], 'test.svg'))


if __name__ == '__main__':
    main()
