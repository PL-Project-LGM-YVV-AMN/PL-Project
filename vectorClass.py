import lexer_test as lt
import re


class vector:
    elemsRule = re.compile((r'-?' + lt.t_float + r'|-?' + lt.t_int))

    def __init__(self, string):
        self.elems = vector.elemsRule.findall(string)
        self.size = len(self.elems)

    def __str__(self):
        result = re.sub(r'\'', '', str(self.elems))
        result = re.sub(",","", str(result))
        return result

    def __add__(self, RightVec):
        result = []
        for i in range(self.size):
            result.append(float(self.elems[i])+float(RightVec.elems[i]))
        vecResult = vector(vector.FormatColumnVectors(str(result)))
        return vecResult

    def __sub__(self, RightVec):
        result = []
        for i in range(self.size):
            result.append(float(self.elems[i])-float(RightVec.elems[i]))
        vecResult = vector(vector.FormatColumnVectors(str(result)))
        return vecResult
    
    def __len__(self):
        return self.size

    def scalar_multiplication(self, multiplier):
        multiplied_vec = []
        for i in range(self.size):
            multiplied_vec.append(float(self.elems[i])*multiplier)
        return vector(vector.FormatColumnVectors(str(multiplied_vec)))

    @staticmethod
    def FormatColumnVectors(string):
        result = re.sub(r'\'', '', str(string))
        result = re.sub(",","", str(result))
        return result



        


