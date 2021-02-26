chars = "abcdefghijklmnopqrstuvwxyz1234567890àèìòù,.-_:;ç@#[]()=/&%$£!?^<>§*' "

switches = "(àx][7>s%#w1ir'k$oqò3*gndìhav^b?lj5=c,6£/0@muyù&8eè§-2ç9)4<:t._;fp!z "

code = input("Input code:")

def encode(text):
    result = ""

    f = text
    for i in f:
        idx = chars.index(i)
        result = result + switches[idx]
    return result

def decode(text):
    result = ""

    f = text
    for i in f:
        idx = switches.index(i)
        result = result + chars[idx]
    return result

print("Encoded:")
print(encode(code))
print("Decoded:")
print(decode(code))