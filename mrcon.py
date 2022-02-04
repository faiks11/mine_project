from mcrcon import MCRcon
import time


class rcon():

    def send(self):
        while self.while_var < len(self.command):
            with MCRcon(self.ip, self.pas, self.port) as self.mcr:
                self.resp = self.mcr.command(self.command[self.while_var])
                print(self.resp)
            self.while_var +=1

    def test_send(self):
        try:
            with MCRcon(self.ip, self.pas, self.port) as self.mcr:
                self.resp = self.mcr.command("TEST_SEND")
            self.test_send_bool = True
        except ConnectionRefusedError:
            self.test_send_bool = False

        return self.test_send_bool

    def con(self):
        if self.test_send() == True:
            self.send()
        else:
            time.sleep(1)
            self.con()

    def __init__(self, com, ip, pas, port=25575):
        self.con
        self.command = list(com)
        self.ip = ip
        self.pas = pas
        self.port = port
        self.while_var = 0
        self.test_send_bool = False

        self.con()




class test():

    def __init__(self):
        gg = 1


