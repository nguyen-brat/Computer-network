# class PublicFile:
#     def __init__(self, ):
#         pass
        
# class FetchFile:
#     def __init__(self, ):
#         pass

class Client:
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    def publicFileToServer(self, server_ip):
        '''
        Send message to signal that the client has this file
        '''
        pass

    def fetchTargetClient(self, targer_ip, file_name):
        '''
        Send message to server to find the client that contains the file 
        '''
        pass

    def handleFetchConnection(self, ):
        '''
        Create a connection with the client that has the file
        '''
        pass

    def handleFetch(self):
        '''
        handle the request and send the target file through response
        '''
        pass

if __name__ == '__main__':
    pass