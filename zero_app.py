import zerorpc

class TestApi(object):
    """Python class containing the method calls for application
    functionality.
    """
    def say_hello(self):
        return "Hello, World!"

def main():
    """Server configuration"""
    address = 'tcp://127.0.0.1:4242'
    server = zerorpc.Server(TestApi())
    server.bind(address)
    server.run()
    
if __name__ == "__main__":
    main()
