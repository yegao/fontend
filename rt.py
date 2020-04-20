class Fb:
  def __iter__(self):
    self.a = 0
    self.b = 1
    return self
  def __next__(self):
    self.c = self.a+self.b
    self.a = self.b
    self.b = self.c
    if self.c > 100:
      raise StopIteration()
    else:
      return self.b

fb = Fb()

for x in fb:
  print(x)