from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

from tkcalendar import DateEntry
from datetime import datetime
from datetime import date
import csv

today = date.today()
fields = ['TIMESTAMP','FIRSTNAME','LASTNAME','BRIDDATY','AGE','HEIGHT','WEIGHT','BMI','CONSIDER']
########################### FUNCTION #######################################

def WriteCsv(detaillist) :
     with open('data.csv','a',encoding='utf-8',newline='') as file:
          fw = csv.writer(file)
          fw.writerow(detaillist)

def ReadCsv():
     with open('data.csv',encoding='utf-8',newline='') as file:
          fr = csv.reader(file)
          data = list(fr)

     return data

     

def ShowMessagebox(titlems,message) : 
    messagebox.showinfo(titlems,message)

def showData() : 
     #data = 'name : {} {}\nbirthday : {}\nheight : {}\nweight :{}'.format(entry_firstname.get(),entry_lastname.get(),entry_bdate.get_date(),entry_height.get(),entry_weight.get())
     data = StringVar() 
     ShowMessagebox('show data', data.get())

def SaveDataToList() :
        if (CheckData()) : 
            bmi, msage = CalBmi()
            data = []
            data.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            data.append(entry_firstname.get())
            data.append(entry_lastname.get())
            data.append(entry_bdate.get_date())
            data.append(CalAge())
            data.append(entry_height.get())
            data.append(entry_weight.get())
            data.append(bmi)
            data.append(msage)
            
            print('Data in List\n')
            for x in data : 
                print(str(x)+'\n')    
            print('-------------------------------------\n\n')
            

def CalAge() : 
        bdate = entry_bdate.get_date()
        age = today.year - bdate.year -  ((today.month, today.day) < (bdate.month, bdate.day))
        return age

def CheckData() : 
    if CheckNullEntry() and ChekNum(entry_height.get(),entry_weight.get()) : 
        print('CheckData : TRUE')
        return TRUE
    
    print('CheckData : FALSE')
    return FALSE

def CheckNullEntry() : 
    runnig = TRUE
    if entry_firstname.index("end") == 0 : 
        ShowMessagebox('Error', 'plase input firstname')
        runnig = FALSE
    if entry_lastname.index("end") == 0 : 
        ShowMessagebox('Error', 'plase input lastname')
        runnig = FALSE
    if entry_height.index("end") == 0 : 
        ShowMessagebox('Error', 'plase input height')
        runnig = FALSE
    if entry_weight.index("end") == 0 : 
        ShowMessagebox('Error', 'plase input weight')
        runnig = FALSE

    if runnig :
        #print('CheckNullEntry : TRUE') 
        return TRUE
    
    #print('CheckNullEntry : FALSE')
    return FALSE


def ChekNum(h,w) : 
       try : 
        float(h) and float(w)
       except : 
        ShowMessagebox('Error', 'plase input number')
        return FALSE

       if float(h) < 0 or float(w) < 0 :
        ShowMessagebox('Error', 'plase input more than 0')
        return FALSE
       elif float(h) > 999 or float(w) > 999:
        ShowMessagebox('Error', 'limit 999')
        return FALSE

       return TRUE
       
def CalBmi() : 
    height, weight = float(entry_height.get()),float(entry_weight.get())
    bmi = round(weight/pow((height/100),2),2)

    if bmi > 30 : 
        return bmi, 'อ้วนมาก'
    elif bmi > 25 : 
        return bmi, 'อ้วน'
    elif bmi > 23 : 
        return bmi, 'ท้วม'
    elif bmi > 18.50 : 
        return bmi, 'น้ำหนักปกติ'
    else : 
        return bmi, 'น้ำหนักน้อยกว่ามาตรฐาน'

'''
    if bmi > 30 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ อ้วนมาก'.format(str(BMI))
    elif bmi > 25 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ อ้วน'.format(str(bmi))
    elif bmi > 23 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ ท้วม'.format(str(bmi))
    elif bmi > 18.50 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ น้ำหนักปกติ'.format(str(bmi))
    else : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ น้ำหนักน้อยกว่ามาตรฐาน'.format(str(bmi))
    
    ShowMessagebox('Result',message)
'''

#######################################################################################################################################################

GUI = Tk()
GUI.title('คำนวน BMI')
GUI.geometry('720x480')

text_header = Label(GUI, text='คำนวน BMI',font=('Angsana New',30),fg='green')
text_header.grid(row=0, column=0)

Label(GUI,text='firstname : ',font=('Angsana New',18)).grid(row=1, column=0)
Label(GUI,text='lastname : ',font=('Angsana New',18)).grid(row=1, column=2)
Label(GUI,text='brittany : ',font=('Angsana New',18)).grid(row=2, column=0)
Label(GUI,text='height (cm) : ',font=('Angsana New',18)).grid(row=3, column=0)
Label(GUI,text='weight (Kg) :',font=('Angsana New',18)).grid(row=4, column=0)


entry_firstname = Entry(GUI,font=('Angsana New',18))
entry_lastname = Entry(GUI,font=('Angsana New',18))
entry_bdate = DateEntry(GUI,locale='en_US', date_pattern='yyyy/MM/dd',maxdate=today)
entry_height = Entry(GUI,font=('Angsana New',18))
entry_weight = Entry(GUI,font=('Angsana New',18))

entry_firstname.grid(row=1, column=1)
entry_lastname.grid(row=1, column=3)
entry_bdate.grid(row=2, column=1,padx=15)
entry_height.grid(row=3, column=1)
entry_weight.grid(row=4, column=1)



button_cal =  Button(GUI,text='Calculate', command=SaveDataToList, font=('Angsana New',16)).grid(
    row=6,column=0,sticky='ew',pady=4)

button_exit = Button(GUI,text='Exit', command=GUI.quit, font=('Angsana New',16)).grid(
    row=6,column=1,sticky='ew',pady=4)

GUI.mainloop()