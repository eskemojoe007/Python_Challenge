import string
from collections import deque

base_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# %% My Method before knowing about maketrans
def shift_string(input_str, shift=2):
    ascii_str = string.ascii_lowercase

    def shift_char(char, shift=2):
        key = ascii_str.find(char.lower())
        if key >= 0:
            return ascii_str[(key + shift) % len(ascii_str)]
        else:
            return char

    return ''.join(map(lambda x: shift_char(x, shift=shift), input_str))


shift_string(base_str)
shift_string('map')

# %% Using maketrans
new_list = deque(string.ascii_lowercase)
new_list.rotate(-2)
trans = str.maketrans(string.ascii_lowercase, ''.join(new_list))

base_str.translate(trans)
'map'.translate(trans)
