# -*-coding:utf-8-*-
"""
记录一下deque的方法
append()
appendleft()
clear() 
count()
extend()
extendleft()
maxlen()
pop()
popleft()
remove()
reverse()
rotate() 旋转 这个比较有意思，deque = [1,2,3,4] deque.rotate(1)->[4,1,2,3]
由两端删除，追加元素时间复杂度O(1),区别于列表，在列表开头插入或删除元素时间复杂度是O(N)
"""

from collections import deque
test_deque = deque(maxlen=4)
test_deque.append(1)

test_deque.appendleft(2)
print test_deque
#test_deque.clear()
print test_deque.count(1)

