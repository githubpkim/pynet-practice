def send_mail(recipient,subject,message,sender):
    '''
    Simple function to help simplify sending SMTP email
    Assumes a mailserver is available in localhost
    '''
    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient

    smtp_conn = smtplib.SMTP('localhost')
    
    smtp_conn.sendmail(sender,recipient,message.as_string())
    
    smtp_conn.quit()

    return True
