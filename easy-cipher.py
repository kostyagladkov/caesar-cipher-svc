def encode():

   #Alphabets
   alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

   lang = "english"

   #Lang = English
   if lang == "english":
      output = ""
      text = input("Write the text you want to encode: ").lower()
      key = int(input("Enter the key (number): "))
      if key/33 == 1:
         key = input("Input a different key please: ")
         key = int(key)
      else:
         print("")
      for i in text:                                     #Loop to index every symbol in text
         if i in alphabet_eng:                           #Checks if the symbol is a word or not
            t = alphabet_eng.find(i)                     #Finds the index of the symbol
            new_ind = (t + key) % len(alphabet_eng)      #Finds the new index of the word
            output += alphabet_eng[new_ind]              #Converts the new index to a word (strin )from the alphabet and adds it to the output
         else:                                           #If it's not a word, it adds it to the output as it is
            output += i

      

   #Result            
   print("Your encoded text is: " + output)


   print("\nYour encoded text was written in a file named \"encoded_text.txt\" \n")

   #Makes a file and writes the encoded text
   file = open("encoded_text.txt","w+")
   file.write(output)
   file.close()




def decode():

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
      key = int(input("Enter the key (number): "))
      for i in text:                                     #Loop to index every symbol in text
         if i in alphabet_eng:                           #Checks if the symbol is a word or not
            t = alphabet_eng.find(i)                     #Finds the index of the symbol
            new_ind = (t - key) % len(alphabet_eng)      #Finds the new index of the word
            output += alphabet_eng[new_ind]              #Converts the new index to a word (string)from the alphabet and adds it to the output
         else:                                           #If it's not a word, it adds it to the output as it is
            output += i
   else:
      print("")

   #Result            
   print("Your decoded text is: " + output)


choice = input("Choose what you want to do (encode or decode): ").lower()

if choice == "encode":
   encode()
elif choice == "decode":
   decode()
else:
   print("You didn\'t pick correctly")