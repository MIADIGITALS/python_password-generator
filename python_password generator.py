#PYTHON PASSWORD GENERATOR
import random
lower='abcdefghijklmnopqrstuvwxwz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
symbols='._-@*%$!{}[]'
all=lower+upper+number+symbols
length=int(input('WHAT IS THE LENGTH OF PASSWORD YOU NEED : '))
password=''.join(random.sample(all,length))
print(password)