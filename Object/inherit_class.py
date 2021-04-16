class FourCal:
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
class FourCal_div(FourCal):
    def div(self):
        result = self.first / self.second
        return result

div_data = FourCal_div(4,2)
a = div_data.add()
print(a)
    