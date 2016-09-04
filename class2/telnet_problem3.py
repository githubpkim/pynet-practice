#!/usr/bin/env python

import telnetlib
import time
import sys
import socket
import getpass

class Telnet_login(object):
   TELNET_PORT = 23
   TELNET_TIMEOUT = 6

   def __init__(self,ip_address):
      self.remote_connection = telnetlib.Telnet(ip_address,self.TELNET_PORT,self.TELNET_TIMEOUT)

   def read_til(self,msg):
      self.remote_connection.read_until(msg,self.TELNET_TIMEOUT)
  
   def run_cmd(self,command):
      self.remote_connection.write(command+"\n")
      time.sleep(1)
      print self.remote_connection.read_very_eager()
    
   def close_conn(self):
      self.remote_connection.close()

def main():
   ip_addr = '184.105.247.70'
   user_name = 'pyclass'
   #passwd = getpass.getpass()
   passwd = "88newclass"

   try:
      remote_conn = Telnet_login(ip_addr)
   except socket.timeout:
      sys.exit("Connection Timed-out")

   remote_conn.read_til("rname:")
   remote_conn.run_cmd(user_name+'\n')
   remote_conn.read_til("word:")
   remote_conn.run_cmd(passwd+'\n')

   remote_conn.run_cmd("terminal length 0")
   remote_conn.run_cmd("show version")
   remote_conn.run_cmd("show ip route")

   remote_conn.close_conn()

if __name__ == "__main__":
    main()
