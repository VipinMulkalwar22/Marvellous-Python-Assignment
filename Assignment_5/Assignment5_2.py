def VowelConsonant(str,listvowelstr):
    
    # if(str == "a"  or str == "e" or str == "i" or str == "o" or str == "u"):
    #     print(str, "is a Vowel")
    # else:
    #     print(str, "is a Consonant")

    # for i in range(len(listvowelstr)):
    #     if(str == listvowelstr[i]):
    #         print(str, "is a Vowel")
    #         break

    if(str in listvowelstr):
        print(str,"is a Vowel")
    else:
        print(str,"is a Consonant")


def main():
    
    print("Enter the Character")
    str = input()
    vowelstr = "aeiouAEIOU"
    if (len(str) == 1 and str.isnumeric() != True):
        VowelConsonant(str,vowelstr)
    else:
        print("Enter the single Character")

if __name__ == "__main__":
    main()