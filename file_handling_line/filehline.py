with open('marks.txt','r') as f:
    with open('marksheet.txt','w') as m:
        i=0
        while True:
            i+=1
            l=f.readline()
            if not l:
                break
            m1=int(l.split(',')[0])
            m2=int(l.split(',')[1])
            m3=int(l.split(',')[2])
            line1=(f"Marks of Student {i} in Maths are {m1}\n")
            line2=(f"Marks of Student {i} in Maths are {m2}\n")
            line3=(f"Marks of Student {i} in Maths are {m3}\n\n")
            print (f"{line1}{line2}{line3}{l}")
            line=[line1,line2,line3]
            m.writelines(line)