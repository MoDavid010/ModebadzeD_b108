import socket
import time
import json
import re

host = '127.0.0.1'
port = 8000
clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
quit = False
print('[Server Started]')

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        data = json.loads(data)

        if addr not in clients:
            clients.update({addr: data["name"]})
            print(clients)

        itsattime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
        print(addr, itsattime, '', end="")
        print(data)
        who_send_massege = re.findall(r"\w+", data['message'])

        if who_send_massege[0] in clients.values():
            for addr_n, name in clients.items():
                if who_send_massege[0] == name:
                    s.sendto(json.dumps(data).encode("utf-8"), addr_n)
        else:
            for client in clients:
                if addr != client:
                    s.sendto(json.dumps(data).encode('utf-8'), client)

    except Exception as ex:
        print(ex)
        print('\n[ Server Stopped ]')
        quit = True

s.close()
