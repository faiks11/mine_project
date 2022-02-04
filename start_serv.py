import os
import psutil

class start_serv():

    def scan_process(self):
        for self.process in psutil.process_iter():
            self.processlist.append(self.process.name())
        return self.processlist

    def check_proc(self):
        while self.while_var < len(self.process_list):
            if self.process_list[self.while_var] == self.proc_name:
                self.check_proc_bool = True
                break
            else:
                pass
            self.while_var +=1
        return self.check_proc_bool

    def start_prog(self):
        os.chdir(self.serv_path)
        os.startfile(self.prog)

    def __init__(self, serv_path, prog ,proc_name, launch_prog):


        self.proc_name = proc_name

        self.serv_path = serv_path

        self.while_var = 0

        self.processlist = list()

        self.check_proc_bool = bool()

        self.launch_prog = bool(launch_prog)

        self.prog = prog



        self.process_list = self.scan_process()

        self.avalib_proc = self.check_proc()

        if self.launch_prog == True and self.avalib_proc == False:
            self.start_prog()
        else:
            pass

if __name__ == "__main__":

    start_serv("D:\mine_project\server", "ds.bat", "java.exe", True)