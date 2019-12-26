#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 854

text = open('INPUT.TXT').readlines();

fact, cond = map(int, text[0].split(' '))
mode = text[1].rstrip('\n\r')

ans = None

if mode == 'freeze':
    if fact >= cond:
        ans = cond
    else:
        ans = fact

elif mode == 'heat':
    if fact <= cond:
        ans = cond
    else:
        ans = fact

elif mode == 'auto':
    ans = cond

else:
    ans = fact

file = open('OUTPUT.TXT', 'w')
file.write(str(ans) + '\n')
file.close()

