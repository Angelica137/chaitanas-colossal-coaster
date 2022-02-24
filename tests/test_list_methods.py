from scripts import *


def test_add_me_to_the_queue():
    assert add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=[
                               "RobotGuy", "WW"], ticket_type=0, person_name="HawkEye") == ["RobotGuy", "WW", "HawkEye"]
