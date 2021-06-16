
a = 'abcdae'

def crc_byte(data):
    crc_byte = 0
    for i in  range(0, 8):
        if((crc_byte^data) & 0x01):
            crc_byte ^= 0x18
            crc_byte >>= 1
            crc_byte |= 0x80
        else:
            crc_byte >>= 1
        data >>= 1

    return crc_byte
    pass

def crc8(data):
    ret = 0
    for byte in data:
        ret = (crc_byte(ret^byte))
    return ret
