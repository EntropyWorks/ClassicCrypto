from Ciphers.UtilityFunctions import groups, alphabetPermutation
import numpy as np

def fourSquare(text,keys,decode=False,printkey=False):
        
    k1 = alphabetPermutation(keys[0],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    k2 = alphabetPermutation(keys[1],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    sq1 = np.full([6,6],"")
    sq2 = np.full([6,6],"")
    alphasq = np.full([6,6],"")
    for i in range(6):
        sq1[i] = [x for x in groups(k1,6)[i]]
        sq2[i] = [x for x in groups(k2,6)[i]]
        alphasq[i] = [x for x in groups("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",6)[i]]

    if printkey == True:
        for i in range(6):
            print(" ".join(alphasq[i]),end="  ")
            print(" ".join(sq1[i]))
        print()
        for i in range(6):
            print(" ".join(sq2[i]),end="  ")
            print(" ".join(alphasq[i]))
        return ""


    if len(text) % 2 == 1:
        text += "X"
    G = groups(text,2)
    
    if decode == False:
        out = ""
        for g in G:
            A = np.where(sq1 == g[0])
            B = np.where(sq2 == g[1])
            
            out += alphasq[A[0],B[1]][0]
            out += alphasq[B[0],A[1]][0]
            
        return out
    
    if decode == True:
        out = ""
        for g in G:
            A = np.where(alphasq == g[0])
            B = np.where(alphasq == g[1])
            
            out += sq1[A[0],B[1]][0]
            out += sq2[B[0],A[1]][0]
            
        return out
    
def fourSquareExample():
    print("Example of the Four Square Cipher\n")
    print("The key is:")
    keys = ["4SQUARE5","738CIPHER091"]
    fourSquare("TEST",keys,printkey=True)
    
    print("")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = fourSquare(ptext,["2SQUARE5","738CIPHER091"])
    dtext = fourSquare(ctext,["2SQUARE5","738CIPHER091"],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))