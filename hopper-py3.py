import codecs
import json
from tkinter import filedialog as fd


def deserializeJSON(script_file):
    f = codecs.open(script_file, "r","utf-8")

    # Reading from file
    data = json.loads(f.read())
    return data


def changeAddressNames(script):
    print(script['ScriptMethod'][0])
    for i in script['ScriptMethod']:
        addr = i['Address']
        name = i['Name']
        sig = i['Signature']
        typesig = i['TypeSignature']
        
        #print(addr, name)
        doc.setNameAtAddress(addr,name)

    return


def main():
    script_file = fd.askopenfilename()
    script = deserializeJSON(script_file)
    changeAddressNames(script)

doc = Document.getCurrentDocument()
main()
