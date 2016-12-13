import socket
import threading

is_finished = False


def handle(c):
    while not is_finished:
        data = c.recv(1024)
        if not data:
            c.close
            break
        print data
        c.sendall(data)


s = socket.socket()
s.bind(('0.0.0.0', 8000))
s.listen(5)
print "Server started"

try:
    while True:
        c, a = s.accept()
        print "Connected ", a

        t = threading.Thread(target=handle, args=(c,))
        t.start()
except KeyboardInterrupt:
    is_finished = True
