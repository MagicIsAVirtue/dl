if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Zace

class Zace(Adv):
    a1 = ('s',0.2)
    conf = {}
    conf['slot.a'] = Jewels_of_the_Sun() + RR()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

