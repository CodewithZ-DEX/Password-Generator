import string
import random

a = string.ascii_letters
b = string.ascii_lowercase
c = string.octdigits
d = string.punctuation
p = []
length = int(input("enter password length"))
p.extend(list(a))
p.extend(list(b))
p.extend(list(c))
p.extend(list(d))
random.shuffle(p)
print("Your password is:")
print("".join(p[0:length]))
