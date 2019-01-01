import json

max_data = {
    'Sorceress': {
        'max_health': 50,
        'max_defence_power': 42,
        'max_attack_power': 90,
        'max_mana': 200
    },
    'Knight': {
        'max_health': 100,
        'max_defence_power': 170,
        'max_attack_power': 150,
        'max_mana': 0
    },
    'Barbarian': {
        'max_health': 120,
        'max_defence_power': 150,
        'max_attack_power': 180,
        'max_mana': 0
    },
    'Warlock': {
        'max_health': 70,
        'max_defence_power': 50,
        'max_attack_power': 100,
        'max_mana': 180
    }
}


class Hero(object):
    def __init__(self, race, health, attack_power, defence_power,
                 experience, mana=0):
        self.race = race
        self.experience = experience

        self.max_health = max_data[race]['max_health']
        self.max_attack_power = max_data[race]['max_attack_power']
        self.max_defence_power = max_data[race]['max_defence_power']
        self.max_mana = max_data[race]['max_mana']

        self.health = min(health, self.max_health)
        self.attack_power = min(attack_power, self.max_attack_power)
        self.defence_power = min(defence_power, self.max_defence_power)
        self.mana = min(mana, self.max_mana)

    def is_die(self):
        return self.health <= 0

    def attack(self, other, params):
        if self.is_die():
            return

        self.attack_power = self.attack_power - params['power']
        to_health = min(0, other.defence_power - params['power'])
        other.defence_power = max(0, other.defence_power - params['power'])
        other.health = max(0, other.health + to_health)

        if other.is_die():
            self.experience += 5
        else:
            self.experience += 1
            other.experience += 1

    def defence(self, other, params):
        if self.is_die():
            return
        other.attack(self, params)

    def cast_health_spell(self, other, params):
        if self.is_die():
            return

        self.mana = self.mana - params['power']
        other.health = min(other.max_health, other.health + params['power'])

    def cast_damage_spell(self, other, params):
        if self.is_die():
            return

        self.mana = self.mana - params['power']
        to_health = min(0, other.defence_power - params['power'])
        other.defence_power = max(0, other.defence_power - params['power'])
        other.health = max(0, other.health + to_health)

        if other.is_die():
            self.experience += 5
        else:
            self.experience += 1
            other.experience += 1


def create_armies(bp_army):
    ronald_army, archibald_army = {}, {}
    for id in bp_army:
        hero_info = bp_army[id]
        hero = Hero(
            hero_info['race'], hero_info['health'], hero_info['attack'],
            hero_info['defence'], hero_info['experience'],
            hero_info['mana'] if 'mana' in hero_info else 0
        )
        if hero_info['lord'] == 'Archibald':
            archibald_army[id] = hero
        else:
            ronald_army[id] = hero

    return ronald_army, archibald_army


def calc_experience(h):
    return h.experience + 2 * h.defence_power + 3 * h.attack_power \
           + 10 * h.mana


def calc_stats_for_win(army):
    health, experience = 0, 0
    for id in army:
        hero = army[id]
        if not hero.is_die():
            health += hero.health
            experience += calc_experience(hero)
    return health, experience


def define_winner(ronald_army, archibald_army):
    ronald_health, ronald_experience = calc_stats_for_win(ronald_army)
    archibald_health, archibald_experience = calc_stats_for_win(archibald_army)
    if ronald_health == 0 and archibald_health == 0:
        return 'unknown'
    if ronald_health == 0:
        return 'Archibald'
    elif archibald_health == 0:
        return 'Ronald'
    elif ronald_experience == archibald_experience:
        return 'unknown'
    else:
        return 'Ronald' if ronald_experience > archibald_experience \
            else 'Archibald'


def modeling_battle_progress(battle_progress):
    ronald_army, archibald_army = create_armies(battle_progress['armies'])

    battle_steps = battle_progress['battle_steps']
    for step in battle_steps:
        if step['id_from'] in ronald_army:
            hero_from = ronald_army[step['id_from']]
        else:
            hero_from = archibald_army[step['id_from']]

        if step['id_to'] in ronald_army:
            hero_to = ronald_army[step['id_to']]
        else:
            hero_to = archibald_army[step['id_to']]

        getattr(hero_from, step['action'])(hero_to, step)

    print(define_winner(ronald_army, archibald_army))


if __name__ == '__main__':
    try:
        battle_progress = json.loads(input())
        modeling_battle_progress(battle_progress)
    except EOFError:
        pass
