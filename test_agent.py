import unittest

from dummy import get_data
from agent import get_agent


class AgentTestCase(unittest.TestCase):
    def count_available(self, agents, req_roles):
        final_agent = list(filter(lambda agent: agent["is_available"] and set(
            req_roles).issubset(set(agent['roles'])), agents))
        return len(final_agent)

    def test_all_available(self):
        agent_data, final_count, roles = get_data("all_available")

        agents = get_agent(agent_data, "all_available", roles)
        agents_count = self.count_available(agents, roles)

        self.assertEqual(agents_count, final_count)

    def test_least_busy(self):
        agent_data, time_available, roles = get_data("least_busy")

        agents = get_agent(agent_data, "least_busy", roles)
        agents_count = self.count_available(agents, roles)

        self.assertEqual(agents_count, 1)
        self.assertEqual(agents[0]['available_since'], time_available)

    def test_random(self):
        agent_data = get_data("random")
        role = ['management', ]

        agents = get_agent(agent_data, "random", role)
        agents_count = self.count_available(agents, role)

        self.assertEqual(agents_count, 1)


if __name__ == '__main__':
    unittest.main()
