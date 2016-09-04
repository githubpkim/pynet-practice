#!/usr/bin/env python

import email_helper

recipient = 'honglak_kim@yahoo.com'
subject = "Test message from Pylab"
message = '''
This is a fictional test message from Pylab.

Regards,

Paul
'''
sender = 'pkim@twb-tech.com'
email_helper.send_mail(recipient,subject,message,sender)
