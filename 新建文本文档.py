f=open(r'D:\PYthon\练习\333.txt',encoding='utf=8')

boy=[]
girl=[]
count=1

for each_line in f:
    if each_line [:5]!='=====':
        (role,line_spoken)= each_line.split("：",1)
        if role =='我':
            boy.append(line_spoken)
        if role =="你":
            girl.append(line_spoken)
    else:
        file_name_boy='boy_'+str(count)+'.txt'
        file_name_girl='girl_'+str(count)+'.txt'

        boy_file= open(file_name_boy,'w')
        girl_file= open(file_name_girl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy=[]
        girl=[]
        count+=1

f.close()
