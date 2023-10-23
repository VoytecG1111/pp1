class Array():
    @staticmethod
    def method_name(number,value):
        arr = []
        for i in range(number):
            arr.append(value)
        return arr

array = Array.method_name(3,5)
print(array)