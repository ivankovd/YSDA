class Player(object):
    def __init__(self, start_msg='start', ready_msg='ready'):
        self.command1 = start_msg
        self.command2 = ready_msg
        self.ready = self.iterator
        delattr(Player, 'iterator')

    def iterator(self, com1, com2):
        self.command1 = com1
        command2 = getattr(self, self.command2)
        setattr(self, com2, command2)
        delattr(self, self.command2)
        self.command2 = com2

    def try_play(self, game):
        getattr(game, self.command1)(self)


def play(game):
    player = Player()
    while True:
        player.try_play(game)
