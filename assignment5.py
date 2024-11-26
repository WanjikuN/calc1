class Tech:
  def __init__(self, name,year):
    self.name = name
    # Encapsulation
    self._year=year  
  def get_year(self):
    return self._year
  def best(self):
    print(f"The best tech is {self.name}")

class Software(Tech):
  def __init__(self, name, year, dept):
    super().__init__(name, year)
    self.dept = dept
  def best(self):
    # Override parent function
    # super().best()
    print(f"The best tech is {self.name} in {self.dept}")
tech1 = Tech("Python", 2020)
# tech1.best()
tech2 = Software("Java", 1995, "Computer Science")
tech2.best()
# print(tech1.get_year())