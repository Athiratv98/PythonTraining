
def Print_Result(school):
    count={}
    for line in file:
        #print(line)
        line=line[:-1:]
        linelist=line.split(",")
        school=linelist[1]
        #print(linelist)
        if(school not in count):
            count[school]=1
        else:
            count[school]+=1
    return count
    

file=open(r'C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\Day8\Info.csv','r')
print(Print_Result("BU"))
file.close()