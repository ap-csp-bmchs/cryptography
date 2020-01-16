#define functions and variables
temp_ls = []
def str_br(x):
    global temp_ls
    for i in range(len(str(x))):
        temp_ls.append(str(x[i]))
str_t = ""
n_str = ""
key = 10
low_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap_l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num_r = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lp = False
def rot_ls(dire,lisv,charv,keyv):
    ls_pos = 0
    keyt = keyv
    n_pos = 0
    for i in range(len(lisv)):
        if charv == lisv[i]:
            ls_pos = i
    if keyt >= len(lisv):
        keyt = keyt - ((keyt//len(lisv))*len(lisv))
    if dire == 1:
        n_pos = ls_pos + keyt
        if n_pos > (len(lisv) - 1):
            n_pos = n_pos - len(lisv)
    elif dire == 2:
        n_pos = ls_pos - keyt
        if 0 > n_pos:
            n_pos = len(lisv) - abs(n_pos)
    else:
        return "ModeEror"
    return lisv[n_pos]
    
def scramble(dire, lisv, keyv):
    tv = []
    t_str = ""
    for i in range(len(lisv)):
        if lisv[i] != ' ' and lisv[i] != '!' and lisv[i] != '@' and lisv[i] != '#' and lisv[i] != '$' and lisv[i] != '%' and lisv[i] != '^' and lisv[i] != '&' and lisv[i] != '*' and lisv[i] != '(' and lisv[i] != ')' and lisv[i] != '_' and lisv[i] != '-' and lisv[i] != '+' and lisv[i] != '=' and lisv[i] != ':' and lisv[i] != ';' and lisv[i] != '"' and lisv[i] != "'" and lisv[i] != '<' and lisv[i] != ',' and lisv[i] != '>' and lisv[i] != '.' and lisv[i] != '?' and lisv[i] != '/':
            try:
                tv = int(lisv[i])
                t_str = t_str + str(rot_ls(dire, num_r, lisv[i], keyv))
            except ValueError:
                if lisv[i].isupper():
                    t_str = t_str + str(rot_ls(dire, cap_l, lisv[i], keyv))
                if lisv[i].islower():
                    t_str = t_str + str(rot_ls(dire, low_l, lisv[i], keyv))
        else:
            t_str = t_str + lisv[i]
    n_str = t_str
    t_str = ""
    return n_str
    
#ask for message
while True:
    pv = str(input("Would you like to decrypt or encrypt a message (yes or no): "))
    if pv == "yes":
        while True:
            if lp:
                pv2 = str(input("Would you like to continue (yes or no): "))
                if pv2 == "no":
                    break
                elif pv2 != "yes":
                    print ("Not a valid response.")
            while True:
                pv3 = str(input("Would you like to encrypt or decrypt (type encrypt or decrypt): "))
                if pv3 == "decrypt":
                    str_t = str(input("Enter a message to decrypt: "))
                    str_br(str_t)
                    while True:
                        try:
                            key = int(input("Enter a key (whole number): "))
                            break
                        except ValueError:
                            print ("Not a valid key.")
                    print (scramble(2, temp_ls, key))
                    n_str = ""
                    temp_ls = []
                    lp = True
                    break
                elif pv3 == "encrypt":
                    str_t = str(input("Enter a message to encrypt: "))
                    str_br(str_t)
                    while True:
                        try:
                            key = int(input("Enter a key (whole number): "))
                            break
                        except ValueError:
                            print ("Not a valid key.")
                    print (scramble(1, temp_ls, key))
                    n_str = ""
                    temp_ls = []
                    lp = True
                    break
                else:
                    print ("Not a valid response.")           
        break
    elif pv == "no":
        print ("ok")
        break
    else:
        print ("Not a valid response.")
    

