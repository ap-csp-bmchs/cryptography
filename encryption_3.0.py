alphabet = 'abcdefghijklmnopqrstuvwxyz'
def getMode():
    print("Would you like to encrypt or decrypt a message? ")
    mode = input().lower()
    mode = mode[0]
    return mode

def getKey():
    print("Enter a key from 1-9 ")
    key = int(input())
    if 1 <= key <= 9:
        return key

#def getTranslatedMessage(mode, message, key):
    #if mode == "d":
        #key = -key
    #translated = ''
    

newMessage = ''

message = input('Enter a message with lowercase letters: ')
key = getKey()


for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character




print('Your new message is', newMessage)

    


