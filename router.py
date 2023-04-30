#  Python 3 program
#  Show path in Bellman Ford algorithm
import sys
neigh=[]
neighSize=0
forward=[]
class AjlistNode :
	# Vertices node key
	def __init__(self, id, weight) :
		# Set value of node key
		self.id = id
		self.next = None
		self.weight = weight
	

class Vertices :
	
	def __init__(self, data) :
		self.data = data
		self.next = None
	

class MyGraph :
  # number of Vertices
  def __init__(self, size) :
    self.size = size
    self.node = [None] * size
    self.set_data()
	
  # Set initial node value
  def set_data(self) :
    if (self.node == None) :
      print("\nEmpty Graph", end = "")
    else :
      index = 0
      while (index < self.size) :
        self.node[index] = Vertices(index)
        index += 1
      #self.node.append(Vertices(index))
      #for i in range(self.size+1):
      #  print('self.node:',self.node[i].data)
			
  def add_router(self) :
    self.node.append(Vertices(self.size))
    self.size=self.size+1
	
  def remove_router(self,index) :
    self.node[index-1].next=None
    del self.node[index-1]
    self.size=self.size-1
    for i in range(self.size):
      t=self.node[i]
      t=t.next
      while(t!=None):
        print(self.node[t.id].data)
        if(self.node[t.id].data==index-1):
          self.node[t.id]=self.node[t.id].next
        t=t.next

  def edit_link(self,start,last,weight):
    newEdge = AjlistNode(last, weight)
    temp = self.node[start].next
    while (self.node[temp.id].data != last) :
        temp = temp.next
    temp=newEdge

    newEdge = AjlistNode(start, weight)
    temp = self.node[last].next
    while (self.node[temp.id].data != start) :
        print('t: ',self.node[temp.id].data)
        temp = temp.next
    temp=newEdge


	# Connect two node
  def add_edge(self, start, last, weight) :
    newEdge = AjlistNode(last, weight)
    if (self.node[start].next == None) :
			# Include first adjacency list node of location start 
      self.node[start].next = newEdge
    else :
      temp = self.node[start].next
			# Add new node at the end of edge
      while (temp.next != None) :
        temp = temp.next
			
			# Add node 
      temp.next = newEdge
		
	
	# Display graph elements
  def print_graph(self) :
    print('#############################################################################################################################')
    print('#############################################################################################################################')
    if (self.size > 0 and self.node != None) :
      index = 0
      while (index < self.size) :
        print("\nAdjacency list of vertex ", self.node[index].data+1 ," : ", end = "")
        temp = self.node[index].next
        while (temp != None) :
          print(self.node[temp.id].data+1 ," ", end = "")
          temp = temp.next
				
        index += 1
			
		
	
  def view_path(self, path, location) :
    if (path[location] == -1) :
      return
		
    self.view_path(path, path[location])
    neigh.append(location)
    print(" ", location+1, end = "")
	
  def show_table(self):
    for start in range(self.size):
      neigh=[]
      self.bellman_ford(start)
      print("ROUTER",start+1,"TABLE")
      for  i in range(self.size):
        if(forward[i]==''):
          print(i+1,'|',forward[i])
        else:
          print(i+1,'|',forward[i]+1)
          
  def bellman_ford(self, source) :
    neighSize=0
    forward.clear()
    neigh.clear()
    if (source < 0 and source >= self.size) :
      return
		
    if (self.node != None) :
      distance = [0] * self.size
      path = [0] * self.size
      i = 0
      while (i < self.size) :
				# Initial distance is Integer.MAX_VALUE is infinity
        distance[i] = sys.maxsize
        path[i] = -1
        i += 1
			
      distance[source] = 0
      temp = None
      print("\n-------------------------------------------------------------------------------------------------\n Source Node ", source+1 ," \n", end = "")
      i = 1
      while (i < self.size) :
        j = 0
        while (j < self.size) :
          temp = self.node[j].next
					# compare node (J) outgoing edges
          while (temp != None) :
            if(source==2):
              print('w: ',temp.weight)
            if (distance[j] != sys.maxsize and distance[j] + temp.weight < distance[temp.id]) :
              distance[temp.id] = distance[j] + temp.weight
              path[temp.id] = j
						
            temp = temp.next
					
          j += 1
				
        i += 1
			
      i = 1
      while (i < self.size) :
        j = 0
        while (j < self.size) :
          temp = self.node[j].next
					# compare node (J) outgoing edges
          while (temp != None) :
            if (distance[j] != sys.maxsize and distance[j] + temp.weight < distance[temp.id]) :
              print("\n Negative Cycle exist node (", temp.id ," ", j ,")\n", end = "")
              return
						
            temp = temp.next
					
          j += 1
				
        i += 1
			
      print("\nVertex Distance Path\n", end = "")
      i = 0
      while (i < self.size) :
        if (distance[i] == sys.maxsize) :
          print(" ", i+1 ," \t \t Integer MAX VALUE\n", end = "")
        else :
          print(" ", i+1 ," \t ", distance[i] ,"\t ", source+1, end = "")
				
        self.view_path(path, i)
        #print('\tneigh: ',neigh)

        if i==source:
          forward.append('')
        else:
          if not neigh:
            forward.append('')
          else:
            forward.append(neigh[0])
        neigh.clear()
        #print('after neigh: ',neigh)
        print("\n", end = "")
        i += 1
			
    else :
      print("Empty Graph", end = "")
     
		


def main() :
	# Number of Routers
  totalNode = 10
  g = MyGraph(totalNode)
	# Connected two node with Edges
	# Third parameter is weight
  g.add_edge(0, 1, 2)
  g.add_edge(1, 0, 2)
  g.add_edge(0, 2, 1)
  g.add_edge(2, 0, 1)
  g.add_edge(1, 2, 3)
  g.add_edge(2, 1, 3)
  g.add_edge(1, 3, 1)
  g.add_edge(3, 1, 1)
  g.add_edge(2, 4, 1)
  g.add_edge(4, 2, 1)
  g.add_edge(3, 4, 3)
  g.add_edge(4, 3, 3)
  g.add_edge(3, 5, 2)
  g.add_edge(5, 3, 2)
  g.add_edge(4, 5, 1)
  g.add_edge(5, 4, 1)
  g.add_edge(1, 6, 4)
  g.add_edge(6, 1, 4)
  g.add_edge(3, 7, 4)
  g.add_edge(7, 3, 4)
  g.add_edge(2, 8, 4)
  g.add_edge(8, 2, 4)
  g.add_edge(4, 9, 4)
  g.add_edge(9, 4, 4)
  g.print_graph()
	# Start location

  g.show_table()
  cmd=0
  while cmd!=4:
    cmd = int(input('Please enter your command:\n1-Edit link weight\n2-Add a router\n3-Remove a router\n4-Exit\n'))
    if cmd==1:
      x = int(input('Please enter first router:\n'))
      y = int(input('Please enter second router:\n'))
      w = int(input('Please enter new link weight:\n'))
      g.edit_link(x-1,y-1,w)
      g.print_graph()
      g.show_table()
    if cmd==2:
      totalNode+=1
      g.add_router()
      print('New Router successfully Added with index',totalNode,'!')
      c=1
      while(c==1):
        c=int(input('Do you want to add link between this new router and another router?\n1-Yes\n2-No\n'))
        if c==1:
          r=int(input('which router?\n'))
          w=int(input('weight?\n'))
          g.add_edge(totalNode-1,r-1,w)
          g.add_edge(r-1,totalNode-1,w)
        g.print_graph()
        g.show_table()
    if cmd==3:
      r=int(input('which router?\n'))
      g.remove_router(r-1)
      g.print_graph()
      g.show_table()

if __name__ == "__main__":
  main()