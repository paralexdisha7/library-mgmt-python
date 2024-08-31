#************************************************************************************************************
#main_menu.py----------------------------------------------------------------------------------------------**
#************************************************************************************************************
import main_menu            
import admission
import student_data
import fee_details
import lib_details

while True:
    print("--------------------------------------------------------------")
    print("**************WELCOME TO SCHOOL MANAGEMENT SYSTEM***************")
    print("----------------------------------------------------------------")
    print("********************* ABCD SCHOOL MAIN MENU***********************")
    print("1.ADMISSION")
    print("2.STUDENT DATA")
    print("3.FEE DETAILS ")
    print("4.LIBRARY DETAILS")
    print("5.EXIT")
    print("--------------------------------------------------------------------")
    ch = int(input("ENTER YOUR CHOICE (1/2/3/4/5):"))
    if ch ==1:
        admission.ADM_MENU()
    elif ch ==2 :
        student_data.STU_MENU()
    elif ch==3 :
        fee_details.FEE_MENU()
    elif ch==4:
        lib_details.LIB_MENU()
    elif ch==5:
        break
    else :
        print("!!!!!!!!!!!!ERROR!!!!!!!!!!!INVALID CHOICE TRY AGAIN.......!!")
        conti=input("__________PRESS ANY KEY TO CONTINUE________")
#************************************************************************************************************
#admission.py----------------------------------------------------------------------------------------------**
#************************************************************************************************************
import main_menu
import admission
def ADM_MENU():
    while True :
        print("------------------------------------------------------------------")
        print("**********WELCOME TO SCHOOL MANAGEMENT SYSTEM *****************")
        print("=================================================================")
        print("*************************** ADMISSION MENU **********************")
        print("------------------------------------------------------------------")
        print("1.ADMISSION DETAILS")
        print("2.SHOW ADMISSION DETAILS")
        print("3.SEARCH ADMISSION DETAILS")
        print("4.DELETE ADMISSION DETAILS")
        print("5.UPDATE ADMISSION DETAILS")
        print("6.RETURN TO MAIN MENU....")
        print("-------------------------------------------------------------------")
        ch = int(input("ENTER YOUR CHOICE(1/2/3/4/5/6):"))

        if ch==1:
            admission.ADMIN_DETAILS()
        elif ch==2:
            admission.SHOW_ADMIN_DETAILS()
        elif ch==3:
            admission.SEARCH_ADMIN_DETAILS()
        elif ch==4:
            admission.DELETE_ADMIN_DETAILS()
        elif ch==5:
            admission.UPDATE_ADMIN_DETAILS()
        elif ch==6:
            return
        else :
            print("!!!!ERROR!!!!INVALID CHOICE TRY AGAIN....!!")
            conti=input("_______PRESS ANY KEY TO CONTINUE_____")
#*************************************************************************************************************
#student_data.py--------------------------------------------------------------------------------------------**
#*************************************************************************************************************
import main_menu
import student_data
def STU_MENU():
    while True :
        print("------------------------------------------------------------------")
        print("*******WELCOME TO SCHOOL MANAGEMENT SYSTEM ***********")
        print("==================================================================")
        print("***************** STUDENT DATA MENU  **************************")
        print("--------------------------------------------------------------------")
        print("1.ADD STUDENT RECORD")
        print("2.SHOW STUDENT DETAILS")
        print("3.SEARCH STUDENT DETAILS ")
        print("4.DELETE STUDENT RECORD")
        print("5.UPDATE STUDENT RECORD")
        print("6.RETURN TO MAIN MENU")
        print("---------------------------------------------------------------------")
        ch=int(input("ENTER YOUR CHOICE(1/2/3/4/5/6) :"))

        if ch==1:
            student_data.ADD_RECORDS()
        elif ch==2:
            student_data.SHOW_STU_DETAILS()
        elif ch==3:
            student_data.SEARCH_STU_DETAILS()
        elif ch==4:
            student_data.DELETE_STU_DETAILS()
        elif ch==5:
            student_data.UPDATE_STU_DETAILS()
        elif ch==6:
            return
        else :
            print("!!!!!!!!!!!!ERROR!!!!!!!!!!!INVALID CHOICE TRY AGAIN.......!!")
            conti=input("__________PRESS ANY KEY TO CONTINUE________")

#***********************************************************************************************************
#fee_details.py-------------------------------------------------------------------------------------------**
#***********************************************************************************************************
import main_menu
import fee_details
def FEE_MENU():
    while True:
        print("------------------------------------------------------------------")
        print("*************WELCOME TO SCHOOL MANAGEMENT SYSTEM *****************")
        print("------------------------------------------------------------------")
        print("******************** STUDENT'S FEES MENU***************************")
        print("------------------------------------------------------------------")
        print("1.FEE DEPOSIT")
        print("2.FEE DETAILS")
        print("3.RETURN TO MAIN MENU")
        print("------------------------------------------------------------------")
        ch=int(input("ENTER YOUR CHOICE(1/2/3):"))
        if ch==1:
            fee_details.FEE_DEPOSIT()
        elif ch==2:
            fee_details.FEE_DETAIL()
        elif ch==3:
            return
        else:
            print("!!!!!!!!!!!!ERROR!!!!!!!!!!!INVALID CHOICE TRY AGAIN.......!!")
            conti=input("__________PRESS ANY KEY TO CONTINUE________")
#***********************************************************************************************************          
#lib_details.py-------------------------------------------------------------------------------------------**
#***********************************************************************************************************
import main_menu
import lib_details
def LIB_MENU():
    print("--------------------------------------------------------------")
    print("*******WELCOME TO SCHOOL MANAGEMENT SYSTEM*****************")
    print("--------------------------------------------------------------")
    print("******************** LIBRARY MENU ***************************")
    print("--------------------------------------------------------------")
    print("1.ISSUE BOOK")
    print("2.RETURN BOOK")
    print("3.RETURN TO MAIN MENU...")
    print("--------------------------------------------------------------")
    ch=int(input("ENTER YOUR CHOICE(1/2/3):"))
    if ch==1:
        lib_details.ISSUE_BOOK()
    elif ch==2:
        lib_details.RETURN_BOOK()
    elif ch==3:
        return
    else :
        print("!!!!ERROR!!!!INVALID CHOICE TRY AGAIN....")
        cont = input("________PRESS ANY KEY TO RETURN TO MENU______")
#**************************************************************************************************************
#ADMIN_DETAILS.py--------------------------------------------------------------------------------------------**
#**************************************************************************************************************
import admission
import mysql.connector
def ADMIN_DETAILS():
    try:
        mycon=connection.MySQLConnection(user='root',password='smita1996',host='localost',database='schoolmanage')
        mycursor=mycon.cursor()
        adno=input("ENTER ADMISSION NUMBER:")
        rollno=int(input("ENTER ROLL NUMBER:"))
        sname=input("ENTER STUDENT NAME:")
        address=input("ENTER YOUR ADDRESS:")
        phoneno=input("ENTER VALID PHONE NUMBER:")
        cls=input("ENTER STUDENT'S CLASS:")

        query=("insert into admission values(%s,%d,%s,%s,%s)")
        record=(adno,rollno,sname,address,phoneno,cls)
        mycursor.execute(query,record)
        mycursor.close()
        mycon.close()
        print("RECORD HAS BEEN SAVED IN ADMISSION DATA TABLE...")
    except mysql.connector.error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("!!!ERROR!!!__SOMETING IS INVALID ....RECHECK USERNAME OR PASSWORD..")
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("ADMISSION /scoolmanage:DATABSE **DOES NOT EXIST....TRY ANOTHER DATABSE")
        else:
            print(err)
        con.close()
#*********************************************************************************************************************
#SHOW_ADMIN_DETAILS.py----------------------------------------------------------------------------------------------**
#*********************************************************************************************************************
from mysql.connector import errorcode
from mysql.connector import (connection)
import admission
def SHOW_ADMIN_DETAILS():
    try :
        mycon=connection.MySQLConnection(user='root',password='smita1996',host='localhost',database='schoolmanage')
        mycursor=mycon.cursor()
        query=("select * from admission")
        mycursor.execute(query)
        for(adno,rollno,sname,address,phoneno,cls)in cursor :
            print("==========================================================")
            print("ADMISSION NUMBER --> ",adno)
            print("ROLL NUMBER --> ",rollno)
            print("STUDENT NAME --> ",sname)
            print("ADDRESS --> ",address)
            print("PHONE NUMBER -->",phoneno)
            print("class --> ",cls)
    except mysql.connector.error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("!!!ERROR!!!__SOMETING IS INVALID ....RECHECK USERNAME OR PASSWORD..")
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("ADMISSION /scoolmanage:DATABSE **DOES NOT EXIST....TRY ANOTHER DATABSE")
        else:
            print(err)
        mycursor.close()
        con.close()
#***************************************************************************************************************************
#SEARCH_ADMIN_DETAILS.py--------------------------------------------------------------------------------------------------**
#***************************************************************************************************************************
from mysql.connector import errorcode
from mysql.connector import (connection)
import admission
def SEARCH_ADMIN_DETAILS():
    try:
        mycon=connection.MySQLConnection(user='root',password='smita1996',host='localhost',database='schoolmanage')
        temp_adno=input("ENTER ADMISSION NUMBER TO BE SEARCH :")
        mycursor=mycon.cursor()
        query=("select * from admission where temp_adno='%s'")
        rec_srch=(temp_adno,)
        mycursor.execute(query,rec_srch)
        for(adno,rollno,sname,address,phoneno,cls)in cursor :
            print("==========================================================")
            print("ADMISSION NUMBER --> ",adno)
            print("ROLL NUMBER --> ",rollno)
            print("STUDENT NAME --> ",sname)
            print("ADDRESS --> ",address)
            print("PHONE NUMBER -->",phoneno)
            print("class --> ",cls)
    except mysql.connector.error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("!!!ERROR!!!__SOMETING IS INVALID ....RECHECK USERNAME OR PASSWORD..")
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("ADMISSION /scoolmanage:DATABSE **DOES NOT EXIST....TRY ANOTHER DATABSE")
        else:
            print(err)
        mycursor.close()
        con.close()
#*******************************************************************************************************************************
#DELETE_ADMIN_DETAILS.py------------------------------------------------------------------------------------------------------**
#*******************************************************************************************************************************
from mysql.connector import errorcode
from mysql.connector import (connection)
import admission

def DELETE_ADMIN_DETAILS():
    try:
        mycon=connection.MySQLConnection(user='root',password='smita1996',host='localhost',database='schoolmanage')
        mycursor=mycon.cursor()
        temp_adno=input("ENTER ADMISSION NUMBER TO BE DELETED :")
        mycursor=mycon.cursor()
        query=("delete from admission where temp_adno='%s'")
        rec_srch=(temp_adno,)
        mycursor.execute(query,rec_srch)
        mycursor.close()
    except mysql.connector.error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("!!!ERROR!!!__SOMETING IS INVALID ....RECHECK USERNAME OR PASSWORD..")
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("ADMISSION /scoolmanage:DATABSE **DOES NOT EXIST....TRY ANOTHER DATABSE")
        else:
            print(err)
        mycursor.close()
        con.close()
#**********************************************************************************************************************************   
#UPDATE_ADMIN_DETAILS.py---------------------------------------------------------------------------------------------------------**       
#**********************************************************************************************************************************
from mysql.connector import errorcode
from mysql.connector import (connection)
import admission
def UPDATE_ADMIN_DETAILS():
    try:
        mycon=connection.MySQLConnection(user='root',password='smita1996',host='localhost',database='schoolmanage')
        temp_adno=input("ENTER ADMISSION NUMBER TO BE UPDATED :")
        query=("select * from admission where temp_adno='%s'")
        mycursor=mycon.cursor()
        rec_srch=(temp_adno,)
        print("************  INPUT NEW DATA ********")
        rollno=int(input("ENTER ROLL NUMBER:"))
        sname=input("ENTER STUDENT NAME:")
        address=input("ENTER YOUR ADDRESS:")
        phoneno=input("ENTER VALID PHONE NUMBER:")
        cls=input("ENTER STUDENT'S CLASS:")
        q=("update admission set rollno='%d', sname='%s',address='%s',phoneno='%s',cls='%s',where temp_adno='%s'")
        d=(rollno,sname,address,phoneno,cls)
        mycursor.execute(q,d)
        print("******************YOUR RECORD HAS BEEN UPDATED********************")
        
    except mysql.connector.error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("!!!ERROR!!!__SOMETING IS INVALID ....RECHECK USERNAME OR PASSWORD..")
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("ADMISSION /scoolmanage:DATABSE **DOES NOT EXIST....TRY ANOTHER DATABSE")
        else:
            print(err)
        mycursor.close()
        con.close()
        
        

            




    

        




        
        
