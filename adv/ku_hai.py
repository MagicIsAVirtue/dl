from core.advbase import *
from module.x_alt import Fs_alt
import slot
from slot.a import *
from slot.d import *

def module():
    return Ku_Hai

class Ku_Hai(Adv):
    comment = 'c2+fs during s2'
    a1 = ('cd',0.15)
    a3 = ('cd',0.15, 'hp70')
    conf = {}
    # c1+fs_alt has higher dps and sp rate than c2+fs_alt with or without stellar show  (x)
    # c2+fs_alt fs can init quicker than c1+fs_alt
    conf['slots.a'] = Mega_Friends()+Primal_Crisis()
    conf['slots.poison.a'] = Mega_Friends()+The_Fires_of_Hate()
    conf['slots.d'] = AC011_Garland()
    conf['slots.poison.d'] = Pazuzu()
    conf['acl'] = '''
        `dragon.act("c3 s end"),fsc
        `s3, not self.s3_buff
        `s4
        `s2
        `s1, fsc
        `fs, x=2 and self.fs_alt.get()
        `fs, x=3
        '''
    coab = ['Blade','Dragonyule_Xainfried','Akasha']
    share = ['Curran']

    def prerun(self):
        self.fshit = 2
        conf_fs_alt = {
            'fs.dmg':0.83*2,
            'fs.sp' :330,
            'fs.charge': 2/60.0, # needs confirm
            'fs.startup':31/60.0,
            'fs.recovery':33/60.0,
            'fs.hit': 2,
            'x2fs.startup':16/60.0,
            'x2fs.recovery':33/60.0,
            'x3fs.startup':16/60.0,
            'x3fs.recovery':33/60.0,
        }
        if self.condition('big hitbox'):
            conf_fs_alt['fs.dmg'] += 0.83
            conf_fs_alt['fs.hit'] += 1
        self.fs_alt = Fs_alt(self, conf_fs_alt)
        self.apsaras_formation_buff = EffectBuff(
            'apsaras_formation', 10, 
            lambda: self.fs_alt.on(-1), 
            lambda: self.fs_alt.off()
        )

    def s2_proc(self, e):
        self.apsaras_formation_buff.on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)