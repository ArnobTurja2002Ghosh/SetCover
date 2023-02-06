class ISET():
  def __init__(self, filename):
    self._co1 = []
    self._co2 = []
    self._co3 = []
    self._b = []
    fhand = open(filename, "r")
    for line in fhand:
      self._co1.append(line)
    for i in self._co1[1:]:
      self._co2.append(i.strip()[3:])
    for i in self._co2:
      self._b.append(set(i))
    fhand.close()
  def subset_list(self):
    return self._b


  def universe(self):
    u = {" "}
    for i in range(1, int(self._co1[0][0])+1):
      u = u.union(str(i))
    return u

  def input_description(self):
    print("\t Numbers of items:", self._co1[0][0])
    print("\t Item-subset sets:")
    for i in self._co1[1:]:
      print("\t\t Set #"+i)



