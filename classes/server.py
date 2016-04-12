import smtplib, threading, time, random

class Server():
    'Class to contain server object along with additional variables and methods'
    def __init__(self, email, password):
        self.email = email
        self.data_path = ".emails/%s" % (email)
        with open("%s/.password.txt" % (self.data_path), "r") as pass_file:
            self.password = pass_file.read() #Do not strip in case user has trailing spaces for password
        with open("%s/.messages_sent.txt", "r") as messages_sent_file:
            self.messages_sent = int(messages_sent_file.read().strip())
        self.messages = []
        with open("%s/.messages.txt", "r") as messages_file:
            for line in messages_file:
                self.messages.append(line.strip())
        self.currently_spamming = False
        #Overwrite log file
        log_file = open("%s/.log" % (self.data_path), "w")
        log_file.close()

    def write_to_log(self, output):
        with open("%s/.log" % (data_path), "a") as log_file:
            log_file.write(output)

    def write_to_messages_sent(self):
        with open("%s/.messages_sent.txt") as messages_sent_file:
            messages_sent_file.write(self.messages_sent)

    def initialize_server(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
    	server.starttls()
    	server.login(self.email,self.password)

    """def spam(self):
        self.spamming = True
        while True:
            try:
    			msg = messages[random.randrange(len(messages))]
    			server.sendmail(usernames[index], toaddrs[counter], msg)
    			messages_sent[index] += 1
    			print "%s sent to %s" % (usernames[index], toaddrs[counter])
    			print("%d message(s) sent today from %s, %d total message(s) from %s" % ((((messages_sent[index]-1) % daily_limit) + 1) , usernames[index], messages_sent[index], usernames[index]))
    			counter = (counter + 1) % len(toaddrs)
    			file_IO.write_to_messages(messages_sent, "messages_sent.txt")
    		except smtplib.SMTPServerDisconnected:
    			print "Disconnected by ban, email %s" % (usernames[index])
    			servers[index] = server_management.initialize_a_server(usernames[index], passwords[index])
    			print "Logged in again to %s" % (usernames[index])"""

#Put universal except in thread class
#Consider calling write_to_messages_sent only when thread is being shut down
"""class ServerThread(threading.Thread):
    'Class to make a separate server thread that will spam outside of main thread'
"""
