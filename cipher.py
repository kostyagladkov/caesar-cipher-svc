import caesar

choice = input("Choose what you want to do (encode or decode): ").lower()


if choice == "encode":
    text = input("Now write what do you want to encode: ")
    key = input("Great, now you have to choose a key (write a number):")
    key = int(key)
    if key%26 == 0:
        key = input("Input a different key please: ")
        key = int(key)
    caesar.encode(text, key)
elif choice == "decode":
    key = input("Choose your key to decode (write a number):")
    key = int(key)
    caesar.decode(key)
else:
    print("You didn\'t pick a correct choice")