class Hero:

    def __init__(self,name='player1',hp=100,act=10):
        self.name=name
        self.hp=hp
        self.act=act
        print("英雄%s诞生！"%self.name)

    def hit(self,name):
        name.hp -= self.act

    def blood(self):
        pass


class Element:
    def __init__(self,name='boss',hp=1000,act=20):
        self.name=name
        self.hp=hp
        self.act=act
        print("BOSS%s诞生！"%self.name)

    def hit(self,name):
        name.hp -= self.act

    def blood(self):
        pass

if __name__=="__main__":
    milo=Hero('milo')
    boss=Element('boss')
    print(boss.hp)
    milo.hit(boss)
    print(boss.hp)
    boss.hit(milo)
    print(milo.hp)





