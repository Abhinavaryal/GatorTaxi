
from collections import deque

# -------------------------------------RBTTREE-----------------------------------------
# DEFINING A NODE
class RBN():
      def __init__(self, rideN, rideC, tripD):

            # 3 values to be inserted in the node, whose data is obtained from the input file
            self.rideN = rideN
            self.rideC = rideC
            self.tripD = tripD

            # Other 3 node attributes
            self.parent = None  # new node with no parent
            self.rightC = None  # new node with no rightChild
            self.leftC = None  # new node with no leftChild

            # Representing the Two colors, '0'-> black, '1'-> red
            self.nodeC = 1  # Every new node will be red

#  RBTree class to define an RBTree
class RBTree():
      def __init__(self):
            n = 0
            self.N = RBN(n, n, n)  # representing a null node
            self.N.nodeC = 0
            self.N.rightC = None
            self.N.leftC = None
            self.root = self.N

      '''to search a certain node by the help of the Ride NUmber
      TRide -> target ride, the node that we will be searching.
      This operation will be done in O(logn) time in RBtree as height 
      of RBtree will be logn'''
      def find(self, TRide):
            node2 = self.root
            while  TRide is not node2.rideN and node2 is not self.N:
                  if TRide >= node2.rideN:
                        node2 = node2.rightC #any value that is greater or equal than the parent node will be in the right side
                  else:
                        node2 = node2.leftC  #any value that is less than the parent node will be the Left side
            return node2

      '''inserting new node will trigger this function.
      This funciton will have O(logn) time complexity, 
      same as above because of height of the RBTree will be Log(n+1) and 2log(n+1)'''
      def insertN(self, rideN, rideC, tripD):
            a = self.root
            b = None
            node3 = self.find(rideN)
            if node3 is not self.N:
                  return self.N
            # creating a fresh node as it was not present
            fnode = RBN(rideN, rideC, tripD)
            fnode.rightC = self.N  # assigning null node to the right child
            fnode.leftC = self.N  # assigning null node to the left child

            while a is not self.N:
                  b = a
                  if fnode.rideN > a.rideN:  # keeping the property of the tree after assigning
                        a = a.rightC
                  else:
                        a = a.leftC

            fnode.parent = b
            if b == None:
                  self.root = fnode
            elif fnode.rideN > b.rideN:
                  b.rightC = fnode
            else:
                  b.leftC = fnode

            self.rebalanceinsert(fnode) #balancing the tree after insertion to see if no red nodes are together
            return fnode

      def rotateright(self, fnode):
            temp = fnode.leftC
            fnode.leftC = temp.rightC #swap child of one child to child of another alternately

            if temp.rightC != self.N:
                  temp.rightC.parent = fnode

            temp.parent = fnode.parent #swap parent

            if fnode.parent == None:
                  self.root = temp
            elif fnode == fnode.parent.rightC: 
                  fnode.parent.rightC = temp
            else:
                  fnode.parent.leftC = temp

            temp.rightC = fnode
            fnode.parent = temp

      def rotateleft(self, fnode):
            temp = fnode.rightC
            fnode.rightC = temp.leftC

            if temp.leftC is not self.N: 
                  temp.leftC.parent = fnode

            temp.parent = fnode.parent

            if fnode.parent is None: #it is root
                  self.root = temp

            elif fnode == fnode.parent.rightC:
                  fnode.parent.rightC = temp

            else:
                  fnode.parent.leftC = temp

            temp.leftC = fnode
            fnode.parent = temp

      #Balancing after insertion will be completed with O(logn) time complexity
      def rebalanceinsert(self, fnode):
            while fnode.parent and fnode.parent.nodeC != 0:
                  if fnode.parent == fnode.parent.parent.rightC:
                        lu = fnode.parent.parent.leftC  # checking the left uncle

                        if lu.nodeC == 0: #if uncle's node is black
                              if fnode == fnode.parent.leftC:
                                    fnode = fnode.parent
                                    self.rotateright(fnode) #right rotated from itself

                              fnode.parent.nodeC = 0 #setting parent color as black
                              fnode.parent.parent.nodeC = 1 #set grandparent as red
                              self.rotateleft(fnode.parent.parent) #left rotated from grand parent

                        else: #if uncle is red, make, parent and as uncle black
                              fnode.parent.nodeC = 0
                              lu.nodeC = 0
                              fnode.parent.parent.nodeC = 1 #set grandparent as red
                              fnode = fnode.parent.parent
                        
                  else:
                        ru = fnode.parent.parent.rightC  # checking the right uncle

                        if ru.nodeC == 0:
                              if fnode == fnode.parent.rightC:
                                    fnode = fnode.parent
                                    self.rotateleft(fnode)

                              fnode.parent.nodeC = 0
                              fnode.parent.parent.nodeC = 1
                              self.rotateright(fnode.parent.parent)

                        else:
                              fnode.parent.nodeC = 0
                              ru.nodeC = 0
                              fnode.parent.parent.nodeC = 1
                              fnode = fnode.parent.parent

                        if fnode == self.root:
                              break

            self.root.nodeC = 0

      # Both min and RBTplant will be done in O(height of the tree)
      def min(self, x):
            # If the tree is empty, return None
            if x is self.N:
                  return None
            # Traverse the tree until we reach a node with no left child
            while True:
                  # If x has no left child, x is the minimum node
                  if x.leftC is self.N:
                        return x
                  # Otherwise, move down to x's left child
                  else:
                        x = x.leftC

      # RB-transplant 
      def RBTplant(self, r, c):
            # Setting r as the root and c as the new node
            if r.parent is None:
                  self.root = c
      
            # Otherwise, updating the appropriate child of r's parent to point to c
            elif r == r.parent.rightC:
                  r.parent.rightC = c
            else:
                  r.parent.leftC = c

            # Updating the parent of the root and the child
            c.parent = r.parent

      def Updation(self, rideN, ntripD):
            if rideN.tripD < ntripD <= rideN.tripD*2:
                  rideN.rideC = rideN.rideC + 10

            elif ntripD > rideN.tripD*2:
                  self.deleteN(rideN)

            rideN.tripD = ntripD

      def Range(self, PA, PrintN, rideN1, rideN2):
            if PrintN is None:
                  return
            
            if PrintN.rideN < rideN1:
                  self.Range(PA, PrintN.rightC, rideN1, rideN2)

            elif PrintN.rideN > rideN2:
                  self.Range(PA, PrintN.leftC, rideN1, rideN2)

            else:
                  self.Range(PA, PrintN.leftC, rideN1, rideN2)
                  if PrintN.rideN >= rideN1 and PrintN.rideN <= rideN2:
                        PA.append((PrintN.rideN, PrintN.rideC, PrintN.tripD))
                        self.Range(PA, PrintN.rightC, rideN1, rideN2)

      # deletion will be done in logn time.
      def deleteN(self, dnode):
            if not dnode != self.N:  # checking for boundary condition
                  return

            orgC = dnode.nodeC
            y = dnode

            # no children present or only right child present
            if dnode.leftC is self.N:
                  x = dnode.rightC
                  self.RBTplant(dnode, dnode.rightC)

            # no children present or only left child present
            elif dnode.rightC is self.N:
                  x = dnode.leftC
                  self.RBTplant(dnode, dnode.leftC)

            # both the children are present
            else:
                  y = self.min(dnode.rightC)
                  orgC = y.nodeC
                  x = y.rightC

                  if y.parent != dnode:
                        self.RBTplant(y, y.rightC)
                        y.rightC = dnode.rightC
                        y.rightC.parent = y

                  else:
                        x.parent = y

                  self.RBTplant(dnode, y) #Transplant operation on the node
                  y.leftC = dnode.leftC
                  y.leftC.parent = y
                  y.nodeC = dnode.nodeC 

            if orgC == 0: # if the deleted node is black, we will call a balance function
                  self.balanceDel(x)

      def balanceDel(self, i): #fixing the property of RBT if a black node is deleted
            while i is not self.root and i.nodeC != 1: #done till i reaches the root and i is black
                  if i is i.parent.rightC:
                        sib = i.parent.leftC #sib = sibling of i
                        
                        if sib.nodeC != 0: 
                              sib.nodeC = 0  #as the sibling is red, make it black
                              i.parent.nodeC = 1
                              self.rotateright(i.parent) #right rotation of the parent of i
                              sib = i.parent.leftC

                        elif sib.rightC.nodeC != 1 and sib.leftC.nodeC != 1: #if both are not red
                              sib.nodeC = 1  #set the color of sibiling as red as non of its child is red
                              i = i.parent

                        else:
                              if sib.leftC.nodeC != 1: #CASE: if  left child of th sibling is black
                                    sib.rightC.nodeC = 0
                                    sib.nodeC = 1
                                    self.rotateleft(sib) #left rotaion of the sibling
                                    sib = i.parent.leftC

                              sib.nodeC = i.parent.nodeC
                              i.parent.nodeC = 0
                              sib.leftC.nodeC = 0
                              self.rotateright(i.parent)#right rotaion of the parent
                              i = self.root

                  else:
                        sib = i.parent.rightC 

                        if sib.nodeC != 0: 
                              sib.nodeC = 0 #as the sibling is red, make it black
                              i.parent.nodeC = 1
                              self.rotateleft(i.parent)#left rotaion of the parent
                              sib = i.parent.rightC

                        elif sib.leftC.nodeC != 1 and sib.rightC.nodeC != 1:
                              sib.nodeC = 1
                              i = i.parent

                        else:
                              if sib.rightC.nodeC != 1: # if sibling's right child id black
                                    sib.leftC.nodeC = 0 # set the color of its left child as black as well
                                    sib.nodeC = 1
                                    self.rotateright(sib) #right rotaion of the sibling
                                    sib = i.parent.rightC

                              sib.nodeC = i.parent.nodeC
                              i.parent.nodeC = 0
                              sib.rightC.nodeC = 0
                              self.rotateleft(i.parent)
                              i = self.root
                        
            i.nodeC = 0
      '''this is used to call the node with as we send, a list and self.root with the value from input.txt,
            This will take O(no.of print + logn) time complexity '''
      def Display(self, rideN1, rideN2):
            printable = list()
            self.Range(printable, self.root, rideN1, rideN2)
            return printable


#-------------------------------------MinHeap--------------------------------------------

class minH():
      def __init__(self) -> None:
            self.map = {}  # using dictionary to map index
            self.minheap = []  # this is where we will be storing the nodes

      # Any swapping in the minheap will happen through this function
      def swapd(self, mheap, i, j):
            mheap[i], mheap[j] = mheap[j], mheap[i]

      # Any swapping in the dictionary will happen through this function
      def swapm(self, map, k1, k2):
            temp = map[k1]
            map[k1] = map[k2]
            map[k2] = temp

      # heapify function to follow the min heap property and put smaller elements above
      def heapify(self, index):
            p = (index-1)//2  # parent index
            if index > 0 and (self.minheap[index][1] < self.minheap[p][1] or (self.minheap[index][1] == self.minheap[p][1] and self.minheap[index][2] < self.minheap[p][2])):
                  self.swapd(self.minheap, index, p)
                  self.swapm(self.map, self.minheap[index][3], self.minheap[p][3])
                  self.heapify(p)
            return

      # reverse heapify function to push larger element below by comparing with childrens 
      def revheapify(self, index): 
            C = (2 * index) + 1  # child index, initially for left node
            max = index
            for i in range(0, 2):  # running twice for both the child (left child and right child)
                  if C < len(self.minheap) and ((self.minheap[C][1] < self.minheap[max][1]) or (self.minheap[C][1] == self.minheap[max][1] and self.minheap[C][2] < self.minheap[max][2])):
                        max = C
                  C = C+1  # increasing the index by 1 as that is the difference between the sibling
            if max != index:
                  self.swapd(self.minheap, index, max)
                  self.swapm(self.map, self.minheap[index][3], self.minheap[max][3])
                  self.revheapify(max)
            return

      # inserting components and rbtnode which has already been inserted in the redblack tree
      def insertN(self, rideN, rideC, tripD, rbtN): #O(logn)
            self.minheap.append([rideN, rideC, tripD, rbtN])
            i = len(self.minheap) - 1
            self.map[rbtN] = i
            self.heapify(i)
            return

      # Basic remove min functionality. 

      def GetMin(self):#O(logn)
            if len(self.minheap) != 0:
                  # Storing the min node when minheap is not empty, so this operation can be done in RBT
                  temp = self.minheap[0]

            # boundary condition 1: if the heap only has one node, simply deleting the remaining node
            if len(self.minheap) == 1:
                  self.map.pop(self.minheap[-1][3])
                  self.minheap.pop()

            elif len(self.minheap) == 0:  # boundary condition 2: checking if the min heap is empty of not
                  return

            else:
                  # temp = self.minheap[0] # Storing the min node, so this operation can be checked if done, and continue the same in RBT
                  self.map.pop(self.minheap[0][3])
                  self.map[self.minheap[-1][3]] = 0  # Updating the index mapping
                  self.minheap[0] = self.minheap.pop()
                  self.revheapify(0)  # doing reverse heapify from root node

            return temp

      # deleting a node, requesting nodenumber that is to be deleted. 
      def deleteN(self, rideN):#O(logn)
            i = self.map[rideN]

            # if the node is not the last node, replacing it with the last node
            if i != len(self.minheap) - 1:
                  self.map[self.minheap[-1][3]] = self.map[self.minheap[i][3]]
                  del self.map[self.minheap[i][3]]
                  self.minheap[i] = self.minheap.pop()
                  self.revheapify(i)

            # if the element is the last node, simply popping it out
            else:
                  del self.map[self.minheap[i][3]]
                  self.minheap.pop()

      # if any changes is to be made to the existing data with provided 3 condition.
      def Updation(self, rideN, ntripD):#O(logn)

            # using the index of the node with rideNumber = rideN
            i = self.map[rideN]

            if self.minheap[i][2] < ntripD <= self.minheap[i][2]*2:
                  self.minheap[i][1] = self.minheap[i][1] + 10

            elif ntripD > self.minheap[i][2]*2:
                  self.deleteN(rideN)
                  return
            self.minheap[i][2] = ntripD
            self.heapify(i)
            self.revheapify(self.map[rideN])

            return
