import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

lst = {'Name':[],'Course':[],'Branch':[],'Section':[],'Roll':[]}
ID=0
x=0
hidden={'Percentage':[]}
while x!=4:
    x=int(input('\t\t\t\t\t1:Create Student-ID\n\t\t\t\t\t2:Show List\n\t\t\t\t\t3:Particular Student\n\t\t\t\t\t\t4:Quit\n\t'))
    if(x==1):
        nme=input("Enter name: ")
        lst['Name'].append(nme.title())
        crse=input('Enter Course: ')
        lst['Course'].append(crse.title())
        brnch=input('Enter Branch: ')
        lst['Branch'].append(brnch.upper())
        sec=input('Enter section:  ')
        lst['Section'].append(sec.upper())
        rlno=input('Enter Roll no: ')
        lst['Roll'].append(rlno)
        f=int(input("Enter 1st semster percentage: "))
        hidden['Percentage'].append(f)
        s=int(input("Enter 2nd semster percentage: "))
        hidden['Percentage'].append(s)
        t=int(input("Enter 3rd semster percentage: "))
        hidden['Percentage'].append(t)
        fr=int(input("Enter 4th semster percentage: "))
        hidden['Percentage'].append(fr)
        ID+=4
    elif(x==2):
        df_list=pd.DataFrame(lst)
        print('\n\n\n')
        print(df_list)
    elif(x==3):
        y=int(input("Enter Index"))
        print(df_list[y:y+1])
        z=hidden['Percentage'][(y*4):((3+((y+1)-1)*4)+1)]
        h1={'Semester':['1st','2nd','3rd','4th'],'Percent':z}
        h2=pd.DataFrame(h1)
        print(h2)
        h2.set_index('Semester',inplace=True)
        h2.plot()
        plt.show()
    elif(x==4):
        break
    else:
        print('Enter Valid Input')