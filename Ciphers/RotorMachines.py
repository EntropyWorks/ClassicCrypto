# An Engima style rotor machine. The method is actually quite simple. Each
# letter is encrypted by a series of simple substitution ciphers that change
# automatically for each letter. However because this behavior is quite regular
# it is not especially hard to break the resulting cipher. Using the plugboard
# to swap letters makes it significantly more secure. The military Enigma
# historically chose ten letter pairs.

# Because this simulated rotor machine can accept arbitrary rotors even if the
# number of rotors in use is known the key space is absurdly large. However
# rotor machines like this are very well analyzed and should not be considered
# secure simply because of the number of possible keys.

# This is NOT a simulation of the actual Enigma machine as that included a
# some mechanisms this does not such as rotors that stepped at two different
# places.

import datetime


# Pass a singal through a rotor
def rotor(letter,key,pos,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    entry = alpha.index(letter)
    
    if decode == False:
        inner = key[(entry+pos-1)%26]
        outer = (alpha.index(inner)-pos+1)%26
        return alpha[outer]
    if decode == True:
        inner = alpha[(entry+pos-1)%26]
        outer = (key.index(inner)-pos+1)%26
        return alpha[outer]


#def ringSetting(key,n):
#    for i in range(n-1):
#        key = key[1:] + key[0]
#    return key

# The plugboard (Steckerbrett) flips pairs of letters
# Pairs of letters are not allowed to overlap
def plugboard(text,keys):
    
    if keys == []:
        return text
    
    # A very messy bit of code that makes sure only unique pairs of letters
    # are swapped.
    for pos,key in enumerate(keys):
        for let in key:
            for i in range(pos+1,len(keys)):
                if let in keys[i]:
                    raise Exception('pairs of letters cannot overlap')
    
    # Do the swapping
    for key in keys:
        text = text.replace(key[0],"*")
        text = text.replace(key[1],key[0])
        text = text.replace("*",key[1])
    return text


# Should get around to a copy of Enigma at some point
def enigma(text,keys,decode=False):
    
    # Check that theere are exactly five machine settings provided
    if len(keys) != 5:
        raise Exception('the "keys" argument must provide rotors, reflector, rotor positions, plugs, and ring settings')
    
    
    
    
    ref = keys[1]
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    positions = [alpha.index(i)+1 for i in keys[2]]
    plugs = keys[3]
    rings = [alpha.index(i) for i in keys[4]]
    
    # Look at the keys[0] argument and use it to 
    
    rotors = []
    notches = []
    for num in keys[0]:
        if num == "I":
            rotors.append("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
            notches.append(17)
        if num == "II":
            rotors.append("AJDKSIRUXBLHWTMCQGZNPYFVOE")
            notches.append(5)
        if num == "III":
            rotors.append("BDFHJLCPRTXVZNYEIWGAKMUSQO")
            notches.append(13)
        if num == "IV":
            rotors.append("ESOVPZJAYQUIRHXLNFTGKDCMWB")
            notches.append(10)
        if num == "V":
            rotors.append("VZBRGITYUPSDNHLXAWMJQOFECK")
            notches.append(26)

    rotors.reverse()
    notches.reverse()

    


    positions.reverse()
    rings.reverse()

    for i in range(3):
        positions[i] -= rings[i]
    

    reflector = ""
    if ref == "RA":
        reflector = "EJMZALYXVBWFCRQUONTSPIKHGD"
    if ref == "RB":
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    if ref == "RC":
        reflector = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


    
    text = plugboard(text,plugs)
    
    out = []
    
    # For each letter
    for letter in text:
        
        T = letter
        
        positions[0] += 1
        if positions[0] % 26 == notches[0]:
            positions[1] += 1
        if positions[1] % 26 == notches[1]:
            positions[2] += 1
        
        
        T = rotor(T,rotors[0],positions[0])
        T = rotor(T,rotors[1],positions[1])
        T = rotor(T,rotors[2],positions[2])
        T = rotor(T,reflector,1)
        T = rotor(T,rotors[2],positions[2],True)
        T = rotor(T,rotors[1],positions[1],True)
        T = rotor(T,rotors[0],positions[0],True)
        
        out.append(T)
            
    out = "".join(out)
    
    out = plugboard(out,plugs)
    
    return "".join(out)



# Should get around to a copy of SIGABA at some point
def SIGABA(text,keys,decode=False):
    pass

def enigmaExample():
    
    print("Enigma Example\n")

    rotors = ["II","III","I"]
    rings = ["B","T","G"]
    positions = ["C","B","A"]
    reflector = "RB"
    plugs = ["AT","HY","JM"]
    
    print("Today is {}\n\nThe Codebook Settings Are:".format(datetime.datetime.now().date()))
    for i in rotors:
        print(i,end = " ")
    print(" | ",end = " ")
    for i in positions:
        print(i,end = " ")
    print(" | ",end = " ")
    for i in plugs:
        print(i,end = " ")
    
    print("\n\nRing Settings:",end= " ")
    for i in rings:
        print(i,end = " ")
    print("\n")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = enigma(ptext,keys=[rotors,reflector,positions,plugs,rings])
    dtext = enigma(ctext,keys=[rotors,reflector,positions,plugs,rings])
    print(ctext)
    if dtext != ptext:
        print("ERROR")
        print(dtext)


enigmaExample()