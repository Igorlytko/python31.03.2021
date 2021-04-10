www = 'www . google.com'
if "com" in www:
    print("com in www")
else:
    print("com not in www")
######################

www ='www. command_and_conquer.com'
if "com" in www:
    print("com in www")
else:
    print("com not in www")
################################

www = 'www.command_and_conquer.net'
if "com" in www:
    print("com in www")
else:
    print("com not in www")
    #############################

www = 'www.command_and_conquer.net'
if ".com" in www:
    print("com in www")
else:
    print("com not in www")
    ####################################

www = 'www.conquer_and_command.net'
if ".com" in www:
    print("com in www")
else:
    print("com not in www")
    #################################

value = 123
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)
###############

value=321
my_str=str(value) if value<200 else str(value %10)
print(my_str)

value=123
my_str=str(value) if value<200 else str(value)[::-1]
print(my_str)

value = 321
my_str = str(value) if value < 200 else str(value) [::-1]
print(my_str)
##############

value= "123456789"
my_str = value if len(value)<5 else value [2:5]
print(my_str)
###########

volue = "123456789"
my_str=value if len(value)>=5 else value [2:5]
print(my_str)
################

value = "123456789"
my_str=value if len(value)<5 else value [2:5:2]
print(my_str)
##############

volue = "123456789"
my_str=value if len(value)>=5 else value [2:5:2]
print(my_str)
##############

value = "123456789"
my_str=value if len(value)<=5 else value [2:5]
print(my_str[::-1])
#################

value = "123456789"
my_str=value if len(value)>=5 else value [2:5]
print(my_str[::-1])
###############

value = "123456789"
my_str=value if len(volue)<=5 else value [2:5:2]
print(my_str[::-1])
#################

#count=10
#while count >0:
  #  print("Test")
###################

count=10
while count >0:
    print("Test")
    count -= 1

count=10
exit_flag=True
while exit_flag :
    count -=1
    if count >0:
        exit_flag = False
        print("Test")

################

#1##########
value=100
if value < 100:
    new_value = (value/2)
else:
    new_value =(-value)
    print(new_value)
2###########

value=100
if value<100:
    new_value = (value%3)
else:
    new_value =(value%2)
    print(new_value)
3###########
value = 100
if value < 100:
    new_value =True
else:
    new_value = False
    print(new_value)
    #######
4##################
my_str = "lesson3"
print(my_str[5:-1])
print(my_str[3:-3])
print(my_str[1:-5])

5######################

my_str="lesson3"
print(my_str[6:])
print(my_str[4:-2])
print(my_str[2:-4])
print(my_str[:-6])

6###########################

my_str = "qwer"
new_my_str = "qwer"
nnew_my_str =my_str+new_my_str
print(nnew_my_str)

7###################
my_str= "qwer"
new_my_str= "rewq"
nnew_my_str= my_str+new_my_str
print(nnew_my_str)

