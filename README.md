# INTERNET OF THINGS BASE SMART POLICING IN INDIA 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [My work](#my-work)
  * [Database](#database)
  * [Python Script](#python-script)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [License](#license)


## Demo
- [Complete documentation](https://drive.google.com/file/d/1QhwOWUVaP-L_TwG3bzTNXhD4OgICR9b8/view?usp=sharing) 

- [Running Project Video](https://youtube.com/playlist?list=PLKGi7w5ftnSL0hB1cEZ2TnPi3MhULqDAJ)

[![](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Starting.PNG?raw=true)](https://www.youtube.com/watch?v=lc74zeLj82A&list=PLKGi7w5ftnSL0hB1cEZ2TnPi3MhULqDAJ&index=2&t=3s)

## Overview
This is some part of the project i.e. SMART POLICING. In which I tried to register FIR using Python and MySQL database.

[![](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Working%20FLow%20Chart.PNG?raw=true)](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Working%20FLow%20Chart.PNG?raw=true)

The flow of can be more clarify. All the blue line shows the normal flow of working on the basis of this technology. I want to make focus on one point when no progress report is received
by machine from investigating officers this is shown by red line firstly server will send notification to
upper authority and then authority can give strict instruction to investigating officer.

## Motivation
I was having seen many videos that there is smart police station in Dubai. I feel like why it can't be also in Inida then I make small ppt and uploaded on digital India portal. At that time <b> Amit Sirohi </b> sir motivated me to do work on this because of him I get motivated. <br> After sometime I got call from MHRD that what is my idea they were just motivating me to do proper research on this and then contact them. I started to learn techs and try to implement some part on my idea. 
<br> After a month I got mail from [<b>Bureau of Police Research & Development</b>](https://drive.google.com/file/d/1b1Cd6Z-t3hrVfHIctRfgwXn4-Pop1iSM/view). That they wanted to meet and discuss what is my approch. But at that time I was just having a simple idea in my mind and some written work they just said do some implementaion there is nothing before implementaion.
From that day I start implemeting this project. Till now I think I have completed 1/3 implementation of project. Due to not getting proper resources and not proper guidence I am not able to complete this project.


## My Work
I have divided all the work in to several modules.
- I had created adhaar database of dummy data. 
[![](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Adhaar%20Database.PNG?raw=true)](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Adhaar%20Database.PNG?raw=true)
- One more dummy record of officers where details of officers are stored like no of cases pending, currently working on case and many more.
[![](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Officers%20Database%20Snapsot.PNG?raw=true)](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/Officers%20Database%20Snapsot.PNG?raw=true)

- New case registration from the victim. You check registration of case [here.](https://youtu.be/lc74zeLj82A)

- Now this is snapshot of FIR register where details are updated.
[![](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/FIR%20Register%20Snapshot.PNG?raw=true)](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/FIR%20Register%20Snapshot.PNG?raw=true)

- At last notification message send to victim phome number that is present in adhaar database and to investingating officer assigned by the system based on minimum no of pending cases.
[![](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/whatsapp.PNG?raw=true )](https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/whatsapp.PNG?raw=true )


## Database 
```
├── Adhaar Database
│   ├── Name
│   ├── DOB
│   ├── Adhaar_no
│   ├── Gender
│   ├── Address
│   ├── E-mail
│   ├── Mobile No
│   ├── Photo
│
├── Officers
│   ├── Name
│   ├── DOB
│   ├── ID
│   ├── Gender
│   ├── Address
│   ├── Mobile No
│   ├── E-mail
│   ├── No_of_cases
│
├── FIR Register
│   ├── Sr_no 
│   ├── Victim_Name
│   ├── DOB  
│   ├── Adhaar_no 
│   ├── Gender
│   ├── Address
│   ├── Email
│   ├── Mobile
│   ├── Registered_date_time DATETIME DEFAULT 
│   ├── CURRENT_TIMESTAMP
│   ├── Date_of_incident
│   ├── Place_pf_incident  
│   ├── Description
│   ├── Investigating_officer
│   ├── Updates 
│   ├── Last_Update 
│   ├── Profile
```
## Python Script 
```
├── Algorithms 1 (Database)
├── Algorithms 2 (Main)
├── Algorithms 3 (Officer)
├── Algorithms 4 (Registration) 
├── Algorithms 5 (Sending details)
```
## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

!<img target="_blank" src="https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/mysql.png?raw=true" width=200> 

## Team
<img target="_blank" src="https://github.com/GauravRajwada/smart-police-station/blob/main/Snapshot%20of%20Project/55804310.jpg?raw=true" width=200> <br>

[Gaurav Singh](https://github.com/GauravRajwada)

## License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0e)

Copyright 2021 Gaurav Singh
