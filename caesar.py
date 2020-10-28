def encode(text,key):

    #Alphabets
    alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

    lang = "english"

    #Lang = English
    if lang == "english":
        output = ""
    else:
        print("What?")
    for i in text:                                     #Loop to index every symbol in text
        if i in alphabet_eng:                           #Checks if the symbol is a word or not
            t = alphabet_eng.find(i)                     #Finds the index of the symbol
            new_ind = (t + key) % len(alphabet_eng)      #Finds the new index of the word
            output += alphabet_eng[new_ind]              #Converts the new index to a word (strin )from the alphabet and adds it to the output
        else:                                           #If it's not a word, it adds it to the output as it is
            output += i

    print("\nDone")

    return output





def decode(key):

    #Alphabets
    alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

    lang = "english"


    #Opens and reads the file
    file = open ("encoded_text.txt", "r")
    file_text = (file.readline())

    #Lang = English
    if lang == "english":
        output = ""
        text = file_text
        for i in text:                                     #Loop to index every symbol in text
            if i in alphabet_eng:                           #Checks if the symbol is a word or not
                t = alphabet_eng.find(i)                     #Finds the index of the symbol
                new_ind = (t - key) % len(alphabet_eng)      #Finds the new index of the word
                output += alphabet_eng[new_ind]              #Converts the new index to a word (string)from the alphabet and adds it to the output
            else:                                           #If it's not a word, it adds it to the output as it is
                output += i
    else:
        print("")

    print("\nDone")

    return output


