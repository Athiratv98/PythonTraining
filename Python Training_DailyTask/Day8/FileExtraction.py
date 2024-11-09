"""
create csv file sample data
read csv line by line
split the csv into list
capture the required 
if condition is fulfill print

"""

def Print_Result(target_school):
    for line in file:
        #print(line)
        line=line[:-1:]
        linelist=line.split(",")
        #print(linelist)
        collegename=linelist[1]
        #print(collegename)
        if(collegename==target_school):
            print(line)
    

file=open(r'C:\Users\Administrator\Desktop\Python Training\Day8\Info.csv','r')
Print_Result("XC")
file.close()