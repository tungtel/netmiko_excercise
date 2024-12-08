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

commands = [
    'access-list 101 permit tcp any any eq 80',
    'access-list 101 permit tcp any any eq 80',
    'access-list 101 deny ip any any'
]

output = connect.send_config_set(commands)
print(output)

shows = ['show version' ,'show ip interface brief']
for show in shows:
    output = connect.send_command(show)
    print(output)

# Closing the connection 
print('closing connection')
connect.disconnect()
