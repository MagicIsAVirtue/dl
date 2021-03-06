from core.advbase import *

def module():
    return Ramona

class Ramona(Adv):
    conf = {}
    conf['slots.a'] = ['Summer_Paladyns', 'Primal_Crisis']
    conf['acl'] = """
        `dragon(c3-s-s-end),s=1 and not s4.check()
        `s3, not buff(s3)
        `s2, s1.check()
        `s4, s=1
        `s1(all)
        """
    conf['coabs'] = ['Gala_Sarisse', 'Wand', 'Marth']
    conf['share'] = ['Summer_Patia']

    @allow_acl
    def s(self, n, s1_kind=None):
        if n == 1 and s1_kind == 'all':
            self.current_s['s1'] = s1_kind
        else:
            self.current_s['s1'] = 'default'
        return super().s(n)

    def s1_do_hit(self, t):
        # reeeeeee fix ur shit cykagames
        with KillerModifier('s1_killer', 'hit', 0.3, ['burn']):
            Selfbuff(f'{t.name}_crit', 0.10, 10, 'crit', 'chance').on()
            self.dmg_make(t.name, 2.93/(1 + self.sub_mod('s', 'buff')))
            self.add_combo(t.name)

    def s1_proc(self, e):
        if e.group != 'all':
            return
        for i in range(6):
            t = Timer(self.s1_do_hit)
            t.name = e.name
            t.on(i*0.5+0.5)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
