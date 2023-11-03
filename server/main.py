class Server:
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    def HandlePublicRequest(self):
        '''
        Handle request from user and response with successful or failed published, if successful, store in a data structure
        '''
        pass

    def handleTargetClient(self):
        '''
        Response message with the client name that has the file or not found
        '''
        pass

    
    def fetchClientFileNames(self):
        '''
        Send messages to the client to receive the file names
        '''
        pass

    def pingHost(self):
        '''
        Send ping message to the with the timer to calculate RTT
        '''
        pass