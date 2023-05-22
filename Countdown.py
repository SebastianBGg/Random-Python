from time import sleep
total = 0
timer = 0
minuter = 0
sekunder = 0
loop = 1
def nedtelling():
    total = timer + minuter + sekunder
    for x in range(total):
        total = total - 1
        print(total)
        sleep(1)
    print("Ferdig")
while loop == 1:
    svar = input("-T for timer \n"
    "-M for minuter\n"
    "-S for sekunder\n"
    "-F for ferdig\n").lower()
    if svar == "t":
        timer = int(input("Hvor mange timer?\n"))
        timer = timer * 3600
    if svar == "m":
        minuter = int(input("Hvor mange minuter?\n"))
        minuter = minuter * 60
    if svar == "s":
        sekunder = int(input("Hvor mange minuter?\n"))
    if svar == "f":
        loop = 0
nedtelling()