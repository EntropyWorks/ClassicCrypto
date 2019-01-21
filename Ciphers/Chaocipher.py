# The Chaocipher is a clever mechanical cipher that operates by creating a
# permutation of the alphabet rather than just shifting it.

# Step a forward by N
def stepN(R,n):
    x = R[:]
    for i in range(n):
        x = x[1:] + x[0]
    return x

def permuteL(L,letter):
    L = stepN(L,L.index(letter))
    L = L[0] + L[2:14] + L[1] + L[14:]
    return L
    
def permuteR(R,letter):
    R = stepN(R,R.index(letter)+1)
    R = R[0:2] + R[3:14] + R[2] + R[14:]
    return R

def chaocipher(text,keys=["",""],decode=False):
    
    if keys[0] == "":
        L = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    else:
        L = keys[0]
    
    if keys[1] == "":
        R = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    else:
        R = keys[1]
    
    if decode == False:
        out = ""
        for letter in text:
            pos = R.index(letter)
            out += L[pos]
            L = permuteL(L,L[pos])
            R = permuteR(R,letter)
        return out
    
    if decode == True:
        out = ""
        for letter in text:
            pos = L.index(letter)
            out += R[pos]
            L = permuteL(L,letter)
            R = permuteR(R,R[pos])
    
        return out 
    
    
def chaocipherExample():
    print("Example of the Chaocipher\n")
    
    L = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    R = "PTLNBQDEOYSFAVZKGJRIHWXUMC"


    print("The Left Alphabet:  {}".format(L))
    print("The Right Alphabet: {}".format(R))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = chaocipher(ptext,[L,R])
    dtext = chaocipher(ctext,[L,R],decode=True)
    print("\nPlaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))