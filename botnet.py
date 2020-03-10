from pexpect import pxssh

class Bot:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()

    def ssh(self):
        try:
            bot_ssh = pxssh.pxssh()
            bot_ssh.login(self.host, self.user,self.password)
            return bot_ssh
        except Exception as e:
            print("Connection failed : " + e)
            return e
        
    def commandline(self,command):
        self.session.sendline(command)
        self.session.prompt()
        return self.session.before

def commandBot(cmd):
    for bot in botnets:
        bot.ssh()
        output = bot.commandline(cmd)
        print(output.decode())
        print()

    
botnets = []
def add_bot(host,user,password):
    bot = Bot(host,user,password)
    botnets.append(bot)

add_bot('10.0.34.143','osboxes','moltres123')
commandBot('ls')