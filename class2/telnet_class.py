#!/usr/bin/env python
'''
Convert the code from exercise2 to a class-based solution
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class TelnetConn(object):
    '''
    Establish and manage telnet connection to network devices
    '''

    def __init__(self, ip_addr, username, password):  #initialize all the necessary variables and environment ready for further use, no return is expected.
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        try:
            self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)      # pre-stage the telnet session connection
        except socket.timeout:
            sys.exit("Connection timed-out")

    def login(self):
        '''
        Login to network device
        '''
        self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        time.sleep(1)

    def send_command(self, cmd, sleep_time=1): # default values(=sleep_time)  should come after the received variable(=cmd).  #default value(=paging_cmd) isn't counted as an argument
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(sleep_time)
        return self.remote_conn.read_very_eager()  # the only return in this script!!

    def disable_paging(self, paging_cmd='terminal length 0'): #default value(=paging_cmd) isn't counted as an argument
        '''
        Disable the paging of output
        '''
        self.send_command(paging_cmd)

    def close_conn(self):
        '''
        Close telnet connection
        '''
        self.remote_conn.close()


def main():
    '''
    Convert the code from exercise2 to a class-based solution
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    my_conn = TelnetConn(ip_addr, username, password)
    my_conn.login()
    my_conn.disable_paging() #default value(=paging_cmd) isn't counted as an argument
    output = my_conn.send_command('show ip int brief') #the type of output is "str"

    print "\n\n"
    print output
    print "\n\n"

    my_conn.close_conn()


if __name__ == "__main__":
    main()

