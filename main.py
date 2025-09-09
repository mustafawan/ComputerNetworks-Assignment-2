4# main.py
import sys

class Serverdata:
    def __init__(self):
        self.domain = None
        self.type = None
        self.protocol = None

    def socketcreator(self, domain, type_, protocol):
        self.domain = domain
        self.type = type_
        self.protocol = protocol

        if self.domain != 4:
            print("Server: Domain number is not true")
            return 0
        if self.type != 1:
            print("Server: Type number is not true")
            return 0
        if self.protocol != 1:
            print("Server: Protocol number is not true")
            return 0

        print("Server: Server is created")
        print("Server: Server is listening")
        return 1

    def serveraccept(self, client_port):
        if client_port == 9000:
            print("Server: Connected to the server")
        else:
            print("Server: Connection denied")
            sys.exit()

    def serverreader(self, message, client_address="9000-9000"):
        if message == "Access5000":
            print(f"Server: Client Address= {client_address} , 5000")
            print("Server: Message is Access5000 access permitted")
            return 5000
        elif message == "Access9000":
            print(f"Server: Client Address= {client_address} , 9000")
            print("Server: Message is Access9000 access permitted")
            return 9000
        elif message == "end":
            print("Server: Server closed")
            sys.exit()
        else:
            print("Server: Access Denied")
            return -1


class Clientmy:
    def __init__(self):
        print("Client: Client is created")
        print("Client: Client is ready to connection")

    def clientcreator(self, domain, type_, protocol):
        if domain != 4:
            print("Client: Domain number is not true")
            return 0
        if type_ != 1:
            print("Client: Type number is not true")
            return 0
        if protocol != 1:
            print("Client: Protocol number is not true")
            return 0

        return 1

    def clientconnect(self):
        print("Client: Send connection demand to the server")
        self.port = int(input("Client: Enter the port number: "))
        return self.port

    def clientwriter(self, server):
        while True:
            message = input("Client: Enter the message: ")
            response = server.serverreader(message)
            if response == 5000:
                print("Client:Round Trip Time can be accepted.")
            elif response == 9000:
                print("Client: Round Trip Time is high.Check internet connection.")
            elif response == -1:
                print("Client:Connection not completed.")


# Main simulation
if __name__ == "__main__":
    domainnumber = int(input("Enter domain number: "))
    typenumber = int(input("Enter type number: "))
    protocolnumber = int(input("Enter protocol number: "))

    server = Serverdata()
    if server.socketcreator(domainnumber, typenumber, protocolnumber) != 1:
        sys.exit()

    client = Clientmy()
    if client.clientcreator(domainnumber, typenumber, protocolnumber) != 1:
        sys.exit()

    port = client.clientconnect()
    server.serveraccept(port)

    client.clientwriter(server)
