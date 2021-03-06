"""Backup or collect show tech file from a Cisco Device Using 
SSH/TELNET method for
a single device and Configuration Template"""
# Import the Connection Library which is saved on the same folder
# And getpass for colelcting password
import connection
import getpass
from termcolor import colored

#user provide the required details to connect with the device
ip_add = input(colored("Enter The Device IP Adress:-", "green"))
user_name = input(colored("Enter The Username:-", "red"))
pass_word = getpass.getpass(colored("Enter Password:-", "red"))
# based on the mode of imput telnet or ssh required commands will be used
Connection_mode = input(colored("Enter the Connection Type (telnet/ssh):-", "green"))
if Connection_mode == "telnet":
    Connection_type = "cisco_ios_telnet"
if Connection_mode == "ssh":
    Connection_type = "cisco_ios"
user_cmd = input(colored("Enter the Command:-", "blue"))

# SINGLE_SSH_TELNET_SENDCMD is a Class in connection library
device_data = connection.SINGLE_SSH_TELNET_SENDCMD(
    ip_add,
    user_name,
    pass_word,
    Connection_type,
    user_cmd,
)
device_data.connect()
