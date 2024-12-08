from netmiko import ConnectHandler
import getpass
from datetime import datetime

username = getpass.getpass('Please enter username: ')
print(username)

enable_password = getpass.getpass('Please enter enable password: ')
print(enable_password)

#Create a connect object , parameters are defined from getpass 
r1 = {
    'device_type':'cisco_ios',
    'host':'10.123.2.1',
    'username':username,
    'password':'cisco',
    'port':22,
    'secret':enable_password,
    'verbose':True
}

connect = ConnectHandler(**r1)
commands = ['show ip interface brief','show run']

# find router hostname
prompter = connect.find_prompt()
hostname = prompter[:-1]

#enable mode to router 
if '>' in connect.find_prompt():
    connect.enable()

#create object current_time by calling method now on class datetime 
current_time = datetime.now()

#acces attribute of current_time
year = current_time.year 
month = current_time.month 
date = current_time.day
hour = current_time.hour
min = current_time.minute

# iterate over each command in command list , send to router
for command in commands: 
    output = connect.send_command(command)
    print(output)
    #save output to a file in append mode
    with open (f'output-{hostname}_{year}_{month}_{date}_{hour}_{min}.txt','a') as f:
        f.write(output)
        
# Closing the connection 
print('closing connection')
connect.disconnect()
