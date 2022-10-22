import base64_encode as encoder
import base64_decode as decoder

# from base64 import base64_decode as decoder
import logging

# scheme = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' # MIME, standard
scheme = 'aABCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz0123456789+/' # index switched ('a')

encoded_str_1 = encoder.encode("f", scheme, logging.INFO)
encoded_str_2 = encoder.encode("fo", scheme, logging.INFO)
encoded_str_3 = encoder.encode("foo", scheme, logging.INFO)
encoded_str_4 = encoder.encode("foob", scheme, logging.INFO)
encoded_str_5 = encoder.encode("fooba", scheme, logging.INFO)
encoded_str_6 = encoder.encode("foobar", scheme, logging.INFO)

decoder.decode(encoded_str_1, scheme, logging.INFO)
decoder.decode(encoded_str_2, scheme, logging.INFO)
decoder.decode(encoded_str_3, scheme, logging.INFO)
decoder.decode(encoded_str_4, scheme, logging.INFO)
decoder.decode(encoded_str_5, scheme, logging.INFO)
decoder.decode("Ym9vXmEy", scheme, logging.INFO)