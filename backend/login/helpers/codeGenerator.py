import random
source = "0123456789zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP"

def generate_code():
    return ''.join([random.choice(source) for i in range(6)])


for i in range(50):
    print(generate_code())