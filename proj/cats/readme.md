## q1

题目有点迷惑，那个select函数是限制paragraphs的长度的，先用select筛选一遍paragraphs，返回true的放到新list里，再返回第k张。

## q2

全字母匹配 字符忽略 需要用到utils的前几个函数：换小写、去符号和拆分，然后返回一个匹配函数

## q3

注意一下计算规则，是按词来计算正确率，type输入多了都算错的

```
>>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
? 66.6
-- Not quite. Try again! --

? 100.0
-- OK! --

 # punctuation counts
 #好像不用太在意这个制表符，应该是split的时候去掉了
 
>>> a = 'sdsasd                 asda'
>>> a = split(a)
>>> a
['sdsasd', 'asda']
>>>
```

If both `typed` and `source` are empty, then the accuracy is 100.0. If `typed` is empty but `source` is not empty, then the accuracy is zero. If `typed` is not empty but `source` is empty, then the accuracy is zero

## q4

空格也算打字速度 直接取len就行了

## q5

返回第一个距离最小且不超过limit的

## q6

那个limit是让你提前return用的

从头到尾一个个改 不用dp啥的

## q7

就是暴搜 一个位置有三种可能：增，删和改、

一个递归树

记得考虑完全return情况

## q10

每个词只能用一次