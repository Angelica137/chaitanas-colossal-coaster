def add_to_queue(express_q: list, normal_q: list, ticket: int, name: str) -> list:
    """
    Returns an updated list
    :param ticket: stores the ticket type where 1 = express queue and
    0 = normal queue 
    """
    if ticket == 1:
        express_q.append(name)
        return express_q
    normal_q.append(name)
    return normal_q


def find_my_friend(queue: list, friend_name: str) -> int:
    """
    Returns the position in the queue the friend is at
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list, index: int, person_name: str) -> list:
    """
    Returns the updated queue once we have added the persons name to it
    :param queue: list - the queue to which we want to add the new name
    :param index: int - the position at which we want to insert the new name
    :param person_name: str - the name we need to add to the queu
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list, person_name: str) -> list:
    """"
    Returns the updates queue once ther persons name has been removed
    :param queue: list - list to remove the name from
    :param person_name: str - the name to remove from queue
    """
    queue.remove(person_name)
    return queue


def how_many_name_fellows(queue: list, person_name: str) -> int:
    """
    Returns the number of namefellows in the given queue
    """
    count = 0
    for name in queue:
        if name == person_name:
            count += 1
    return count
