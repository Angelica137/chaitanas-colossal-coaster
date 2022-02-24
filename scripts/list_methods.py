def add_to_queue(express_q: list, normal_q: list, ticket: int, name: str) -> list:
    """
    Returns an updated list
    :param ticket stores the ticket type where 1 = express queue and
    0 = normal queue 
    """
    if ticket == 1:
        express_q.append(name)
        return express_q
    normal_q.append(name)
    return normal_q