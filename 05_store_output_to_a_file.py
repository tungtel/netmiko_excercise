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

# find router hostname
prompter = connect.find_prompt()
hostname = prompter[:-1]

#enable mode to router 
if '>' in connect.find_prompt():
    connect.enable()

# iterate over each command in command list , send to router
for command in commands: 
    output = connect.send_command(command)
    print(output)
    #save output to a file in append mode
    with open (f'output-{hostname}.txt','a') as f:
        f.write(output)
        
# Closing the connection 
print('closing connection')
connect.disconnect()
