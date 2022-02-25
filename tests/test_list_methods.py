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


def test_add_me_with_my_friends():
    assert add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky") == [
        "Natasha", "Bucky", "Steve", "T'challa", "Wanda", "Rocket"]
