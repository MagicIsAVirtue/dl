from core.advbase import *
from slot.a import *

def module():
    return Yue

class Yue(Adv):
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Breakfast_at_Valerios()
    conf['slots.burn.a'] = Primal_Crisis()+Elegant_Escort()
    conf['acl'] = """
        `dragon, s=2
        `s3, not self.s3_buff
        `s1
        `s2, x=4
        `fs, x=5
    """
    coab = ['Blade', 'Marth', 'Halloween_Mym']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
