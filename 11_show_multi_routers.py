from netmiko import ConnectHandler

#Create a list of routers 
with open ('devices.txt' ,'r') as f:
    devices = f.readlines()
    new_devices = [device[:-1]for device in devices]
    print(new_devices)

#Iterate over router list 
for router in devices: 
    r = {
        'device_type':'cisco_ios',
        'host':router,
        'username':'u1',
        'password':'cisco',
        'port':22,
        'secret':'cisco',
        'verbose':True
    }

    #connect and enable
    connect = ConnectHandler(**r)
    if '>' in connect.find_prompt():
        connect.enable()

    #send command to indvidual router
    output = connect.send_command('show ip interface brief')
    print(output)

    # Closing the connection 
    print('closing connection')
    connect.disconnect()
