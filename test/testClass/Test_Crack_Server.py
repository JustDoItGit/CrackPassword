import CrackOkorNo.Server.Crack_Server
import error.exception.abstract

try:
    host = "47.93.29.25"
    user = "root"
    password = "Admin123"
    port = 22
    myftp = CrackOkorNo.Server.Crack_Server.Crack_Server(host, port, user, password)
    print(myftp.password)
except error.exception.abstract.Abstract:
    print("抽象类")
