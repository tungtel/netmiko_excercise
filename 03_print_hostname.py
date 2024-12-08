from netmiko import ConnectHandler

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
output = connect.find_prompt()
print(output)
hostname = output[:-1]
print(hostname)


connect.disconnect()
