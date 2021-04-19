# CUI Hotel Manager

**Note:** This is a mock program that imitates a hotel management system<br />
<br />
CUI Hotel Manager (in Python) is a simple console application, based on a Character User Interface. This project is used for hotel booking for individual accounts. In this CUI application we have tried to keep the language highly user friendly so that the user is properly directed through the steps of booking their hotel rooms. At the same we have also tried to maintain all the possibility which may help the user to book his/her hotel in a fast yet secured way.

## Contents

* [Program Features](#program-features)
* [Packages & Modules used](#packages--modules-used)
* [Prerequisites](#prerequisites)
* [Limitations of the Program](#limitations-of-the-program)
* [How to use the Program](#how-to-use-the-program)
* [Handling Program crashing Error](#handling-program-crashing-error)
* [Program Mockups](#program-mockups)
* [Developers](#developers)
* [License & Copyright](#license--copyright)

## Program Features

* **USER ACCOUNTS:** This feature helps users to create theirindividual accounts so that their data is secured and bookings areeasily accessible.
* **ACCOUNT SETTINGS:** This feature helps the users to changetheir account details like username, password & email id anytimethey wish to. (Note: For changing password, the last password willalso be required for confirmation so as to prevent unauthorisedaccess to user accounts)
* **CARD VALIDITY CHECKER:** This feature allows the system tocheck the validity of a card number based on some internationallyaccepted predefined structures for credit and debit card numbers.Thus, payments are more secured.
* **INVOICE GENERATOR:** This feature provides the user with adetailed invoice at the end of every transaction. This invoice canalso be accessed later by the user through their accounts.
* **BOOKING CANCELLATION:** This feature allows the user tocancel a booking and get the refund for a booking they had donepreviously, before the booking period is over.

## Packages & Modules used

* **MYSQL.CONNECTOR:** Used for connecting **Python** (Front-end) with **MySQL** (Back-end).
* **DATETIME:** Used for calculating the date and time duration of the hotel room booking and for checking the validity of number of days.
* **SYS:** The sys module has been implemented in order to providevarious functions and variables that are used to manipulatedifferent parts of the Python runtime environment. It allowsoperating on the interpreter as it provides access to the variablesand functions that interact strongly with the interpreter.
* **CSV:** This module has been implemented for storing records ofusers’ bookings in an organised manner in a csv file that can lateron be accessed in order to check/manipulate bookings.

## Prerequisites

* Python version 3.x **(Link to download python--> https://www.python.org/downloads/)**
* MySQL Community Server 8.0 and above **(Link to download mysql community server--> https://dev.mysql.com/downloads/mysql/)**
* **Operating System:** Windows 10/8/7, Linux, MacOS
* Minimum 128MB Ram 
* Minimum 10MB of free storage
* All necessary packages & modules mentioned above under the **"Packages & Modules used"** section should be installed on the system before hosting this program

## Limitations of the Program

* Lack of Graphical User Interface.
* Mouse is non usable – only keyboard commands.
* Character User Interface often seems non intuitiveto many.
* If user forgets their password then he/she will notfffbe able to recover his/her account.
* Confidential information/text like password, credit card number, CVV are not hidden while typing.
* Software does not have any data encryption system.

## How to use the Program

**1. First fulfill all the prerequisites mentioned above under the _"Prerequisites"_ section.**<br />
<br />
**2. Then on the GitHub repository page click on the green button named _"Code"_ and then click _"Download ZIP"_. The repository will be downloaded in your system.**
![](https://i.imgur.com/rbrFUdK.jpg)<br />
<br />
**3. Now in your system, go to the folder where you have downloaded the ZIP.**
![](https://i.imgur.com/iR86Ntx.jpg)<br />
<br />
**4. Now right click on the ZIP file and click on _"Extract Here"_.**
![](https://i.imgur.com/P8JCyk6.jpg)<br />
<br />
**5. The ZIP will be extracted to a folder named _"CUI-Hotel-Manager-main"_. Double click on the folder to open it.**
![](https://i.imgur.com/LfRGJaa.jpg)<br />
<br />
**6. Now to run the program just double click on the file _"hotel_manage.py"_. And the program runs.**
![](https://i.imgur.com/L9T0DI3.jpg)<br />
<br />

## Handling Program crashing Error

If you have set your own password while installing MySQL community server then you will face an error where the program will just keep crashing just after you follow STEP 6 mentioned above under the _"How to use the Program"_ section. The reason for this error is that while coding the program, the password for mysql connection was given as a mock password so when an user has their own password set then python would not be able to connect to mysql server due to password mismatch. To correct the error follow the steps given below:<br />
<br />
**1. After performing STEP 5 mentioned above under the _"How to use the Program"_ section, right click on the python file named _"hotel_manage.py"_ then move your mouse pointer over the option named _"Edit with IDLE"_. Another dropdown menu will be shown, there click on _"Edit with IDLE 3.x (32/64-bit)"_.**<br />
![](https://i.imgur.com/zo1X1gV.jpg)<br />
<br />
**2. Now the python file will open and you should see something like shown below. Now in the indicated area show just replace xxxxxxxx with your own MySQL server password.**
![](https://i.imgur.com/KoT7BdW.jpg)<br />
<br />
**3. Finally just click on _"File"_ option in the ribbon menu under the taskbar and click _"Save"_. Then close the file and you are done, the error is debugged.**
![](https://i.imgur.com/g6iobxn.jpg)<br />
<br />
**Now you can run the program error free.**<br />
<br />

## Program Mockups

![](https://i.imgur.com/3QxC30y.jpg)<br />
<br />
![](https://i.imgur.com/u26WhQo.jpg)<br />
<br />
![](https://i.imgur.com/d1YGuIc.jpg)<br />
<br />
![](https://i.imgur.com/HvGG5Z5.jpg)<br />
<br />
![](https://i.imgur.com/buB8gAH.jpg)<br />
<br />
![](https://i.imgur.com/NYeFOsp.jpg)<br />
<br />
![](https://i.imgur.com/DZlg0OQ.jpg)<br />
<br />

## Developers 
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md) 

![](https://i.imgur.com/M4BV4Qv.jpg)<br />
<br />

## License & Copyright

Copyright © 2021 Aritra Bose, Repository Owner and Programmer

Licensed under the [MIT License](LICENSE)
