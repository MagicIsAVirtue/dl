if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Rodrigo

class Rodrigo(adv.Adv):
    a1 = ('a',0.08,'hp70')
    conf = {}
    conf['slot.a'] = TSO()+BN()
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+JotS()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

