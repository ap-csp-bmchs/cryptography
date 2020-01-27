def getMode():
  print("Do you want to encrypt or decrypt a mesage?:")
  mode = input().lower()
  mode = mode[0]
  return mode

def getMessage():
  print("Enter your message:")
  message = input()
  return message

def getKey():
  print("Enter the key number from 1 to 9")
  key = int(input())
  if 1 <= key <= 9:
    return key

def getTranslatedMessage(mode, message, key):
  if mode == "d":
    key = -key
  translated = ''

  for symbol in message:
    if symbol.isalpha():
      num = ord(symbol)
      num += key

      if symbol.isupper():
        if num > ord('Z'):
          num -= 26
        elif num < ord('A'):
          num += 26
      if symbol.islower():
        if num > ord('z'):
          num -= 26
        if num < ord('a'):
          num += 26
      translated += chr(num)
    else:
      translated += symbol
  return translated


mode = getMode()
message = getMessage()
key = getKey()

print("Your translated text is: ")
print(getTranslatedMessage(mode, message, key))
