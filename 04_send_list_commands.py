from netmiko import ConnectHandler

#Create a connect object
r1 = {
    'device_type':'cisco_ios',
    'host':'10.123.2.1',
    'username':'u1',
    'password':'cisco',
    'port':22,
    'secret':'cisco',
    'verbose':True
}
connect = ConnectHandler(**r1)
commands = ['show ip interface brief','show run']

#enable to router 
if '>' in connect.find_prompt():
    connect.enable()

# iterate over each command in command list , send to router
for command in commands: 
    output = connect.send_command(command)
    print(output)

# Closing the connection 
print('closing connection')
connect.disconnect()
