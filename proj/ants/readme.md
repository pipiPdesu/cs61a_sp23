植物大战僵尸

蜜蜂从某行进来 对付蚂蚁\前进  进家、吃掉蚁后

蚂蚁：收集食物、丢树叶  杀死所有蚂蚁

类好复杂啊 自己看给的关系图吧

# q1+2

- q1 没啥
- q2 就是说一块地皮吗 你必须要和自己家那个方向连着、家方向是exit 蜂箱是entrance
- 然后这就是个先有鸡后有蛋的问题 怎么创一个让exit和entrance连接 
- 刚创建place 入口默认none 然后上一个有了出口 就让入口和这个出口相连
- 给你exit 你要给exit的entrance赋值成self  self的exit是exit
- 就两行

# q3

遍历place找最近的蜜蜂  有一个标签判断是不是到蜂巢了

返回一个函数 这个函数的参数是一个list的蜜蜂

place的bee属性 是list

list为空返回none（为什么例题回答false而不是none啊）（哦）

注意不要动self.place 不要让蚂蚁跑蜂巢去了（

# q4

长距离蚂蚁：5米远才能达到（走五次entrance）并且攻击最远的那个

短距离蚂蚁 最多走三次entrance

为什么测试样例里会有第四种蚂蚁啊

lowernound和upperbound都是蚂蚁的attribute！！！

突然莫名其妙就过了 神秘

python可以用链式不等式

# q5

火蚂蚁-》会反伤的坚果

收到amount点伤害 对他在的区域所有蜜蜂反伤amount

最后死的时候还爆炸一下造成damage

要super调用失去生命函数 然后最后再死 要不然索引不到当前位置了

# q6

纯坚果

# q7

食人花

随机吃掉一个

不知道传进来的gamestate干啥用的

# q8



南瓜盆

### 8b 

就是说这个地方是先放植物还是先放瓜盆嘛 后放瓜盆就把位置上的植物改成瓜盆 一层层访问

# q9

可以放东西的地刺（）

# q10

水池都来了 进第三关了

# q11

好贵的水蚁

# q12

蚁后可以使得身后的攻击力翻倍（火一样、

重载掉血和移走函数

# q13

没有伤害的玉米投手？冰冻蘑菇？

停滞五回合  只有gamestate是even的时候不能动

这个五回合可以重置

SlowThrower should cause slowness on odd turns

