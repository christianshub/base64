from logger import *

def binStr_to_ascii(binStr):
    
    ascii_text = ""
    try:
        # Python program to illustrate the
        # conversion of Binary to ASCII
        
        # Initializing a binary string in the form of
        # 0 and 1, with base of 2
        binary_int = int(binStr, 2);
        
        # Getting the byte number
        byte_number = binary_int.bit_length() + 7 // 8
        
        # Getting an array of bytes
        binary_array = binary_int.to_bytes(byte_number, "big")
        
        # Converting the array into ASCII text
        ascii_text = binary_array.decode()
    except (UnicodeDecodeError):
        ascii_text += "."
            
    # Getting the ASCII value
    return ascii_text

def decode(input_str, scheme):
    logging.debug(f"Pre-encoded input: {input_str}")
    if (len(scheme) != 64):
            raise Exception("Not a base64 scheme, needs to be 64 characters")

    logging.debug(f"Scheme: {scheme}, length: {len(scheme)}")
    for i in range(len(scheme)):
        logging.debug(f"Letter: {scheme[i]}, index: {i}")

    scheme_index_arr = []
    for i in input_str:
        for j in range(len(scheme)):
            if (i == scheme[j]):
                logging.debug(f"Match!: input letter: {i}, scheme index: {j}, scheme letter: {scheme[j]}")
                scheme_index_arr.append(j)

    logging.debug(f"scheme index: {scheme_index_arr}")

    binary_string = ""
    for i in scheme_index_arr:
        binary_string += '{0:06b}'.format(i)

    
    logging.debug(f"binary str: {binary_string}, len: {len(binary_string)}")

    curStr = ""; arr = [];
    for i in range(1, len(binary_string)+1):
        if (i % 8 == 0) and (i != 0):
            curStr += binary_string[i-1]
            arr.append(curStr)
            curStr = ""
        else:
            curStr += binary_string[i-1]

    logging.debug(f"binary string (8 digits): {arr}")

    retStr = ""
    for i in arr:
        retStr = retStr + binStr_to_ascii(i)

    logging.info(f"Decoder: Pre-decoded '{input_str}' decoded to '{retStr}'")

    return retStr    
