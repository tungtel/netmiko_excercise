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

output = connect.send_config_set('username admin1 secret topsecret')
print(output)
output = connect.send_command('write memory')
print(output)

# Closing the connection 
print('closing connection')
connect.disconnect()
