from guizero import *

chars = "abcdefghijklmnopqrstuvwxyz1234567890àèìòù,.-_:;ç@#[]()=/&%$£!?^<>§*' "

switches = "(àx][7>s%#w1ir'k$oqò3*gndìhav^b?lj5=c,6£/0@muyù&8eè§-2ç9)4<:t._;fp!z "

def encode():
    #Function to encode
    #words into the text in the guy
    result = ""

    f = text_box.value.lower()
    for i in f:
        idx = chars.index(i)
        result = result + switches[idx]
    
    if (caps.value == True):
        text.value = result.upper()
    else: text.value = result

def decode():
    #Same as encode() but it decodes
    result = ""

    f = text_box.value.lower()
    for i in f:
        idx = switches.index(i)
        result = result + chars[idx]
    if (caps.value == True):
        text.value = result.upper()
    else: text.value = result

#GUI
app = App(title="Encoder", bg="#000000", layout="grid", width=400, height=130)

text_box = TextBox(app, grid=[0,0], width=32)
text_box.text_color = "#ffffff"
box = Box(app, grid=[0,1])
encode_button = PushButton(box, command=encode, text="Encode", align="left", width=10)
encode_button.text_color = "#ffffff"
decode_button = PushButton(box, command=decode, text="Decode", align="left", width=10)
decode_button.text_color = "#ffffff"
caps = CheckBox(app, text="Capital", grid=[1,0])
caps.text_color = "#ffffff"
text = Text(app, grid=[0,2], size=24, align="left", color="#ffffff")

app.display()
