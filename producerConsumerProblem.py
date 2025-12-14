from threading import *
import time

resource = 0 #available or not(initially not)
class Consumer(Thread):
    def __init__(self, tName, cVariable): #cVariable common to all of them
        Thread.__init__(self, name=tName)
        self.cVariable = cVariable
        print(self.name + " is created")

    def run(self):
        global resource
        with self.cVariable: #it acquires the associated lock for the duration of the end
            while resource == 0: #multiple of them together, but resource may not available, one of them can use resource == 0, others can block
                print(self.name + " is waiting for a resource")
                self.cVariable.wait()
            resource = 0 #we will make it 1 in producer side
            print(self.name + " consumed the resource")


class Producer(Thread):
    def __init__(self, cVariable):
        Thread.__init__(self)
        self.cVariable = cVariable
        print("Producer is created")

    def run(self):
        global resource
        for i in range(5):
            with self.cVariable:
                resource = 1
                print("Resource is generated")
                self.cVariable.notifyAll() #it notifies for all threads that resource is available
            time.sleep(10)

if __name__ == "__main__":
    cVariable = Condition()
    producer = Producer(cVariable)
    consumers = []
    for i in range(1,6):
        consumers.append(Consumer("C" + str(i), cVariable))
    for i in range(5):
        consumers[i].start()
    producer.start()


