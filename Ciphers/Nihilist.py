from Polybius import polybiusSquare

# The nihilist cipher is a composite cipher that uses the polybius square
# along with a modified vigenere cipher. Rather than wrapping around modulo 26
# addition and subtraction and performed normally.
def nihilistCipher(text,key=["A","A"],decode=False,mode="EX"):
    
    # Convert the vigenere key into numbers using the polybius square
    keynum = polybiusSquare(key[1],key[0],mode=mode,sep=" ")
    keynum = [int(n) for n in keynum.split(" ")]
    kLen = len(keynum)
    
    if decode == False:
        
        textnum = polybiusSquare(text,key[0],mode=mode,sep=" ")
        textnum = [int(n) for n in textnum.split(" ")]


        for i in range(len(textnum)):
            textnum[i] = (textnum[i]+keynum[i%kLen])
        
        return " ".join([str(i) for i in textnum])
    
    if decode == True:
        
        textnum = [int(n) for n in text.split(" ")]
        
        for i in range(len(textnum)):
            textnum[i] = (textnum[i]-keynum[i%kLen])
        
        textnum = " ".join([str(i) for i in textnum])
        
        dtext = polybiusSquare(textnum,key[0],decode=True,mode=mode,sep=" ")
            
        return dtext
    
def nihilistCipherExample():
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = ["SOMETHING","NIHILIST"]
    print("Example Of The Nihilist Cipher\n\nKey is {}\n".format(key))

    mode = "KQ"
    print("Plaintext is:  {}".format(ptext))
    ctext = nihilistCipher(ptext,key,mode = mode)
    print("Ciphertext is: {}".format(ctext))
    dtext = nihilistCipher(ctext,key,decode=True, mode = mode)
    print("Decodes As:    {}".format(dtext))