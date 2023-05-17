def morsefrase(morse):
    datosmorse={
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    " ": "/",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−"}
    frase=" "
    caracteres=morse.split(" ")
    for codigo in caracteres:
        for clave,valor in datosmorse.items():
            if valor==codigo:
                frase=frase + clave
                break
            else:
                frase=frase + " "
    return frase 
def FraseMorse(frase):
    datosmorse={
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    " ": "/",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−"}
    morse=" "
    for caracter in frase:
        caracter=caracter.upper()
        if caracter in datosmorse:
            codigomorse=datosmorse[caracter]
            morse=morse + codigomorse + " "
        else:
            morse = morse +" "

texto=input("Ingrese un texto  o codigo Morse: ")
if "-" in texto or "." in texto:
    frase= morsefrase(texto)
    print("la frase es: ",frase)
else:
    codigo_morse=FraseMorse(texto)
    print("la frase es: ",str(codigo_morse))