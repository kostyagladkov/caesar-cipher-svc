def encode(text,key):

    #Alphabets
    alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

    output = ""
    for i in text:                                       #Loop to index every symbol in text
        if i in alphabet_eng:                            #Checks if the symbol is a word or not
            t = alphabet_eng.find(i)                     #Finds the index of the symbol
            new_ind = (t + key) % len(alphabet_eng)      #Finds the new index of the word
            output += alphabet_eng[new_ind]              #Converts the new index to a word (strin )from the alphabet and adds it to the output
        else:                                            #If it's not a word, it adds it to the output as it is
            output += i


    return output



def decode(text, key):

    #Alphabets
    alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

    output = ""
    for i in text:                                       #Loop to index every symbol in text
        if i in alphabet_eng:                            #Checks if the symbol is a word or not
            t = alphabet_eng.find(i)                     #Finds the index of the symbol
            new_ind = (t - key) % len(alphabet_eng)      #Finds the new index of the word
            output += alphabet_eng[new_ind]              #Converts the new index to a word (string)from the alphabet and adds it to the output
        else:                                            #If it's not a word, it adds it to the output as it is
            output += i

    return output


