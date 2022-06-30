text_list = ['x','xxx','xxxxx','xxxxxxx','']


g=lambda x: x+20
print(g(20))
f=lambda x:len(x)>=4

print(f("yo"))

print(list(filter(lambda x:len(x)>=4,text_list)))
