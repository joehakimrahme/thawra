import operator
import random


class Battle(object):

    def __init__(self, teams, weather=None):
        self.teams = teams
        self.weather = weather
        self.log = []  # Later

        @property
        def heroes(self):
            reduce(operator.add, self.teams)

    def _other_teams(self, team):
        return [t for t in self.teams if t is not team]

    def _dead_or_alive(self):
        dead = []
        alive = []

        for team in self.teams:
            if any(hero.hp > 0 for hero in team):
                alive.append(team)
            else:
                dead.append(team)

        return dead, alive

    def select_next_hero(self):
        nextround = []
        for hero in self.teams[0] + self.teams[1]:
            if hero.hp > 0:
                for _ in range(hero.stats['SPD']):
                    nextround.append(hero)

        return random.choice(nextround)

    def battle_loop(self):
        while True:
            dead, alive = self._dead_or_alive()
            if len(alive) == 1:
                break  # cleanup actions: winners, fill stats, ...

            actor, actor_team = self.select_next_hero()
            # actor_choice = self.get_choice(actor, actor_team)
