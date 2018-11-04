from ..util import LoadLibrary
from .avcodec import AVCodec_p, AVCodecContext_p


libavcodec = LoadLibrary('avcodec')


avcodec_alloc_context3 = libavcodec.avcodec_alloc_context3
avcodec_alloc_context3.argtypes = [AVCodec_p]
avcodec_alloc_context3.restype = AVCodecContext_p
