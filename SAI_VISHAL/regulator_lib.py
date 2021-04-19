from dataclass.regulator import Regulator

class Regulate():
    def int_to_be_regulated(self, regulator_int: int):
        if len(str(regulator_int)) ==8:
            return str(regulator_int)
        else:
            return "The given number is not regulated"

    def int_to_be_regulated_with_provided_length(self,regulator_int: int, provided_length: int):
        if type(regulator_int) == int and type(provided_length) == int:
            if len(str(provided_length))!=0:
                return str(regulator_int)
            else:
                return "Given provided length is 0"
        else:
            return "Given values for Provided length is not integer"

class DeRegulate():
    def int_to_be_deregulated(self, regulator_int: int):
        if len(str(regulator_int)) == 8:
            return str(regulator_int)
        else:
            return "The given number is not regulated"

    def int_to_be_deregulated_with_provided_length(self, regulator_int: int, provided_length: int):
        if type(regulator_int) == int and type(provided_length) == int:
            if len(str(provided_length)) != 0:
                return str(regulator_int)
            else:
                return "Given provided length is 0"
        else:
            return "Given values for Provided length is not integer"



