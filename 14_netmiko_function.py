from netmiko import ConnectHandler

#define function with two arguments device and command
def execute(device,command_list):
    connect = ConnectHandler(**device)
    connect.enable()
    output = connect.send_config_set(command_list)
    print(output)
    connect.disconnect()

r1 = {
    'device_type':'cisco_ios',
    'host':'10.123.2.1',
    'username':'u1',
    'password':'cisco',
    'port':22,
    'secret':'cisco',
    'verbose':True
}

#create a command list 
command_list = ['no router rip', 
                'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 
                'end',
                'sh ip int loopback 0',
                'configure terminal',
                'username u6 password 0 cisco',
                'end',
                'show version'
                ]

if __name__ == '__main__':
    execute(device = r1, command_list = command_list)
