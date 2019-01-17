import adv_test
import adv

def module():
    return Luca

class Luca(adv.Adv):
    conf = {
        'condition':{
            'hp100':{
                "mod_a" : ('att' , 'passive' , 0.13) ,
                },
            'aff':{},
            }
        } 

    def init(this):
        this.dmg_make("o_paralysis",2.65)
        this.dmg_make("o_paralysis",2.65)
        this.dmg_make("o_paralysis",2.65)



if __name__ == '__main__':
    module().comment = 'paralysis 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)
    module().comment += '& spawn c1+fs'
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)
