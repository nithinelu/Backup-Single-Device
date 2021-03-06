"""Establish SSH or TELENT or  SERIAL conenction
and issue the cmds   using NETMIKO Library and
save the output on the a folder with the 
date on same directory"""
# import libraries for this script
from netmiko import (
    ConnectHandler,
    redispatch,
    NetmikoAuthenticationException,
    NetMikoTimeoutException,
)
import time
from datetime import datetime
import csv
import os
from termcolor import colored


class SINGLE_SSH_TELNET_SENDCMD:
    """Function to Connect with the device
    using SSH or TELNET and Send User Specific Command Variables are (IP, Username , Password , Connection type(ssh or telnet), Command)"""

    def __init__(
        self,
        ip,
        username,
        password,
        Connection_type,
        user_cmd,
    ):
        # Argument User Specific Command .
        self.ip = ip
        self.username = username
        self.password = password
        self.Connection_type = Connection_type
        self.user_cmd = user_cmd

    def connect(self):

        device = {
            "device_type": self.Connection_type,
            "ip": self.ip,
            "username": self.username,
            "password": self.password,
        }

        # Files will be saved on same folder but with the date.
        path = datetime.now()
        # Check if the Directory Exist or not. if not will cerate a new one.
        if not os.path.exists(path.strftime("%Y" + "-" + "%m" + "-" + "%d")):
            try:
                os.mkdir(path.strftime("%Y" + "-" + "%m" + "-" + "%d"))
            except OSError:
                print(colored("Creation of the directory %s failed" % path), "green")
            else:
                print(colored("Successfully created the directory %s " % path), "green")
        path = path.strftime("%Y" + "-" + "%m" + "-" + "%d")
        print (colored("*" * 100, 'green'))
        print(" " * 45 + "Connecting " + device["ip"])
        print (colored("*" * 100, 'green'))
        # Connect the Device using NETMIKO and send the Command
        try:
            net_connect = ConnectHandler(**device)
        except NetmikoAuthenticationException:
            print("Entered Credentials are Invalid.")
        except NetMikoTimeoutException:
            print("Cannot connect to this device.")
        output = net_connect.send_command(self.user_cmd, delay_factor=5, max_loops=15000)
        print(output)
        # Backup will be saved on Folder created above and with the name as IP address+Command in txt format.
        f = open(path + "/" + device["ip"] + "-" + self.user_cmd + ".txt", "w")
        f.write(output)
        print (colored("*" * 100, 'green'))
        print(" " * 35 + "Output Saved at " + path)
        print (colored("*" * 100, 'green'))
