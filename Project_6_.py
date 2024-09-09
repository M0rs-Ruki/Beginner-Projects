#Rendom password

import random
import string

pass_len = 8
chval = string.ascii_letters + string.digits + string.punctuation

password = ''
for x in range(pass_len):
    password +=(random.choice(chval))

print("your passwprd is =", password)
