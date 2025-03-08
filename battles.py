from monster import Monster

class Battle:
    def __init__(self, buffer, idx):
        self._buffer = buffer
        self._idx = idx

    @property
    def name(self):
        return None
    
    @property
    def wrangler_id(self):
        pass

    @property
    def victories(self):
        return None
    
    @property
    def scouted(self):
        return None
    
    @property
    def monster_rate(self):
        return None
    
    @property
    def losses(self):
        return None
    
    @property
    def monsters(self):
        monsters = [Monster(self._buffer, self._idx+int) for i in range(3)]
        return [monster for monster in monsters if monster.id != 0]