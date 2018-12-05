word = (input("Type the word you want encrypted here:"))
key = 12
letters = []
crypt = []
choice = 0



while choice != 3:
    print("1.Kryptera")
    print("2.decryptera")
    choice = int(input()) 
    
    

    if choice ==1:
        
        for letter in word:
            letters.append(ord(letter) + key)
            
        print(letters)

    if choice ==2:

        for l in letters:
            crypt.append(chr(l-key))

        print(crypt)