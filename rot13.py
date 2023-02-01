def rot13(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cipher_message=""
    capslock = False
    
    for char in message:
        if char.islower():
            capslock = False
        else:
            char=char.lower()
            capslock = True

        position = alpha.find(char)
        
        if position == -1:
            cipher_message=cipher_message+char
        else:
                 
            i = position
            position = position + 13
            if position < 26:            
                if capslock == False:
                    cipher_message=cipher_message+alpha[position]
                else:
                    cipher_message=cipher_message+alpha[position].upper()
            else:
               restartedPosition = position - 26
               if capslock == False:
                cipher_message=cipher_message+alpha[restartedPosition]
               else:
                cipher_message=cipher_message+(alpha[restartedPosition]).upper()        
    print(cipher_message)
    return cipher_message

   
   

rot13('Mensagem secreta #1')