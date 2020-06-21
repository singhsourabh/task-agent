data = [
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
        'roles': ['sales', 'dispatch', 'purchase']
    },
    {
        'is_available': False,
        'available_since': 1598609410.005656,
        'roles': ['quality', 'management']
    },
    {
        'is_available': True,
        'available_since': 1539639410.005656,
        'roles': ['sales', 'purchase']
    }
]


def get_data(mode: str):
    if mode == "all_available":
        # returns agent data and count
        return (data, 4, ["sales"])
    elif mode == "least_busy":
        # returns agent data and time
        return (data, 1509639410.005656, ["purchase"])
    else:
        # returns only agent data
        return data
