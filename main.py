from start_serv import start_serv
from mrcon import rcon


test = start_serv("D:\mine_project\server", "ds.bat", "java.exe", True)

rcon(["help", "say Goodbye", "op Faiks12"], "192.168.0.105", "van")


