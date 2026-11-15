class MediaError(Exception): pass
class UnsupportedFormatError(MediaError): pass
class CompressionError(MediaError): pass
