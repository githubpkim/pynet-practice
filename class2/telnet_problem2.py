#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def telnet_login(ip_add):
   remote_connection = telnetlib.Telnet(ip_add,TELNET_PORT,TELNET_TIMEOUT)
   print "instance  of remote login:",remote_connection
   return remote_connection

def run_cmd(command,remote_session):
   remote_session.write(command+"\n")
   time.sleep(1)
   print remote_session.read_very_eager()
   print "***************************",remote_session.read_very_eager()
    
def main():
   ip_addr = '184.105.247.70'
   user_name = 'pyclass'
   passwd = '88newclass'

   remote_conn = telnet_login(ip_addr)
   print "remote_Conn type:",telnet_login(ip_addr)

   remote_conn.read_until("rname:", TELNET_TIMEOUT)
   remote_conn.write(user_name+'\n')
   remote_conn.read_until("word:", TELNET_TIMEOUT)
   remote_conn.write(passwd+'\n')

   run_cmd("terminal length 0",remote_conn)
   run_cmd("show version",remote_conn)
   run_cmd("show ip route",remote_conn)

   remote_conn.close()

if __name__ == "__main__":
    main()
