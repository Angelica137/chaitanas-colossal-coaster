from scripts.list_methods import *


def test_add_to_queue_0():
    assert add_to_queue(express_q=["Tony", "Bruce"], normal_q=[
        "RobotGuy", "WW"], ticket=0, name="HawkEye") == ["RobotGuy", "WW", "HawkEye"]


def test_add_to_queue_1():
    assert add_to_queue(express_q=["Tony", "Bruce"], normal_q=["RobotGuy", "WW"],
                        ticket=1, name="RichieRich") == ["Tony", "Bruce", "RichieRich"]


def test_find_my_friend():
    assert find_my_friend(
        queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve") == 1
