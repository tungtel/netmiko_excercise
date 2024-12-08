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
if '>' in connect.find_prompt():
    connect.enable()

#create a list of config commands
with open ('rip.txt','r') as f:
    rip = f.readlines()
    new_rip = [r[:-1] for r in rip]

#send commands to router
output = connect.send_config_set(new_rip)
print(output)

#verify the rip config
shows = ['show ip route' ,'show run | section router' ]
for show in shows:
    output = connect.send_command(show)
    print(output)

# Closing the connection 
print('closing connection')
connect.disconnect()
