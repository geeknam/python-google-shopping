

def gtin_checksum(code):
    total = 0

    for (i, c) in enumerate(code):
        if i % 2 == 1:
            total = total + int(c)
        else:
            total = total + (3 * int(c))

    check_digit = (10 - (total % 10)) % 10
    return check_digit


def gtin_pad(gtin):
    """
    Append 0 to fill in the exact format of
    gtin12 schema value
    """
    zero_space = 11 - len(gtin)
    gtin = '%s%s' % ('0'*zero_space, gtin)
    if len(gtin) == 11:
        gtin = '%s%s' % (gtin, gtin_checksum(gtin))
    return gtin
