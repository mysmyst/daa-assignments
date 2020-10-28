print("0/1 Knapsack branch and bound")

ub=9999
cost=9999
kp=[]
print("enter the contents to put in knapsack as 'profit weight', eg. '6 2' enter x to stop.")
while True:
    inp=input("enter object- ")
    if inp=='x':
        break
    inp=inp.split()
    kp.append([inp[0],inp[1]])

cap=int(input("enter capacity of knapsack- "))
n=len(kp)




class node:
    left=False
    right=False
    weight=-1
    def calccost(self,weight):
        pass
    def calcub(self,weight):
        while True:
            pass
