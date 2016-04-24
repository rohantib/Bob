import smtplib, threading, time, random, traceback

class Server():
    'Class to contain server object along with additional variables and methods'
    def __init__(self, email):
        self.email = email
        self.data_path = ".emails/%s" % (email)
        #Get password
        with open("%s/.password.txt" % (self.data_path), "r") as pass_file:
            self.password = pass_file.read() #Do not strip in case user has trailing spaces for password
        #Get messages sent
        with open("%s/.messages_sent.txt" % (self.data_path), "r") as messages_sent_file:
            self.messages_sent = int(messages_sent_file.read().strip())
        #Get list of messages
        self.messages = []
        with open("%s/.messages.txt" % (self.data_path), "r") as messages_file:
            for line in messages_file:
                self.messages.append(line.strip())
        #Get list of targets
        self.targets = []
        with open("%s/.targets.txt" % (self.data_path), "r") as targets_file:
            for line in targets_file:
                self.targets.append(line.strip())
        #Set Boolean to determine if server is currently spamming to false
        self.currently_spamming = False
        #Overwrite log file
        log_file = open("%s/output.log" % (self.data_path), "w")
        log_file.close()
        self.status = "Not spamming"


    def write_to_log(self, output):
        with open("%s/output.log" % (self.data_path), "a") as log_file:
            timestamp = time.ctime(time.time())
            log_file.write("%s - %s" % (timestamp, output))

    def write_to_messages_sent(self):
        with open("%s/.messages_sent.txt" % (self.data_path), "w") as messages_sent_file:
            messages_sent_file.write(str(self.messages_sent))

    def initialize_server(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.email,self.password)

    def send_message(self, target):
        try:
            msg = self.messages[random.randrange(len(self.messages))]
            self.server.sendmail(self.email, target, msg)
            self.messages_sent += 1
            self.write_to_messages_sent()
            self.write_to_log("%s sent to %s" % (self.email, target))
        except smtplib.SMTPServerDisconnected:
            self.write_to_log("Disconnected by ban, email %s" % (self.email))
            self.initialize_server()
            self.write_to_log("Logged in again to %s" % (self.email))

#Put universal except in thread class
#Consider calling write_to_messages_sent only when thread is being shut down
class ServerThread(threading.Thread):
    'Class to make a separate server thread that will spam outside of main thread'
    SECONDS_IN_A_DAY = 24*60*60
    DAILY_LIMIT = 500

    def __init__(self, server_object):
        threading.Thread.__init__(self)
        self.exitFlag = 0
        self.server_object = server_object
        self.server_object.currently_spamming = False #Server is not currently spamming
        self.server_object.status = "Not spamming"
        self.daemon = True #Sets it as daemon thread so that when main thread exits, this is terminated too

    def run(self):
        target_index = 0
        self.server_object.initialize_server()
        self.server_object.currently_spamming = True #Server is now spamming
        self.server_object.status = "Currently spamming"
        while not self.exitFlag:
            try:
                self.server_object.send_message(self.server_object.targets[target_index])
                target_index = (target_index + 1) % len(self.server_object.targets)
                target_index += 1
                time.sleep(ServerThread.SECONDS_IN_A_DAY/ServerThread.DAILY_LIMIT)
            except Exception as error:
                self.server_object.status = "Not spamming - Error thrown - %s - look in log file at %s/output.log for more info" % (error.message, self.server_object.data_path)
                self.server_object.write_to_log(traceback.format_exc())
                self.exitFlag = 1
        self.server_object.write_to_log("Exit flag checked in old thread - Spamming with %s is stopping..." % (self.server_object.email))
        self.server_object.server.quit()
