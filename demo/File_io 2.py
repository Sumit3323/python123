f=open('python/File_io 2.txt','r')


total_char=0
new_line=0
total_word=0


for i in f:
    # print(len(i))
    # print(i.split())
    new_line+=1
    total_char+=len(i)
    total_word+=len(i.split())

print(new_line) 
print(total_char) 
print(total_word)  
    





