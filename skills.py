import json

SKILL_TABLE, POINT_TABLE = {}, {}
with open('./skills.json', 'r') as file:
    SKILL_TABLE = json.load(file)

with open('./skillpoints.json', 'r') as file:
    POINT_TABLE = json.load(file)

class Skill:
    def __init__(self, buffer, idx):
        self._buffer = buffer
        self._idx = idx

    @property
    def name(self):
        return SKILL_TABLE[self.id]

    @property
    def id(self):
        return int.from_bytes(self._buffer[self._idx:self._idx+2], byteorder='little')
    
    @id.setter
    def id(self, v):
        if v in SKILL_TABLE.keys():
            self._buffer[self._idx] = int(v).to_bytes(2, byteorder='little')

        elif v == 0:
            self.skillpoints = 0
            self._buffer[self._idx] = int(0).to_bytes(2, byteorder='little')

        elif v in SKILL_TABLE.values():
            self._buffer[self._idx] = {val : key for key, val in SKILL_TABLE.items()}[v].to_bytes(2, byteorder='little')

        elif v == None or v == '':
            self.skillpoints = 0
            self._buffer[self._idx] = int(0).to_bytes(2, byteorder='little')

    @property
    def skillpoints(self):
        return int.from_bytes(self._buffer[self._idx+2:self._idx+4], byteorder='little')

    @property
    def max_skillpoints(self):
        return POINT_TABLE[self.id]

    @id.setter
    def id(self, v):
        if v in SKILL_TABLE.keys():
            self._buffer[self._idx:self._idx+2] = int(v).to_bytes(2, byteorder='little')

    @skillpoints.setter
    def skillpoints(self, v):
        if v <= self.max_skillpoints and v >= 0:
            self._buffer[self._idx+2:self._idx+4] = int(v).to_bytes(2, byteorder='little')