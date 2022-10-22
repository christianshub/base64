import logging, sys

def encode(input_str, scheme, log_level = logging.DEBUG):
    logging.basicConfig(stream=sys.stderr, level=log_level)

    if (len(scheme) != 64):
        raise Exception("Not a base64 scheme, needs to be 64 characters")

    logging.debug(f"Scheme: {scheme}, length: {len(scheme)}")
    for i in range(len(scheme)):
        logging.debug(f"Letter: {scheme[i]}, index: {i}")

    binary_string = ""
    for i in range(len(input_str)):
        binary_string += format(ord(input_str[i]), '08b')
    
    logging.debug(f"Length of binary_string: {len(binary_string)}, binary string: {binary_string}")
   
    arr_length = len(binary_string)
    leftover = arr_length % 6
    logging.debug(f"arr_lenght: {arr_length}, leftover: {leftover}")

    main_arr = []
    leftover_bits = []
    leftover_bit_amount = 0

    if (leftover != 0):
        main_arr = binary_string[:-leftover]
        leftover_bits = binary_string[-leftover:]
        leftover_bit_amount = 6 - leftover
        logging.debug(f"main_arr: {main_arr}, leftover_bits: {leftover_bits}, type: {type(leftover_bits)}, leftover_bit_amount: {leftover_bit_amount}")
    else:
        main_arr = binary_string
    
    curStr = ""; arr = [];
    for i in range(1, len(main_arr)+1):
        if (i % 6 == 0) and (i != 0):
            curStr += main_arr[i-1]
            arr.append(curStr)
            curStr = ""
        else:
            curStr += main_arr[i-1]


    if (leftover != 0):
        new_leftover = leftover_bits
        for i in range(leftover_bit_amount):
            new_leftover = new_leftover + '0'

        arr.append(new_leftover)


    logging.debug(f"Encoded binary string: {arr}")

    encoded_str_indexes = []

    for i in arr:
        encoded_str_indexes.append(int(i, 2))

    logging.debug(f"Encoded str indexes: {encoded_str_indexes}")

    encoded_str = ""
    for i in encoded_str_indexes:
        encoded_str = encoded_str + scheme[i]

    logging.info(f"Encoder: Pre-encoded '{input_str}' encoded to '{encoded_str}'")
    return encoded_str

