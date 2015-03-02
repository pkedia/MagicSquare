MAX_VALUE = 25
#self.mySquare = []
odd = 1
even = 2
even4 = 3


class Matrix:
  size = 0
  """Data Structure that stores the values in magic square"""
  def __init__(self, size):
    """Initializes the Matrix to all zeroes"""
    self.size = size
    self.table = [0]
    for i in range(1, size*size): # initialize the matrix elements to zero
      self.table.append(0)
    
  def RawPrint(self):
    """Dump the Matrix for debugging purposes"""
    print(self.table)
    
  def update(self,n,i,j):
    """updates the cell i,j with the value n, does not check if cell is already filled"""
    #print('Update-updating {0:4d} {1:4d} with value {2:4d}'.format(i,j,n))
    if i > self.size or j > self.size: raise IndexError
    index = i*self.size + j
    #print('update-size,i,j,index is {0:2d} {1:2d} {2:2d} {3:2d}'.format(self.size,i,j,index))
    self.table[index] = n

    
  def access(self,i,j):
    """Retrieves the value in cell i,j"""
    if i > self.size or j > self.size: raise IndexError
    index = i*self.size + j
    return self.table[index]
    
  def printmatrix(self,size):
    """ prints out the matrix formatted"""
    s = size
    print('Magic Square of size ','{0:4d}'.format(s))
    # figure out how much padding to add based on # of digits in largest number
    digits = len(str(size*size))
    digit_fmt = "%" + str(digits) + "d"
    if (s > 0):
      for i in range(0, s*s, s):
         print([(digit_fmt % i) for i in self.table[i:i+s]])

class MagicSquare:
  """Base class that Magic Squares inherit from"""
  def __init__(self, size):
    self.size = size

    self.mySquare = Matrix(size)
    
  def CreateWebPageOutput(self,size):
    """Generates HTML Output for displaying teh Magic Square in a browser"""
    #print the magic square
    s = size
    w = s*6
    sum = (s*s)*(s*s+1)/2/s
    #self.mySquare.printmatrix(self.size)
    outstr = """
      <!DOCTYPE html>
      <html>
        <head>
          <style type="text/css">\n
            tr {
              text-align: Center;
              padding:10px;
            }
            table tr:nth-child(even) {
              background-color: #f00;
              color:white;
            }
            table tr:nth-child(odd) {
              background-color:#fff;
            }
          </style>
        </head>
        <body>
          <p>Magic Square of size %d</p>
          <p>
            Sum of each Row, Each Column and each main Diagonal is %d
          </p>
        <table border="1">
    """ % (size, sum)
    for i in range (size):
      outstr += '<tr>'
      for j in range (size):
        outstr += '<td>%d</td>' % self.mySquare.access(i,j)
      outstr += '</tr>'
    outstr += """
        </table>
      </body>
    </html>
    """
    #print(outstr)
    return outstr

class OddMagicSquare(MagicSquare):
  """Generates the magic square of odd size"""
  def __init__(self, size):
    MagicSquare.__init__(self, size)
    self.size = size

    
  def MoveNext(self):
    newrow = (self.currow - 1) % self.size
    newcol = (self.curcol + 1) % self.size
    newrow = self.currow - 1
    newcol = self.curcol + 1
    #print('MoveNext-Before::newrow {0:2d} newcol {1:2d}'.format(newrow,newcol))
    if newrow < 0:
      newrow = self.size -1

    if newcol >= self.size:
      newcol = 0
      
    # if the square we're trying to move to is already occupied, use the square directly
    # below the current one
    if self.mySquare.access(newrow, newcol) != 0:
        newrow = (self.currow + 1) % self.size
        newcol = self.curcol

    self.currow = newrow
    self.curcol = newcol
    self.curnum += 1  
    #print('movenext:{0:3d} {1:3d} {2:3d}'.format(self.curnum, self.currow, self.curcol))
    self.mySquare.update(self.curnum, self.currow, self.curcol)
    
  def Build(self):
    # place the first number, then keep calling moveNext()
    self.curnum = 1
    self.currow = 0
    self.curcol = (self.size-1)/2
    self.mySquare.update(self.curnum,self.currow,self.curcol)
    for s in range(2,self.size*self.size+1):
       self.MoveNext()
    
class Even4MagicSquare(MagicSquare):
  """Generates Magic Square of doubly even size, i.e. n is a multiple of 4"""
  
  def __init__(self,size):
    MagicSquare.__init__(self,size)
    self.size = size
    
  def SeedTheSquare(self):
    # fill the square sequentially going right to left and top to bottom, i.e. 3rd cell on 2nd row in a square of size 8 will be 11
    for i in range(self.size):
      for j in range(self.size):
        self.mySquare.update(i*self.size+j+1,i,j)
    # zero out corner cells and the center block of 4 cells in each sub matrix of size 4X4
    for i in range(0, self.size, 4):
      for j in range(0, self.size, 4):
        self.mySquare.update(0,i,j)
        self.mySquare.update(0,i,j+3)
        self.mySquare.update(0,i+1,j+1)
        self.mySquare.update(0,i+1,j+2)
        self.mySquare.update(0,i+2,j+1)
        self.mySquare.update(0,i+2,j+2)
        self.mySquare.update(0,i+3,j)
        self.mySquare.update(0,i+3,j+3)
    
  def FillTheRest(self):
    # fill the zeroed out cells with numbers sequentially working backwards from last cell to first right to left and bottom to top
    for i in range(0,self.size):
      for j in range(0,self.size):
        if (self.mySquare.access(i,j) == 0):
          self.mySquare.update((self.size*self.size - (i*self.size + j)),i,j)
      
    
  def Build(self):
    self.SeedTheSquare()
    self.FillTheRest()

class EvenMagicSquare(MagicSquare):
  """Generates a Magic Square of even size"""
  
  def __init__(self,size):
    MagicSquare.__init__(self,size)
    self.size = size
    
  def GoDownOne(self,size, nextnum):
    self.currow += 1
    if (self.currow >= size): self.currow -= size
    self.mySquare.update(nextnum,self.currow,self.curcol)
     
  def SeedTheSquare(self):
    subsize = self.size/2
    self.currow = 0
    self.curcol = (subsize - 1)/2
    self.mySquare.update(1,self.currow,self.curcol)
    
    for num in range(2,subsize*subsize+1):
      if(self.OneUpOneRight(subsize,num) == False):
        self.GoDownOne(subsize,num)
       
  def OneUpOneRight(self,size,nextnum):
    #print('OneUpOneRight: size = {0:2d},nextnum = {1:2d}'.format(size,nextnum))
    i = (self.currow - 1) % size
    j = (self.curcol + 1) % size
    if (self.mySquare.access(i,j) ==0):
      self.mySquare.update(nextnum,i,j)
      self.currow = i
      self.curcol = j
      return True
    else:
      return False
     
  def FillTheRest(self):
    halfsize = self.size/2
    for i in range(self.size/2):
      for j in range(self.size/2):
        temp = self.mySquare.access(i,j)
        halfsizesq = halfsize*halfsize
        #matrix 4
        self.mySquare.update(temp+halfsizesq,i+halfsize,j+halfsize)
        #matrix 2
        self.mySquare.update(temp+3*halfsizesq,i+halfsize,j)
        #matrix 3
        self.mySquare.update(temp+2*halfsizesq,i,j+halfsize)
     
  def SwapColHalves(self,j,domidel):
    subsize = self.size/2
    for i in range(subsize):
      temp = self.mySquare.access(i,j)
      self.mySquare.update(self.mySquare.access(i+subsize,j),i,j)
      self.mySquare.update(temp,i+subsize,j)
    if (domidel == True):
      temp = self.mySquare.access((subsize-1)/2,j)
      self.mySquare.update(self.mySquare.access(subsize+(subsize -1)/2,j),(subsize-1)/2,j)
      self.mySquare.update(temp,(subsize+(subsize -1)/2),j)
      
  def DoMidElements(self,j):
    subsize = self.size/2
    temp = self.mySquare.access((subsize-1)/2,j)
    self.mySquare.update(self.mySquare.access(subsize+(subsize-1)/2,j),(subsize-1)/2,j)
    self.mySquare.update(temp,subsize+(subsize-1)/2,j)
    
  def Build(self):
    self.SeedTheSquare()
    self.FillTheRest()
    #compute the number of cols to swap
    nswapcols = (self.size - 2)/4
    #swap top half with bottom half in cols 1..nswapcols and size-nswapcols + 1 .. size
    for j in range(nswapcols - 1):
      self.SwapColHalves(j, False)
      self.SwapColHalves(size - 1-j, False)
    #now swap nswapcols and swap back middle element
    self.SwapColHalves(nswapcols - 1, True)
    self.DoMidElements(nswapcols)
    
def main(size = None):

  if size == None:
    size = int(input("what size Magic Square would you like: "))

  if (size > MAX_VALUE):
    return
  elif (size % 4) == 0:     #Even4MagicSquare
    magicSquare = Even4MagicSquare(size)
  elif (size % 2) == 0:     #evenMagicSquare
    magicSquare = EvenMagicSquare(size)
  else:  
    magicSquare = OddMagicSquare(size) 
  magicSquare.Build()
  return magicSquare.CreateWebPageOutput(size)


if __name__ == "__main__":
  print(main(None))