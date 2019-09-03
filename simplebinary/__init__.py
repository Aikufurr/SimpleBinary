def toBinary(string):
    return ''.join([bin(ord(ch))[2:].zfill(8) for ch in string])

def toString(binary):
    loop = 0
    n = 8
    out = ""
    split = [binary[i:i+n] for i in range(0, len(binary), n)]
    for i in split:
        t = split[loop]
        r = int(t, 2)
        out += str(chr(r))
        loop += 1

    return out
