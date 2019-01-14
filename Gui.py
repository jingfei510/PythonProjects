import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏')    #msgbox其实还可以设置第二个参数，
    #第二个参数代表标题栏上面的文字，就如下面那个msgbox里面的 '结果'


    msg='请问你希望在鱼C工作室学习到什么知识呢？'
    title='小游戏互动'
    choices=['谈恋爱','编程','OOXX','琴棋书画']


    choice=g.choicebox(msg,title,choices)     #还没看文档，不过这个choicebox这个函数应该是可以接受好几个参数的，包括顶栏的标题，选项内容，已经主语句


    g.msgbox('你的选择是:' + str(choice),'结果')


    msg ='你希望重新开始小游戏吗？'
    title='请选择'


    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
