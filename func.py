from string import ascii_lowercase
import pandas as pd

def letter_count(phrase):
    letters = [ch for ch in phrase]
    s = set(letters)
    counts = []
    for ch in s:
        counts.append((ch, letters.count(ch)))
    counts.sort(reverse=True, key=lambda x: x[1])
    return counts

BASE62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encode_62(num, alphabet=BASE62):
    """Encode a positive number in Base X

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode_62(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

def rot_n_letter(l, n, alphabet = ascii_lowercase):
    ix = alphabet.find(l)
    ix = (ix+n) % len(alphabet)
    return alphabet[ix]

def rot_n(s, n, alphabet = ascii_lowercase):
    new_s = ''
    for l in s:
        new_s += rot_n_letter(l, n, alphabet)
    return new_s

def letter_frequency(message):
    message = ''.join(message.split())
    s = set(message)
    res = []
    for ch in s:
        res.append((ch, message.count(ch)))
    df = pd.DataFrame(res)
    df[2] = df[1] / len(df[1])
    df = df.sort_values(2)
    return(df)

def substitute(l_find, l_fill, original, fillin = ''):

    d = {}
    for ch1, ch2 in zip(l_find, l_fill):
        d[ch1] = ch2

    if fillin == '':
        fillin = ' ' * len(original)

    for i, ch in enumerate(original):
        if ch in d:
            end = fillin[i:]
            if len(end) == 1:
                end = ''
            else:
                end = end[1:]
            fillin = fillin[:i] + d[ch] + end
    return fillin

