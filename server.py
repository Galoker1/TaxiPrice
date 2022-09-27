import socket
import test
import base64
from urllib.parse import unquote

def send_data(datas):
    print("hi")
    if (datas.split(' ')[0]=="GET"):

        print("Get")
        HDRS = 'HTTP/1.1 200 OK\r\nContnent-type: text/html; charset=utf-8\r\n\r\n'
        html_file = open('main.html', 'r')
        content = html_file.read().encode('utf-8')
        client_socket.send(HDRS.encode('utf-8') + content)

    elif (datas.split(' ')[0]=="POST"):
            query_string = datas.split(' ')[1]
            code_adress_a = query_string.split("=")[1].split("&")[0]
            code_adress_b = query_string.split("&")[1].split("=")[1]
            adress_a = unquote(code_adress_a, 'utf-8')
            adress_b = unquote(code_adress_b, 'utf-8')
            k = test.start(adress_a,adress_b,175)
            k = str(k)
            content = k.encode('utf-8')
            HDRS = 'HTTP/1.1 201 OK '+ k+'\r\nContnent-type: text/html; charset=utf-8;\r\n\r\n'
            client_socket.send(HDRS.encode('utf-8') + content)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.50.136',11002))
server.listen(1000)
while True:
    client_socket, adress = server.accept()
    data = client_socket.recv(1024).decode('utf-8')
    send_data(data)

    #k = test.start("Ярославль Гагарина 11","Ярославль Губкина 12",175)
    #content = k.encode('utf-8')
    #client_socket.send(content)
