from netmiko import ConnectHandler
import netmiko_functions
import threading
import time 

start = time.time()
# Define individual command 
r1_commands = ['no router rip', 
                'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 
                'end',
                'sh ip int loopback 0',
                'configure terminal',
                'username u6 password 0 cisco',
                'end',
                'show version'
                ]

r2_commands = ['no router rip', 
                'int loopback 0', 'ip address 1.1.1.4 255.255.255.255', 
                'end',
                'sh ip int loopback 0',
                'configure terminal',
                'username u7 password 0 cisco',
                'end',
                'show version'
                ]

r3_commands = ['no router rip', 
                'int loopback 0', 'ip address 1.1.1.5 255.255.255.255', 
                'end',
                'sh ip int loopback 0',
                'configure terminal',
                'username u8 password 0 cisco',
                'end',
                'show version'
                ]

#put command into a command_list 
command_list = [r1_commands, r2_commands, r3_commands]
index = 0 

#create a list of routers
with open('devices.txt','r') as f:
    devices = f.readlines()
    new_devices = [device[:-1]for device in devices]

#iterate over router lists , each IP will be assigned to host 
threads = []
for ip in new_devices:
    try:
        r = {
        'device_type':'cisco_ios',
        'host':ip,
        'username':'u1',
        'password':'cisco',
        'port':22,
        'secret':'cisco',
        'verbose':True
        }
        #select the command to be executed from command_list 
        command = command_list[index]
        index += 1 

        th = threading.Thread(target = netmiko_functions.execute, args = (r,command))
        threads.append(th)

    except:
        print(f'Host {ip} is NOT reachable. Continue checking next router')
        print('#' * 30 )
        continue 

for th in threads:
    th.start()


for th in threads:
    th.join()

print('#' * 30 )
print('task is completed')

end = time.time()
print(f'total time of running backup config is {end - start}')
