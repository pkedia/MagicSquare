size = 0
panelsize=700
success = 0
indexError = -1
positionError =-2
maxValue = 25
size = 0
panelsize=700
success = 0
indexError = -1
positionError =-2
#self.mySquare = []
true = 1
false = 0
unknown = 0
odd = 1
even = 2
even4 = 3


class Matrix:
  def __init__(self, size):
    i = 0
    self.size = size
    self.table = [0]
    for i in range(1,size*size): #initialize the matrix elements to zero
      self.table.append(0)
    #print('created a matrix of size {0:2d}'.format(size))
    
  def RawPrint(self):
    print(self.table)
    
  def update(self,n,i,j):     #update matrix[i,j] = n
    #print('Update-updating {0:4d} {1:4d} with value {2:4d}'.format(i,j,n))
   #if (i > size  or j > size): return indexError
    index = i*self.size + j
    #print('update-size,i,j,index is {0:2d} {1:2d} {2:2d} {3:2d}'.format(self.size,i,j,index))
    self.table[index] = n
    #self.RawPrint()
    return success
    
  def access(self,i,j):         #accessing value at i,j
    if (i > self.size  or j > self.size): raise IndexError
    index = (i)*self.size + j
    #print('accessing {0:3d}{1:3d} with index {2:3d}'.format(i,j,index))
    return self.table[index]
    
  def printmatrix(self,size):
    s = size
    print('Magic Square of size ','{0:4d}'.format(s))
    #print(self.table)
    digits = len(str(size*size))
    digit_fmt = "%" + str(digits) + "d"
    if (s > 0):
      for i in range(0,s*s, s):
         print([(digit_fmt % i) for i in self.table[i:i+s]])

class MagicSquare:
  def __init__(self, size):
    #rint('we are in init of MagicSquare')
    self.size = size
    self.currow = -1
    self.curcol = -1

    oddSquare = "MagicSquare of odd size i.e. %3d X %3d";
    evenSquare = "MagicSquare of even size i.e. %3d X %3d";
    even4Square = "MagicSquare of even (multiple of 4) size i.e. %3d X %3d";
    self.mySquare = Matrix(size)
    
  def CreateWebPageOutput(self):
    #print the magic square
    s = self.size
    w = s*6
    sum = (s*s)*(s*s+1)/2/s
    #self.mySquare.printmatrix(self.size)
    outstr = '<!DOCTYPE html>\n<html>\n<head>\n<style>\ntr {\n    text-align: Center;\n    padding:10px;\n}'
    outstr += 'table tr:nth-child(even) {\nbackground-color: #f00;\ncolor:white;}\ntable tr:nth-child(odd) {\nbackground-color:#fff;\n}\n'
    outstr += '\n</style\n</head>'
    outstr += '<p>Magic Square of size '+str(s)+'</p>'
    outstr += '<p>Sum of each Row, Each Column and each main Diagonal is '+str(sum)+'</p>'
    outstr += '<body>\n<table border="1" '
    for i in range (self.size):
      outstr += '<tr>'
      for j in range (self.size):
        outstr += '<td>' + str(self.mySquare.access(i,j)) + '</td>'
      outstr += '</tr>'
    outstr += '</table>\n</body>\n</html>'
    #print(outstr)
    return outstr

class OddMagicSquare(MagicSquare):
  def __init__(self,size):
    MagicSquare.__init__(self,size)
    #print('We are in Init of odd')
    self.size = size
    type = odd
    iconize = panelsize/self.size
    #print('initing an odd magicsquare of size {0:2d}'.format(self.size))
    
  def MoveNext(self):
    newrow = -1
    newcol = -1
    newrow = self.currow - 1
    newcol = self.curcol + 1
    #print('MoveNext-Before::newrow {0:2d} newcol {1:2d}'.format(newrow,newcol))
    if newrow < 0:
      newrow = self.size -1

    if newcol >= self.size:
      newcol = 0
      
    #print('Movenext-After ::newrow {0:2d} newcol {1:2d}'.format(newrow,newcol))
    if self.mySquare.access(newrow, newcol) == 0:
      #print('cell {0:3d}{1:3d} is empty'.format(newrow,newcol))
      self.currow = newrow
      self.curcol = newcol
    else:
      self.currow = self.currow + 1
      if self.currow >= self.size: 
        self.currow == 0
    self.curnum += 1  
    #print('movenext:{0:3d} {1:3d} {2:3d}'.format(self.curnum, self.currow, self.curcol))
    self.mySquare.update(self.curnum, self.currow, self.curcol)
    
  def Build(self):
    #print('We are in Build of Odd')
    #print('{0:2d}'.format(self.size))
    self.curnum = 1
    self.currow = 0
    self.curcol = (self.size-1)/2
    self.mySquare.update(self.curnum,self.currow,self.curcol)
    for s in range(2,self.size*self.size+1):
       self.MoveNext()
    
class Even4MagicSquare(MagicSquare):
  
  def __init__(self,size):
    MagicSquare.__init__(self,size)
    self.size = size
    
  def SeedTheSquare(self):
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
    for i in range(0,self.size):
      for j in range(0,self.size):
        if (self.mySquare.access(i,j) == 0):
          self.mySquare.update((self.size*self.size - (i*self.size + j)),i,j)
      
    
  def Build(self):
    #check the size validity must be multiple of 4
    if (self.size % 4 == 0 ):
      print("size ok")
    else:
      print("size is not multiple of 4")
      return
    #print('building MagicSquare of size {0:3d}'.format(self.size))
    for i in range(self.size):
      for j in range(self.size):
        self.mySquare.update(i*self.size+j+1,i,j)
    self.SeedTheSquare()
    self.FillTheRest()

class EvenMagicSquare(MagicSquare):
  currow = 0
  curcol = 0
  
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
      if(self.OneUpOneRight(subsize,num) == false):
        self.GoDownOne(subsize,num)
       
  def OneUpOneRight(self,size,nextnum):
    #print('OneUpOneRight: size = {0:2d},nextnum = {1:2d}'.format(size,nextnum))
    i = self.currow
    j = self.curcol
    i -= 1
    j += 1
    j %= size
    i %= size
    #if (i < 0): i += size
    if (self.mySquare.access(i,j) ==0):
      self.mySquare.update(nextnum,i,j)
      self.currow = i
      self.curcol = j
      return true
    else:
      return false
     
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
    if (domidel == true):
      temp = self.mySquare.access((subsize-1)/2,j)
      self.mySquare.update(self.mySquare.access(subsize+(subsize -1)/2,j),(subsize-1)/2,j)
      self.mySquare.update(temp,(subsize+(subsize -1)/2),j)
      
  def DoMidElements(self,j):
    subsize = self.size/2
    temp = self.mySquare.access((subsize-1)/2,j)
    self.mySquare.update(self.mySquare.access(subsize+(subsize-1)/2,j),(subsize-1)/2,j)
    self.mySquare.update(temp,subsize+(subsize-1)/2,j)
    
  def Build(self):
    #Make sure the size is even and not multiple of 4
    if ((self.size-2)%4 == 0):
      print('size is even and not multiple of 4')
    else:
      print('Not a valid size for even size square')
      return
    self.SeedTheSquare()
    #self.mySquare.RawPrint()
    self.FillTheRest()
    #print('after FillTheRest')
    #self.mySquare.RawPrint()
    #compute the number of cols to swap
    nswapcols = (self.size - 2)/4
    #swap top half with bottom half in cols 1..nswapcols and size-nswapcols + 1 .. size
    for j in range(nswapcols - 1):
      self.SwapColHalves(j, false)
      self.SwapColHalves(size - 1-j, false)
    #now swap nswapcols and swap back middle element
    self.SwapColHalves(nswapcols - 1, true)
    self.DoMidElements(nswapcols)
    
def main(size = None):
  typeOfMS = [ 'unknown', 'odd', 'even', 'even4']

  if size == None:
    size = int(input("what size Magic Square would you like: "))

  if (size > maxValue):
    return
  elif (size % 4) == 0:     #Even4MagicSquare
    magicSquare = Even4MagicSquare(size)
  elif (size % 2) == 0:     #evenMagicSquare
    magicSquare = EvenMagicSquare(size)
  else:  
    magicSquare = OddMagicSquare(size) 
  #even4Square = "MagicSquare of even (multiple of 4) size i.e. %3d X %3d";
  magicSquare.Build()
  return magicSquare.CreateWebPageOutput()


if __name__ == "__main__":
  print(main(None))