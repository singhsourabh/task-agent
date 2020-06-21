import random
from datetime import timedelta


def get_agent(agents: list, selection_mode: str, req_roles: list = []) -> list:
    """Retrieve all free agents with matchinng roles

    Args:
        agents (list): list of all agents
        selection_mode (str): the mode in which agent/s will be selected
        req_roles (str): list of roles required in selected agent/s
    Returns:
        list of selected agents
    """

    # To filter out all free agents with matchinng roles
    free_agents = list(filter(lambda agent: agent["is_available"] and set(
        req_roles).issubset(set(agent['roles'])), agents))

    if selection_mode == "all_available" or len(free_agents) == 0:
        return free_agents
    elif selection_mode == "least_busy":
        return [min(free_agents, key=lambda agent: agent['available_since']), ]
    else:
        return [random.choice(free_agents), ]


if __name__ == "__main__":
    agents = [
        {
            'is_available': True,
            'available_since': 1592639410.005656,
            'roles': ['sales', 'purchase']
        },
        {
            'is_available': False,
            'available_since': 1592639510.005656,
            'roles': ['store']
        },
        {
            'is_available': True,
            'available_since': 1592639419.005656,
            'roles': ['sales', 'management']
        },
        {
            'is_available': True,
            'available_since': 1592632410.005656,
            'roles': ['quality', 'store']
        },
        {
            'is_available': False,
            'available_since': 1592609410.005656,
            'roles': ['dispatch']
        },
        {
            'is_available': True,
            'available_since': 1509639410.005656,
            'roles': ['sales', 'dispatch']
        }
    ]
    print('All available:', get_agent(
        agents, "all_available", ['A']), sep='\n')
    print('Least busy:', get_agent(agents, "least_busy", ['sales']), sep='\n')
    print('Random:', get_agent(agents, "random", ['A']), sep='\n')
