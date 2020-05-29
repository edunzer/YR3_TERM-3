## FILE ENCRYPTION AND DECRYPTION

code = {"A":"T","a":"T","B":"D","b":"D","C":"L","c":"L","D":"O","d":"O","E":"F","e":"F","F":"A","f":"A","G":"G","g":"G","H":"J","h":"J","I":"K","i":"K","J":"R","j":"R","K":"I","k":"I","L":"C","l":"C","M":"V","m":"V","N":"P","n":"P","O":"W","o":"W","P":"U","p":"U","Q":"X","q":"X","R":"Y","r":"Y","S":"B","s":"B","T":"E","t":"E","U":"Z","u":"Z","V":"Q","v":"Q","W":"S","w":"S","X":"N","x":"N","Y":"M","y":"M","Z":"H","z":"H"}

def encrypt(sentence, code):
    result = ''
    for letter in sentence:
        if letter in code:
            result = result + code[letter]
        else:
            result = result + letter
    return result
user_input = input('Please enter your sentence: ')

print(encrypt(user_input, code))
