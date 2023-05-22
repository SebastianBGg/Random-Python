list = [4, 3, 1, 6, 5, 2, 6, 2, 9, 11, 3]
odd = []
ferdig = []
def decode_morse(morse_code):
    for x in list:
        ferdig.append(x)
        if(x % 2):
            odd.append(x)
    odd.sort()
    print(odd)
    for x in range(len(odd)):
        for y in range(len(list)):
            if(list[y] % 2 & list[y] == False):
                print("replace",odd[x],list[y])
                ferdig = odd[x]
                
    print(list)
decode_morse(list)
