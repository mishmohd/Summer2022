# This class is a collection of functions that return a boolean if the input is valid
class InValidation:
    def ValidateReal(self):  # Validate if the argument is a real number
        vIsValid = False
        try:
            self = float(self)
            vIsValid = True
        except ValueError:
            vIsValid = False
            print("input is not a real number")
        return vIsValid

    def ValidateInteger(self):  # Validate if the argument is an integer number
        vIsValid = False
        try:
            self = int(self)
            vIsValid = True
        except ValueError:
            vIsValid = False
            print("input is not an integer number")
        return vIsValid

    def ValidateRealPositive(self):  # Validate if the argument is a real positive number
        vIsValid = False
        if InValidation.ValidateReal(self):
            if self > 0:
                vIsValid = True
        return vIsValid

    def ValidateIntegerPositve(self):  # Validate if the argument is an integer and positive number
        vIsValid = False
        if InValidation.ValidateInteger(self):
            if self > 0:
                vIsValid = True
        return vIsValid

    def ValidateList(self):  # Validate if the argument is a list
        vIsValid = False
        if isinstance(self, list):
            vIsValid = True
        return vIsValid
