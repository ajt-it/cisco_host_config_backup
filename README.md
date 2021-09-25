![Python 2.7](https://img.shields.io/badge/Python-2.7%2B-green)      ![cisco ios](https://img.shields.io/badge/CISCO-IOS-yellow)      ![Licence GPL-3.0](https://img.shields.io/badge/Licence-GPL_3.0-red)

# cisco_host_config_backup
This script backups the configuration of your CISCO equipments; it is written in "Python 2.7".

Infrastructure :

![Infra script backup cisco](https://user-images.githubusercontent.com/46109209/134438643-949ba2ee-628b-4adf-b86b-7f6d5bd26573.png)


## Works for:
 - :white_check_mark: CISCO Routers
 - :white_check_mark: CISCO Layer 3 Switches


## Prerequisites
You will need Telnet access on the targets, as well as the same "Username" and "Password" on each of them.

## Set up of the script launching system

We used an Ubuntu 18.04 linux machine.
The most recent version of 'Python' at the time of writing is '3.8'.
However, the version used is "Python 2.7"

Proceed as follows for the installation:

![1](https://user-images.githubusercontent.com/46109209/134434702-354572fd-8239-4ff1-ab76-139ce1db18b9.png)

![2](https://user-images.githubusercontent.com/46109209/134434712-5545b39e-0073-490b-b021-dd3a80c3f963.png)


Now you have to determine the location of the script and the files :
" /home/gns3/Scripts/Python-Scripts/ "

![3](https://user-images.githubusercontent.com/46109209/134435282-d4ee782a-5c9b-44bb-87f6-f8a4fbf1bcab.png)

In "1" and "2", create the files.

In "3", we have chosen to assign the 777 rights on all the files.

![4](https://user-images.githubusercontent.com/46109209/134436281-c71adb0e-f0f5-4a22-8e4c-e718dd15a89d.png)

N.B. ALL RIGHTS MUST NEVER BE GIVEN TO USERS OF THE SYSTEM.
     A MORE RESTRICTIVE MANAGEMENT OF ACCESS RIGHTS AND AUTHORIZATIONS MUST BE CONSIDERED.
 
It is also possible to make the script executable with the command: "sudo chmod + x ./cisco_backup.py"


## Script execution process :

On the Ubuntu machine:

Find your way to where the script is located;

... with the following command, run the script : " sudo ./cisco_backup.py "

![5](https://user-images.githubusercontent.com/46109209/134436693-836f6daf-782e-4f76-8fa8-9d83bba1b0bd.png)

![3](https://user-images.githubusercontent.com/46109209/134736428-6815b6eb-4f7e-4038-8bb8-3154486cd505.png)

On the router:

By using the command "debug telnet" on the host (router or switch);
we enable the verbose mode (wich shows telnet actions on the host).

![heheherherherher](https://user-images.githubusercontent.com/46109209/134739552-b490ae7b-405c-4415-8d2c-fe875867a350.png)

![6](https://user-images.githubusercontent.com/46109209/134437621-b79b86ed-aa1e-4b97-a1b1-e4102d4a35db.png)

Backups location:

![8](https://user-images.githubusercontent.com/46109209/134438072-b11af136-e946-4bed-9618-ad429c5c2e2d.png)


