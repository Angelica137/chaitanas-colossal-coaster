from scripts.list_methods import *


def test_add_to_queue_0():
    assert add_to_queue(express_q=["Tony", "Bruce"], normal_q=[
        "RobotGuy", "WW"], ticket=0, name="HawkEye") == ["RobotGuy", "WW", "HawkEye"]


def test_add_to_queue_1():
    assert add_to_queue(["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"],
                        ticket_type=1, person_name="RichieRich") == ["Tony", "Bruce", "RichieRich"]
