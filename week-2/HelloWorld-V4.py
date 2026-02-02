class HelloMessage:
    def show(self):
        helloMsg = 'Hello programming world'
        print(helloMsg)
        courseMsg ='Programming Principles with Python'

        print(courseMsg)
        courseNo = 10004
        print('#prog', courseNo, sep="")

    def printMyName(self, name):
        print(name)

msg = HelloMessage()
msg.show()
msg.printMyName('Brendha')