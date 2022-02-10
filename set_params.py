import os

print(os.getcwd())
print(os.chdir(r'C:\Users\03063Y744\Downloads\python_test\string_func\leetcode'))

with open('env.txt','r') as f:
    for each in f.readlines():
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print(each)
        os.environ[each.split('=',1)[0]] = each.split('=',1)[1].replace("\n",'')
        print(os.environ[each.split('=',1)[0]])
        print( each.split('=',1)[1].replace("\n",''))
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        