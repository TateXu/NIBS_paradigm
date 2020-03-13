import random
import string

def randomString(stringLength=3):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))


freq = [0, 4, 10, 40]

for i in range(10):
    freq = [0, 4, 10, 40]
    identifier = randomString(stringLength=3)
    random.shuffle(freq)

    print(identifier )
    print(''.join(str(freq)))


"""

ZWS
[10, 0, 40, 4]
NUK
[40, 4, 10, 0]
OSA
[0, 40, 10, 4]
KNL
[4, 10, 40, 0]
ZYC
[40, 10, 4, 0]
CCH
[0, 4, 10, 40]
DSW
[10, 0, 40, 4]
VQT
[4, 0, 40, 10]
BXB
[0, 10, 40, 4]
BMC
[0, 40, 4, 10]

"""