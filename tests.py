import base64_encode as encoder
import base64_decode as decoder
from logger import *

# scheme = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' # MIME, standard
scheme = 'aABCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz0123456789+/' # index switched ('a')

encoded_str_1 = encoder.encode("f", scheme)
encoded_str_2 = encoder.encode("fo", scheme)
encoded_str_3 = encoder.encode("foo", scheme)
encoded_str_4 = encoder.encode("foob", scheme)
encoded_str_5 = encoder.encode("fooba", scheme)
encoded_str_6 = encoder.encode("foobar", scheme)

decoder.decode(encoded_str_1, scheme)
decoder.decode(encoded_str_2, scheme)
decoder.decode(encoded_str_3, scheme)
decoder.decode(encoded_str_4, scheme)
decoder.decode(encoded_str_5, scheme)
decoder.decode(encoded_str_6, scheme)