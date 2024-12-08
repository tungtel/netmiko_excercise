import netmiko 

#open file r1.txt
with open('r1.txt','r') as f:
    # fucntion readlines is to create a list , one row of file is one element of list 
    # using list,string slicing to extract r1 information , r1 is a string 
    r1 = f.readlines()[0][:-1]
    # using split method to create new list of r1 , each element is host,ip,username, etc 
    r1 = r1.split(':')
    print(r1)

r1_dict = {
    'device_type':'cisco_ios',
    'host':r1[0],
    'username':r1[2],
    'password':r1[3],
    'port':r1[1],
    'secret':r1[4],
    'verbose':True
}

print(r1_dict)

#check prompter 
connect = netmiko.ConnectHandler(**r1_dict)
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
