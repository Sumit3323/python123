
# File Io

# MOde
"""
1.'r' = File read only
2.'w' = File read write
3.'a' = Append The Text
4.'+' =read aaaaaand write both
5.'r+' = file read and write both
6.'w+' = file read and write both
7.'t'  =Text Mode
8.'b' =binary Mode

"""

# f=open('python/file_io.txt','r')
# print(f.read())
# f.close()


# f1=open('python/file_io.txt2','w')
# f1.write('Hello How are you')
# print(f1)
# f1.close()

# f=open('python/file_io.txt2','a')
# f.write('\nI am python developer')
# print(f)
# f.close()

# f=open('python/file_io.txt','r+')
# # print(f.read())
# f.write('\n Html\n Css \n Javascript \n Pythonnnnnnn')
# f.write('i am work now k;kljlhlj;;lgu')
# print(f.read())
# f.close()



with open('python/file_io.txt5','w') as fllee:
    # print(fle.read())
    print(fllee.write('This'))
