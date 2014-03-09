# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import operator
import random


class Battle(object):

    def __init__(self, teams, weather=None):
        self.teams = teams
        self.weather = weather
        self.log = []  # Later

    #TODO(rahmu): Does it really need to be a property?
    @property
    def action_choices(self):
        self._action_choices = {}
        for hero in self.heroes:
            self._action_choices[hero] = {
                'ATK': hero.actions['ATK'],
                'MAG': hero.actions['MAG'],
            }
            # TODO(rahmu): Fill the rest with the skillmap

        return self._action_choices

    @property
    def heroes(self):
        return reduce(operator.add, self.teams)

    def enemies(self, team):
        return reduce(operator.add,
                      filter(lambda x: x is not team, self.teams),
                      [])

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
        for team in self.teams:
            for hero in team:
                if hero.hp > 0:
                    for _ in range(hero.stats['SPD']):
                        nextround.append((hero, team))

        return random.choice(nextround)

    def battle_loop(self):
        while True:
            dead, alive = self._dead_or_alive()
            if len(alive) == 1:
                break  # cleanup actions: winners, fill stats, ...

            actor, actor_team = self.select_next_hero()
            actor_choice, actor_target = actor.choice(
                actor_team, self.enemies(actor_team))

            actor_action = self.action_choices[actor][actor_choice]
            actor_action(actor_target)(self.weather)
