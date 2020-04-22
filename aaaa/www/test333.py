from colorama import Fore

class LogTest333(object):
    def __print(self,msg,color):
        if type(msg) == str:
            print(color+msg+Fore.RESET)
        else:
            print(color)
            print(msg)
            print(Fore.RESET)
    def d(self,selfarm,msg):
        selfarm.__print(self,msg,Fore.BLUE)

    def v(self,selfarm,msg):
        selfarm.__print(self,msg,Fore.GREEN)

    def w(self,selfarm,msg):
        selfarm.__print(self,msg,Fore.YELLOW)

    def e(self,selfarm,msg):
        selfarm.__print(self,msg,Fore.RED)

if __name__ == '__main__':
    pass