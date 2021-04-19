from SAI_VISHAL.regulator_lib import Regulate
from SAI_VISHAL.regulator_lib import DeRegulate

def test_regulate():
    x = Regulate()
    print(x.int_to_be_regulated(22342342))
def test_deregulate():
    y = DeRegulate()
    print(y.int_to_be_deregulated(22342342))
