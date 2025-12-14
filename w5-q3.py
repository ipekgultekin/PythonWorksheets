from threading import *
import random
import time

class FruitMarket:
    def __init__(self, capacity):
        self.capacity = capacity
        self.apple = 0
        self.orange = 0

        self.cond = Condition() #Condition: include both lock and wait/notify

    def total(self):
        return self.apple+self.orange

    def put_fruit(self, fruit):
        with self.cond:
            while self.total() >= self.capacity: #if the market is full, farmer wait
                print(f"[FARMER] market is full")
                self.cond.wait()

            if fruit == "apple":
                self.apple += 1
            else:
                self.orange += 1
            print(f"[FARMER] +1 fruit added")
            self.cond.notify_all()

    def buy_fruit(self, fruit):
        with self.cond:
            if fruit == "apple":
                while self.apple == 0:
                    print("There is no apple, wait")
                    self.cond.wait()
                self.apple -= 1
            else:
                while self.orange == 0:
                    print("There is no orange, wait")
                    self.cond.wait()
                self.orange -= 1
            print(f"[CUSTOMER] -1 fruit buy")
            self.cond.notify_all()

class Farmer(Thread):
    def __init__(self, tName, market, rounds=10):
        Thread.__init__(self,name= tName)
        self.market = market
        self.rounds = rounds

    def run(self):
        for _ in range(self.rounds):
            fruit = random.choice(["apple","orange"]) # farmer can produce apple or orange randomly
            self.market.put_fruit(fruit)
            time.sleep(random.uniform(0.1,0.4))

class Customer(Thread):
    def __init__(self, tName, market, rounds=10):
        Thread.__init__(self, name=tName)
        self.market = market
        self.rounds = rounds

    def run(self):
        for _ in range(self.rounds):
            fruit = random.choice(["apple","orange"])
            self.market.buy_fruit(fruit)
            time.sleep(random.uniform(0.1,0.5))

if __name__ == "__main__":
    market = FruitMarket(capacity=5)
    farmers = [Farmer("Farmer-1", market, rounds=12),
               Farmer("Farmer-2", market, rounds=12)]

    customers = [Customer("Customer-1", market, rounds=12),
                 Customer("Customer-2", market, rounds=12),
                 Customer("Customer-3", market, rounds=12)]

    for t in farmers+customers: #starting threads
        t.start()

    for t in farmers+customers: #wait threads to complete
        t.join()

    print("finished!!!")