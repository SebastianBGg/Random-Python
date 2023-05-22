
navn = []
alder = []
kjeledyr = []
hobby = []
f = open("Data.txt", "w")
f.close
f = open("Data.txt", "r")
text = f.read()
print(text)
f.close

def lagtext():
    f = open("Data.txt", "a")
    f.truncate(0)
    f.write(text)
    for x in range(len(navn)):
        f.write("Navn:"+navn[x]+", Alder: "+alder[x]+", Antall kjeledyr: "+kjeledyr[x]+"\n" "Hobby: "+hobby[x]+"\n"+"\n")
    f.close()

def melding():
    print("L - For legg til elev")
    print("V - Vis alle elever")
    print("H - Skriver ut navn og hobby til alle elever.")
    print("K - Skal skrive ut alle elever som har X antall kjeledyr.")
    print("A - Avslutte programmet.")
    print("Hva velger du?")

def elevadd():
    elevnavn = input("Skriv navn til eleven\n")
    elevalder = input("Skriv alder til eleven\n")
    elevkjeledyr = input("Skriv antall kjeledyr til eleven\n")
    elevhobby = input("Skriv hobby til eleven\n")
    navn.append(elevnavn)
    alder.append(elevalder)
    kjeledyr.append(elevkjeledyr)
    hobby.append(elevhobby)

def view():
    f = open("Data.txt", "r")
    text = f.read()
    print(text)
    f.close
    for x in range(len(navn)):
        print(text)

def sehobby():
    for x in range(len(navn)):
        print(navn[x]+" Sin hobby er "+ hobby[x])

def elevkjeledyr():
    antall = input("Hvor mange kjeledyr vil du søke etter? \n")
    for x in range(len(kjeledyr)):
        if kjeledyr[x] == antall:
            print(navn[x]+" har "+kjeledyr[x])
            
def main():
    svar=""
    klasse = []
    while svar != "a":
        melding()
        svar = input("").lower()
        if svar == "l":
            elevadd()
            lagtext()
        if svar == "v":
            view()
        if svar == "h":
            sehobby()
        if svar == "k":
            elevkjeledyr()
        
main()