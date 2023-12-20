f=open('myfile.txt','r')
# print(f)
text=f.read()
print(text)
f.close()

with open('myfile.txt','a') as f:
    f.write('Hy in With')
