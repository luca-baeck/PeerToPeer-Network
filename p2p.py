from client import Client
from server import Server
from constants import *

class p2p:
    peers = ['127.0.0.1']

def main():
    msg = "sasdf".encode("utf-8")
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass



                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()