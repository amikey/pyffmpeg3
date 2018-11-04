from .libavcodec import libavcodec
from .avcodec import codecs, AVCodec_p
from ctypes import cast

BUFFER_MIN_SIZE = 16384  # should this keep INPUT?

def find_encoder(enum_name: str):
    """Find a codec by the enumerate name.

    Parameters
    ----------
    enum_name:
        The codec name. e.g. ``'H264'``

    Returns
    -------
    AVCodec_p

    Examples
    --------

    >>> codec = encoding.find_encoder('H264')

    """
    f = libavcodec.avcodec_find_encoder
    f.restype = AVCodec_p
    return f(codecs[enum_name])


def find_encoder_by_name(codec_name: str):
    """Find a codec by the friendly name.

    Parameters
    ----------
    codec_name:
        The codec name. e.g. ``'libx264'``

    Returns
    -------
    AVCodec_p

    Examples
    --------

    >>> codec = encoding.find_encoder_by_name('libx264')

    """
    f = libavcodec.avcodec_find_encoder_by_name
    f.restype = AVCodec_p
    return f(codec_name.encode())
