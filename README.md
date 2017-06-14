# **Log Analysis Project**

### Project Overview

> In this project, you'll work with data that could have come 
from a real-world web application, with fields representing 
information that a web server would record, such as HTTP status
codes and URL paths. The web server and the reporting tool both
connect to the same database, allowing information to flow 
from the web server into the report.

### PreRequisites:

* Python 2.7.10
* Vagrant
* VirtualBox
* Fullstack_nanodegree-vm 
* newsdata.sql file
* create local database:"news" 

### Setup Project with the following commands:

1. Launch Virtual Machine:
    
        $ vagrant up

2. Log into VM:
    
        $ vagrant ssh

3. Connect to vagrant directory:
    
        cd /vagrant

4. Create Database "news":

        $ psql
        $ CREATE DATABASE news;
        $\q

### Setup Database with the following commands:

1. Load the data in local database:

        $ psql -d news -f newsdata.sql
        

2. Create views:

        $ psql -d news -f news_views.sql

3. Run script:

        python Analysis_script.py

        
       


