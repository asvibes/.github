ch=input("Enter your character")

if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("Alphabet")
elif ch>='0' and ch<='9':
    print("Digit")
else:
    print("Character")
