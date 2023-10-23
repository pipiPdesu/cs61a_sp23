

# background

游戏规则

- 两个玩家，目标（默认）100分 
- 每回合选择至多十个骰子 
- sow sad 有一个是1那么这回合都是1
- pig tails  一个玩家可以选择不投骰子 这回合的分是2*abs（对手玩家总分数十位-个位）+1
- square swine 一回合结束如果一个玩家的分数是平方 会移动到下一个平方

文件

- `hog.py`: A starter implementation of Hog
- `dice.py`: Functions for making and rolling dice
- `hog_gui.py`: A graphical user interface (GUI) for Hog (updated)
- `ucb.py`: Utility functions for CS 61A
- `hog_ui.py`: A text-based user interface (UI) for Hog
- `ok`: CS 61A autograder
- `tests`: A directory of tests used by `ok`
- `gui_files`: A directory of various things used by the web GUI



主要修改hog ok评分python3 ok -q \[question number\] -i 01开始

```
 print("DEBUG:", x) 
```

来打印debug信息



竟然每道题都配了几个选择题来确保你理解问题

# q0

`dice.py`

`make_fair_dice`:传入面数，从[1，面数]随机选择一个

`make_test_dice`传入一个序列，然后循环遍历

疑点：第三个选择题应该`six_sided()` and `make fair dice`都对啊 没懂

总之定义好了six_sided()和four_sided()可以直接投骰子

# q1 

roll_dice

要点：即便发生了sow sad也不能直接返回1，否则随机数会乱掉没法做了。

选择题有点小坑 上当了 注意make_test_dice的调用次数，还有输入的答案是能roll到的最大值？没懂

# q2

注意对手分数只有个位和百位的情况 没什么大问题

# q3

没什么问题

# q4

我是硬编码的前20个平方数字 他也没给出数字范围难道用牛顿法逼近吗 

附一个方法：平方数的差是连续奇数，可以这样枚举

1 = 1 - 0
4 = 3 - 1
9 = 5 - 2
16 = 7 - 3
25 = 9 - 4
36 = 11 - 5
49 = 13 - 6
64 = 15 - 7

（的平方没加）

不过我觉得还是查表更方便，应该没有大数字

# q5

strategy0  strategy1 玩家的策略 给当前的分数和对手的分数来返回roll几个骰子  注意玩家1调用是（s1,s0）

update来更新分数

一直循环到游戏结束



# 中场休息

读一下`hog_ui.py` 

play_with定义了游戏方式，上面的函数就是把中间过程打印出来 get_int会等待输入，不得不说传函数还挺方便的

懒得下gui了 

# q6

高阶函数，要求读进来两个没用的参数

# q7 

意思就是说枚举所有可能情况，假如说存在两个情况返回的策略不同就返回false 

# q8

给make_average传的是roll的方式，这个可以是一个函数（original_function）

你要写一个高阶函数，来接受不定量的参数，返回进行多少次的平均值

# q9

注意当多个骰子相同时返回最小的那个

# q10 11

记得用以前的函数

12懒了不做了 也没什么验证的手段

就酱