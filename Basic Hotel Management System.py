# HOTEL MANAGEMENT SYSTEM


import mysql.connector
import datetime
import sys
import csv

db = mysql.connector.connect(host = "localhost", user = "root", password = "xxxxxxxx")
cr = db.cursor()
cr.execute("CREATE DATABASE IF NOT EXISTS HOTEL_MANAGEMENT")
cr.execute("USE HOTEL_MANAGEMENT")
cr.execute('''CREATE TABLE IF NOT EXISTS RECORDS(NAME char(50), PHONE_NUMBER char(10), EMAIL_ID char(50),
                    PASSWORD char(50))''')


acc = c = st = na = 0


print('''
                                                                                   *~*~*~*~*~*~*~*~*~*~*~*~*                                                                        
                                                                                   *   HOTEL THE ROYALE    *
                                                                                   *~*~*~*~*~*~*~*~*~*~*~*~*
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                            
                                                                        ~*~*~*~*~*~  WELCOME TO THE ROYALE  ~*~*~*~*~*~ \n\n ''')

print("DO YOU WANT TO CREATE A NEW ACCOUNT OR ALREADY HAVE AN ACCOUNT ?")


while acc != 1 and acc != 2 and acc != 3 :
       print('''
                PRESS '1' ----->  CREATE A NEW ACCOUNT (SIGN-UP)
                
                PRESS '2' ----->  ALREADY HAVE AN ACCOUNT (LOG-IN)
                
                PRESS '3' ----->  EXIT \n ''')
       acc = int(input("Enter your choice : "))
       if acc != 1 and acc != 2 and acc != 3 :
              print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

            
def ph_valid() :

       c = 0
       while c != 10 :
             c = 0
             ph = int(input("Enter your PHONE NUMBER : "))
             st = ph
             while st > 0 :
                   c = c + 1
                   st = (int)(st / 10)
             if c != 10 :
                   print("PLEASE ENTER A 10-DIGIT PHONE NUMBER !!! \n ")
       return ph           
       
      
def sign_up() :

     global ph1
     
     print("\n                SIGN-UP PORTAL  \n ")
     n1 = input("Enter your NAME : ")
     print()
     ph1 = ph_valid()

     na = 0
     cr.execute("SELECT PHONE_NUMBER FROM RECORDS")
     st = cr.fetchall()
     c = cr.rowcount
     if c > 0 :
           c = 0
           while c == 0 :
                 for i in st :
                       if i[0] == (str)(ph1) :
                             print("PHONE NUMBER ALREADY REGISTERED !!! \n ")
                             print("                PRESS '1' ----->  REGISTER WITH A DIFFERENT PHONE NUMBER \n ")
                             print("                PRESS '2' ----->  LOG-IN (IF YOU ALREADY HAVE AN ACCOUNT) \n ")
                             print("                PRESS '3' ----->  EXIT \n ")
                             na = 0
                             while na != 1 and na != 2 and na != 3 :
                                  na = int(input("Enter your choice : "))
                                  if na != 1 and na != 2 and na != 3 :
                                         print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!! \n ")
                             if na == 1 :
                                    print()
                                    ph1 = ph_valid()
                                    break
                             if na == 2 :
                                    log_in()
                             if na == 3 :
                                    print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!!")
                                    sys.exit(0)
                       c = 1

     if na != 2 :
            print()
            c = 0
            while c != 2 :
                  c = 0
                  em1 = input("Enter your E-MAIL ID : ")
                  for i in em1 :
                        if i == "@" or i == "." :
                              c = c + 1
                  if c < 2 :
                        print("PLEASE ENTER A VALID E-MAIL ID !!! \n ")
            
            print()           
            c = 0
            while c < 6 :
                  pswd1 = input("Enter a STRONG PASSWORD (MINIMUM 6 CHARACTERS) : ")
                  c = len(pswd1)
                  if c < 6 :
                        print("PLEASE ENTER A STRONG PASSWORD (MINIMUM 6 CHARACTERS) !!! \n ")
                        
            cr.execute("INSERT INTO RECORDS VALUES('" + n1 + "','" + (str)(ph1) + "','" + em1 + "','" + pswd1 + "')")
            db.commit()
            print("\nACCOUNT CREATED SUCCESSFULLY !!! YOU HAVE BEEN LOGGED-IN !!!")


def log_in() :
       
      global ph1
      
      print("\n                LOG-IN PORTAL  \n ")
      ph1 = ph_valid()
      
      na = 0
      cr.execute("SELECT PHONE_NUMBER FROM RECORDS")
      st = cr.fetchall()
      c = cr.rowcount
      if c == 0 :
            print("NO SUCH PHONE NUMBER FOUND !!! PLEASE CREATE A NEW ACCOUNT !!! \n ")
            print("                PRESS '1' ----->  CREATE A NEW ACCOUNT (SIGN-UP) \n ")
            print("                PRESS '2' ----->  EXIT \n ")
            na = 0
            while na != 1 and na != 2 :
                  na = int(input("Enter your choice : "))
                  if na != 1 and na != 2 :
                        print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!! \n ")
            if na == 1 :
                  sign_up()
            if na == 2 :
                   print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!!")
                   sys.exit(0)

      if na != 1 :      
             if c > 0 :
                   c = 0
                   while c < 3 :
                          for i in st :
                                 if i[0] == (str)(ph1) :
                                        c = 4
                                        break
                          c = c + 1
                          if c < 3 :
                                 print("NO SUCH PHONE NUMBER FOUND !!! PLEASE ENTER PHONE NUMBER AGAIN !!! \n ")
                                 ph1 = ph_valid()           
                   if c == 3 :
                            print("NO SUCH PHONE NUMBER FOUND !!! NO MORE TRIES LEFT !!! \n ")
                            print("                PRESS '1' ----->  CREATE A NEW ACCOUNT (SIGN-UP) \n ")
                            print("                PRESS '2' ----->  EXIT \n ")
                            na = 0
                            while na != 1 and na != 2 :
                                   na = int(input("Enter your choice : "))
                                   if na != 1 and na != 2 :
                                          print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!! \n ")
                            if na == 1 :
                                   sign_up()
                            if na == 2 :
                                   print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!!")
                                   sys.exit(0)

      if na != 1 :                 
             print()
             c = 0
             while c < 3 :
                   pswd2 = input("Enter your PASSWORD : ")
                   cr.execute("SELECT PASSWORD FROM RECORDS WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
                   st = cr.fetchall()
                   if st[0][0] == pswd2 :
                         c = 4
                   c = c + 1
                   if c < 3 :
                         print("PASSWORD NOT MATCHING !!! PLEASE ENTER PASSWORD AGAIN !!! \n ")
             if c == 3 :
                    print("PASSWORD NOT MATCHING !!! NO MORE TRIES LEFT !!! \n ")
                    print("                PRESS '1' ----->  CREATE A NEW ACCOUNT (SIGN-UP) \n ")
                    print("                PRESS '2' ----->  EXIT \n ")
                    na = 0
                    while na != 1 and na != 2 :
                           na = int(input("Enter your choice : "))
                           if na != 1 and na != 2 :
                                  print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!! \n ")
                    if na == 1 :
                           sign_up()
                    if na == 2 :
                           print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!!")
                           sys.exit(0)
              
             print("\nYOU HAVE BEEN LOGGED-IN !!!")


if acc == 1 :
      sign_up()

if acc == 2 :
       log_in()

if acc == 3 :
       print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!!")
       sys.exit(0)




def find_date(x, y) :

       p = y.day - 1
       q = y.month
       r = y.year
       while x != 0 :
              if q in [1, 3, 5, 7, 8, 10, 12] :
                     while p < 31 and x != 0 :
                            p = p + 1
                            x = x - 1
                     if p == 31 and q == 12 and x != 0 :
                           r = r + 1
                           p = 0
                           q = 1
                     elif p == 31 and x != 0 :
                           p = 0
                           q = q + 1
              elif q in [4, 6, 9, 11] :
                     while p < 30 and x != 0 :
                            p = p + 1
                            x = x - 1
                     if p == 30 and x != 0  :
                           p = 0
                           q = q + 1
              elif q == 2 :
                     if (r % 4 == 0 and r % 100 != 0) or r % 400 == 0 :
                            while p < 29 and x != 0 :
                                   p = p + 1
                                   x = x - 1
                            if p == 29 and x != 0 :
                                   p = 0
                                   q = q + 1
                     else :
                            while p < 28 and x != 0 :
                                   p = p + 1
                                   x = x - 1
                            if p == 28 and x != 0 :
                                   p = 0
                                   q = q + 1
                                   
       return(datetime.date(day = p, month = q, year = r))      

                            
def card_valid(cval) :

       k = 0
       m = 0
       cval = (str)(cval)
       if len(cval) < 13 or len(cval) > 19 :
              return False
       s = cval[-2 : : -2]
       for i in s : 
              k = k + (((int)(i) * 2) % 10) + (int)(((int)(i) * 2) / 10)
       s = cval[-1 : : -2]
       for i in s :
              m = m + (int)(i)
       if (k + m) % 10 == 0 :
              return True
       else :
              return False


def date_make(dmk) :

       k = dmk.split("-")
       if len(k) == 1 :
              dmk = dmk.split(":")
              return (datetime.time(hour = (int)(dmk[0]), minute = (int)(dmk[1])))
       return (datetime.date(year = (int)(k[0]), month = (int)(k[1]), day = (int)(k[2])))
       

def bill(bkid) :
       
       a = {}
       with open("ROOMS_SECTION_DATA.csv", "a+", newline = '') as fh :
              fh.seek(0)
              bpr = csv.DictReader(fh)
              for i in bpr :
                     if i["BK_ID"] == (str)(bkid) :
                            a = i
                            break
                     
              print("\n        ~*~*~*~ INVOICE ~*~*~*~        \n")
              print("DATE :", date_make(a["BK_DATE"]).strftime("%a %d %b %Y"))
              print("TIME :", date_make(a["BK_TIME"]).strftime("%I:%M %p"))
              print("\nBOOKING ID :", a["BK_ID"])
              print("\nNAME :", a["NAME"])
              print("PHONE NUMBER :", a["PH_NO"])
              print("E-MAIL ID :", a["EMAIL_ID"])
              print("\nROOM TYPE :", a["RM_TYPE"])
              print("RATE (PER DAY) :", a["RATE_PD"])
              print("NUMBER OF ROOMS :", a["NO_RM"])
              print("\nCHECK-IN DATE :", date_make(a["CHKIN_DT"]).strftime("%a %d %b %Y"))
              print("CHECK-OUT DATE :", date_make(a["CHKOUT_DT"]).strftime("%a %d %b %Y"))
              print("NUMBER OF DAYS :", a["NO_DAYS"])
              print("\nTOTAL AMOUNT :", a["TOTAL_AMT"])
              print("PAYMENT METHOD :", a["PAY_MTD"])
              print()


def cancel(bkid) :
       
       md = []
       with open("ROOMS_SECTION_DATA.csv", "a+", newline = '') as fh :
              fh.seek(0)
              bpr = csv.DictReader(fh)
              for i in bpr :
                     if i["BK_ID"] != (str)(bkid) :
                            md.append(i)

       with open("ROOMS_SECTION_DATA.csv", "w", newline = '') as fh :
              bcan = csv.DictWriter(fh, fieldnames = ["BK_ID", "NAME", "PH_NO", "EMAIL_ID", "PASSWORD", "RM_TYPE","RATE_PD",
                                                                           "NO_RM", "CHKIN_DT", "CHKOUT_DT", "NO_DAYS", "TOTAL_AMT", "PAY_MTD",
                                                                           "BK_DATE", "BK_TIME"])
              bcan.writeheader()
              bcan.writerows(md)


while True :
       
       print("\nCHOOSE WHAT YOU WANT TO DO NEXT : ")

       acc = 0
       while acc != 1 and acc != 2 and acc != 3 and acc != 4 and acc != 5 and acc != 6 :
              print('''
                PRESS '1' ----->  ROOMS SECTION
                
                PRESS '2' ----->  CHECK YOUR CURRENT BOOKING
                
                PRESS '3' ----->  CANCEL A BOOKING
                
                PRESS '4' ----->  CHANGE YOUR ACCOUNT DETAILS
                
                PRESS '5' ----->  DELETE YOUR ACCOUNT
                
                PRESS '6' ----->  EXIT (LOG-OUT) \n ''')
              acc = int(input("Enter your choice : "))
              if acc != 1 and acc != 2 and acc != 3 and acc != 4 and acc != 5 and acc != 6 :
                     print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

       
       def rooms() :
              
              rt = ["SINGLE ROOM", "DOUBLE ROOM", "TRIPLE ROOM", "QUAD ROOM", "DELUXE ROOM" ]
              rate = ["Rs. 800", "Rs. 1400", "Rs. 2000", "Rs. 2600", "Rs. 3200"]

              print('''
                                                                   *~*~*~*~*~*~*~*~*~*~*~*                                                                          
                                                                   *   ROOMS SECTION   *
                                                                   *~*~*~*~*~*~*~*~*~*~*~*  \n ''')    
              print("CHOOSE THE TYPE OF ROOM YOU WANT TO BOOK : ")

              c = 0
              while c != 1 and c != 2 and c != 3 and c != 4 and c != 5 and c != 6 :              
                     print('''
                  \t\t..ROOM TYPE\t\tRATE (PER DAY)\t\tDESCRIPTION

                PRESS '1' ----->  SINGLE ROOM\t\tRs. 800\t\t\tROOM FOR 1 PERSON  
                                                                                                                                                                      
                PRESS '2' ----->  DOUBLE ROOM\t\tRs. 1400\t\tROOM FOR 2 PERSONS

                PRESS '3' ----->  TRIPLE ROOM\t\tRs. 2000\t\tROOM FOR 3 PERSONS

                PRESS '4' ----->  QUAD ROOM\t\tRs. 2600\t\tROOM FOR 4 PERSONS

                PRESS '5' ----->  SUITE ROOM\t\tRs. 3200\t\tROOM FOR 5 PERSONS

                PRESS '6' ----->  EXIT (LOG-OUT) \n ''')
                     
                     c = int(input("Enter your choice : "))
                     if c != 1 and c != 2 and c != 3 and c != 4 and c != 5 and c != 6 :
                            print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

              if c == 6 :
                     print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!! YOU HAVE BEEN LOGGED-OUT !!!")
                     sys.exit(0)

              nr = 0
              while nr < 1 or nr > 10 :
                     nr = int(input("\nEnter the NUMBER OF ROOMS you want to book : "))
                     if nr < 1 or nr > 10 :
                            print("PLEASE ENTER A VALID NUMBER OF ROOMS !!! YOU CAN BOOK A MAXIMUM OF 10 ROOMS AT A TIME !!!")

              date_now = datetime.datetime.now().date()

              while True :
                     na = 0
                     print("\nEnter the DATE you want to CHECK-IN (as prompted below in DD-MM-YYYY format) : ")
                     dd = int(input("Enter the DAY : "))
                     mm = int(input("Enter the MONTH : "))
                     yyyy = int(input("Enter the YEAR : "))
                     
                     if yyyy < date_now.year or yyyy > (date_now.year + 1) :
                            print("\nINVALID DATE !!! PLEASE CHECK THE RANGE OF YEAR (RANGE OF YEAR - ", date_now.year, " to ",
                                    (date_now.year + 1), ") !!!", sep = "")
                            na = 1

                     elif mm in [1, 3, 5, 7, 8, 10, 12] :
                            if dd < 1 or dd > 31 :
                                print("\nINVALID DATE !!! PLEASE CHECK THE RANGE OF DAY (RANGE OF DAY FOR THAT MONTH - 1 to 31) !!!")
                                na = 1

                     elif mm in [4, 6, 9, 11] :
                            if dd < 1 or dd > 30 :
                                print("\nINVALID DATE !!! PLEASE CHECK THE RANGE OF DAY (RANGE OF DAY FOR THAT MONTH - 1 to 30) !!!")
                                na = 1 

                     elif mm == 2 :
                            if (yyyy % 4 == 0 and yyyy % 100 != 0) or yyyy % 400 == 0 :
                                   if dd < 1 or dd > 29 :
                                    print()
                                    print("INVALID DATE !!! PLEASE CHECK THE RANGE OF DAY (RANGE OF DAY FOR THAT MONTH - 1 to 29) !!!")
                                    na = 1 

                            elif dd < 1 or dd > 28 :
                                print("\nINVALID DATE !!! PLEASE CHECK THE RANGE OF DAY (RANGE OF DAY FOR THAT MONTH - 1 to 28) !!!")
                                na = 1

                     else :
                            print("\nINVALID DATE !!! PLEASE CHECK THE RANGE OF MONTH (RANGE OF MONTH - 1 to 12) !!!")
                            na = 1

                     if na == 0 :
                            cindt = datetime.date(day = dd, month = mm, year = yyyy)

                            if cindt <= date_now :
                                   print("\nINVALID DATE !!! PLEASE ENTER A VALID CHECK-IN DATE STARTING FROM TOMORROW !!!")
                            else :
                                   break   

              nd = 0
              while nd < 1 or nd > 30 :
                     nd = int(input("\nEnter the NUMBER OF DAYS you want to stay : " ))
                     if nd < 1 or nd > 30 :
                         print("PLEASE ENTER A VALID NUMBER OF DAYS !!! YOU CAN BOOK A ROOM FOR MAXIMUM 30 DAYS AT A TIME !!!")

              coutdt = find_date(nd, cindt)
               
              print("\nSELECT A PAYMENT METHOD : ")

              pm = 0
              while pm != 1 and pm != 2 and pm != 3 :
                     print('''
                PRESS '1' ----->  CREDIT CARD
                
                PRESS '2' ----->  DEBIT CARD
                
                PRESS '3' ----->  EXIT (CANCEL THE CURRENT BOOKING AND LOG-OUT) \n ''')
                     pm = int(input("Enter your choice : "))
                     if pm != 1 and pm != 2 and pm != 3 :
                            print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

              if pm == 1 :
                     pm = "ONLINE via CREDIT CARD"
                     cdno = int(input("\nEnter your CREDIT CARD NUMBER without spaces : "))

                     while card_valid(cdno) == False :
                            print("INVALID CREDIT CARD NUMBER !!! PLEASE ENTER CREDIT CARD NUMBER AGAIN !!!")
                            cdno = int(input("\nEnter your CREDIT CARD NUMBER : "))

                     cvv = int(input("\nEnter the CVV : "))

                     while len((str)(cvv)) != 3 and len((str)(cvv)) != 4 :
                            print("INVALID CVV !!! PLEASE ENTER CVV AGAIN !!!")
                            cvv = int(input("\nEnter the CVV : "))

              elif pm == 2 :
                     pm = "ONLINE via DEBIT CARD"
                     cdno = int(input("\nEnter your DEBIT CARD NUMBER without spaces : "))

                     while card_valid(cdno) == False :
                            print("INVALID DEBIT CARD NUMBER !!! PLEASE ENTER DEBIT CARD NUMBER AGAIN !!!")
                            cdno = int(input("\nEnter your DEBIT CARD NUMBER : "))

                     cvv = int(input("\nEnter the CVV : "))

                     while len((str)(cvv)) != 3 and len((str)(cvv)) != 4 :
                            print("INVALID CVV !!! PLEASE ENTER CVV AGAIN !!!")
                            cvv = int(input("\nEnter the CVV : "))

              else :
                   print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!! YOU HAVE BEEN LOGGED-OUT !!! ")
                   sys.exit(0)  
              
              
              cr.execute("SELECT NAME, EMAIL_ID, PASSWORD FROM RECORDS WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
              for i in cr :
                     nm = i[0]
                     emid = i[1]
                     pswd = i[2]
              
              j = 1001
              z = 0
              with open("ROOMS_SECTION_DATA.csv", "a+", newline = '') as rm_dt :
                      rm_dt.seek(0)
                      hx = csv.DictReader(rm_dt)
                      for i in hx :                             
                             z = 1
                             j = ((int)(i["BK_ID"])) + 1
                     
                      user_dt = {"BK_ID" : j, "NAME" : nm, "PH_NO" : ph1, "EMAIL_ID" : emid, "PASSWORD" : pswd, "RM_TYPE" : rt[c - 1],
                                      "RATE_PD" : rate[c - 1], "NO_RM" : nr, "CHKIN_DT" : cindt, "CHKOUT_DT" : coutdt, "NO_DAYS" : nd,
                                      "TOTAL_AMT" : "Rs. " + ((str)((int)(rate[c - 1][4 : :]) * nr * nd)), "PAY_MTD" : pm,
                                      "BK_DATE" : datetime.datetime.now().date(), "BK_TIME" : datetime.datetime.now().time()}

                      if z == 0 :
                             wrt = csv.DictWriter(rm_dt, fieldnames = ["BK_ID", "NAME", "PH_NO", "EMAIL_ID", "PASSWORD", "RM_TYPE",
                                                                                              "RATE_PD", "NO_RM", "CHKIN_DT", "CHKOUT_DT", "NO_DAYS",
                                                                                              "TOTAL_AMT", "PAY_MTD", "BK_DATE", "BK_TIME"])
                             wrt.writeheader()
                             wrt.writerow(user_dt)

                      if z == 1 :
                             wrt = csv.DictWriter(rm_dt, fieldnames = ["BK_ID", "NAME", "PH_NO", "EMAIL_ID", "PASSWORD", "RM_TYPE",
                                                                                              "RATE_PD", "NO_RM", "CHKIN_DT", "CHKOUT_DT", "NO_DAYS",
                                                                                              "TOTAL_AMT", "PAY_MTD", "BK_DATE", "BK_TIME"])
                             wrt.writerow(user_dt)
             
              print()
              bill( j )
              print("\nDO YOU WANT TO CONTINUE WITH THIS BOOKING ?")
              cnf = 0
              while cnf != 1 and cnf != 2 :
                     print('''
                PRESS '1' ----->  YES
                
                PRESS '2' ----->  NO (CANCEL THE CURRENT BOOKING AND LOG-OUT) \n ''')
                     cnf = int(input("Enter your choice : "))
                     if cnf != 1 and cnf != 2 :
                            print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

              if cnf == 1 :
                     if nr == 1 :
                            print("\nTRANSACTION SUCCESSFUL !!! YOUR ROOM HAS BEEN BOOKED !!!")
                     else :
                            print("\nTRANSACTION SUCCESSFUL !!! YOUR ROOMS HAVE BEEN BOOKED !!!")

              if cnf == 2 :
                     cancel( j )
                     print("\nYOUR BOOKING HAS BEEN CANCELLED !!!")
                     print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!! YOU HAVE BEEN LOGGED-OUT !!! ")
                     sys.exit(0)
       
                  
       def check_booking() :

              booking_id = input("\nEnter the BOOKING ID : ")
              e = 1
              while True :
                     a = {}
                     b = 2
                     with open("ROOMS_SECTION_DATA.csv", "a+", newline = '') as fh :
                            fh.seek(0)
                            bpr = csv.DictReader(fh)
                            for i in bpr :
                                   if i["BK_ID"] == (str)(booking_id) :
                                          a = i
                                          break
                                   
                            if a == {} :
                                   b = 0
                            elif datetime.datetime.now().date() > date_make(a["CHKOUT_DT"]) :
                                   b = 1

                     if b == 0 :
                         if e == 3 :
                              print("INVALID BOOKING ID !!! NO MORE TRIES LEFT !!!")
                              break 
                         print("INVALID BOOKING ID !!! PLEASE ENTER BOOKING ID AGAIN !!!")
                         booking_id = input("\nEnter the BOOKING ID : ")
                         
                     if b == 1 :
                         print("\nTHIS BOOKING IS NO LONGER AVAILABLE !!!")
                         break

                     if b == 2 :
                         print("\n\nYOUR CURRENT BOOKING IS THIS : ")
                         bill(booking_id)
                         break

                     e = e + 1

       def cancel_booking() :

              booking_id = input("\nEnter the BOOKING ID : ")
              e = 1
              while True :
                     a = {}
                     b = 2
                     with open("ROOMS_SECTION_DATA.csv", "a+", newline = '') as fh :
                            fh.seek(0)
                            bpr = csv.DictReader(fh)
                            for i in bpr :
                                   if i["BK_ID"] == (str)(booking_id) :
                                          a = i
                                          break
                                   
                            if a == {} :
                                   b = 0
                            elif datetime.datetime.now().date() >= date_make(a["CHKIN_DT"]) :
                                   b = 1

                     if b == 0 :
                         if e == 3 :
                              print("INVALID BOOKING ID !!! NO MORE TRIES LEFT !!!")
                              break 
                         print("INVALID BOOKING ID !!! PLEASE ENTER BOOKING ID AGAIN !!!")
                         booking_id = input("\nEnter the BOOKING ID : ")
                         
                     if b == 1 :
                         print("\nTHIS BOOKING CAN NO LONGER BE CANCELLED !!!")
                         break

                     if b == 2 :
                         print("\nYOUR BOOKING HAS BEEN CANCELLED !!! YOUR REFUND IS BEING PROCESSED !!!")
                         cancel(booking_id)
                         break

                     e = e + 1
              
        
       def account_details() :

             print("\nCHOOSE WHAT YOU WANT TO CHANGE : ")

             cnf = 0
             while cnf != 1 and cnf != 2 and cnf != 3 and cnf != 4 :        
                   print('''
                PRESS '1' ----->  CHANGE NAME

                PRESS '2' ----->  CHANGE E-MAIL ID
                      
                PRESS '3' ----->  CHANGE PASSWORD
                      
                PRESS '4' ----->  EXIT (LOG-OUT) \n ''')
                   cnf = int(input("Enter your choice : "))
                   if cnf != 1 and cnf != 2 and cnf != 3 and cnf != 4 :
                         print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

             if cnf == 1 :
                   newnm = input("\nEnter the new NAME : ")
                   cr.execute("UPDATE RECORDS SET NAME = '" + newnm + "' WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
                   cr.execute("COMMIT")
                   print("\nYOUR NAME HAS BEEN CHANGED SUCCESSFULLY !!!")

             elif cnf == 2 :
                   c = 0
                   while c != 2 :
                         c = 0
                         newemid = input("\nEnter the new E-MAIL ID : ")
                         for i in newemid :
                              if i == "@" or i == "." :
                                    c = c + 1
                         if c < 2 :
                               print("PLEASE ENTER A VALID E-MAIL ID !!!")
                  
                   cr.execute("UPDATE RECORDS SET EMAIL_ID = '" + newemid + "' WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
                   cr.execute("COMMIT")
                   print("\nYOUR E-MAIL ID HAS BEEN CHANGED SUCCESSFULLY !!!")

             elif cnf == 3 :
                  while True :
                        curpswd = input("\nEnter the CURRENT PASSWORD : ")
                        cr.execute("SELECT PASSWORD FROM RECORDS WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
                        for i in cr :
                           pswd = i[0]

                        if pswd != curpswd :
                              print("CURRENT PASSWORD NOT MATCHING !!! PLEASE ENTER CURRENT PASSWORD AGAIN !!!")
                        else :
                              break
                  c = 0
                  while c < 6 :
                        newpswd = input("\nEnter the NEW PASSWORD (MINIMUM 6 CHARACTERS) : ")
                        c = len(newpswd)
                        if c < 6 :
                              print("PLEASE ENTER A STRONG PASSWORD (MINIMUM 6 CHARACTERS) !!!")

                  cr.execute("UPDATE RECORDS SET PASSWORD = '" + newpswd + "' WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
                  cr.execute("COMMIT")
                  
                  print("\nYOUR PASSWORD HAS BEEN CHANGED SUCCESSFULLY !!!")

             else :
                  print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!! YOU HAVE BEEN LOGGED-OUT !!!")
                  sys.exit(0)

       def delete_account() :

             print("\nARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT ?")

             cnf = 0
             while cnf != 1 and cnf != 2 :        
                   print('''
                PRESS '1' ----->  YES

                PRESS '2' ----->  NO \n ''')
                   cnf = int(input("Enter your choice : "))
                   if cnf != 1 and cnf != 2 :
                         print("INVALID INPUT !!! PLEASE ENTER CHOICE AGAIN !!!")

             if cnf == 1 :
                   cr.execute("DELETE FROM RECORDS WHERE PHONE_NUMBER = '" + (str)(ph1) + "'")
                   cr.execute("COMMIT")
                   print("\nYOUR ACCOUNT HAS BEEN DELETED !!!")
                              
            
       if acc == 1 :
              rooms()

       if acc == 2 :
              check_booking()

       if acc == 3 :
              cancel_booking()

       if acc == 4 :
              account_details()

       if acc == 5 :
              delete_account()
              break
            
       if acc == 6 :
            print("\nTHANK YOU FOR VISITING HOTEL THE ROYALE !!! YOU HAVE BEEN LOGGED-OUT !!!")
            sys.exit(0)
            
