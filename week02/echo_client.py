import socket
HOST='localhost'
PORT=1000
def echo_client():
    #网络层，传输层
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #进行TCP连接
    s.connect((HOST,PORT))
    #while True:
    with open('abc.txt','rb')as file:
        data=file.read()
    s.sendall(data)
    data=s.recv(1024)
    if not data:
        print('该文件不存在')
    else:
        print(data.decode('utf-8'))
    s.close()
if __name__=='__main__':
    echo_client()