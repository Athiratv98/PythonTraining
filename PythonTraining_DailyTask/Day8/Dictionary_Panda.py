import pandas as pd
data={
    'name':'sfh'
}

choice=""
while(choice!='3'):
    print("1.Add to dictionary\n2.Print Dataframe\n3.Exit")
    print("Enter your choice")
    choice=input()
    if(choice=='1'):
        key1=input("Enter the key: : ")
        val1=input("Enter the value: ")
        if ',' in val1:
            val1=val1.split(',')
        data[key1]=val1
        
        print(data)
    elif(choice=='2'):
        dt=pd.DataFrame(data)

        print(dt)
    # elif(choice=='3'):
    #     break
    else:
        print("Invalid choice")
