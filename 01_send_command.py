import netmiko

#define router creds
r1 = {
    'device_type':'cisco_ios',
    'host':'10.123.2.1',
    'username':'u1',
    'password':'cisco',
    'port':22,
    'secret':'cisco',
    'verbose':True
}

#check prompter 
connect = netmiko.ConnectHandler(**r1)
prompter = connect.find_prompt()

#Enable
if '>' in prompter:
    print('Entering enable mode')
    connect.enable()
    prompter = connect.find_prompt()
    print(prompter)

#Send commands 
output = connect.send_command('show arp')
print(output)

#Closing connection 
print('closing connection')
connect.disconnect()
