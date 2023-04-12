def cipher(string):
    return ''.join([chr(219 - ord(char)) if char.islower() else char for char in string])

message = 'I have an apple.'
encoded = cipher(message)
print('encoded:', encoded)
decoded = cipher(encoded)
print('decoded:', decoded)