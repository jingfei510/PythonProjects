from heroes import *
msg = '欢迎来到王者峡谷'
if __name__=="__main__":
    print(msg)
    milo=Hero('milo')
    boss=Element('boss')
    print(boss.hp)
    milo.hit(boss)
    print(boss.hp)
    boss.hit(milo)
    print(milo.hp)
