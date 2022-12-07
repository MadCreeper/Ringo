import random
source = "0123456789zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP"

def generateCode():
    return ''.join([random.choice(source) for i in range(6)])
