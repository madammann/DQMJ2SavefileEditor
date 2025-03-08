class GeneralData:
    def __init__(self, buffer : bytearray):
        self._buffer = buffer

    @property
    def name(self):
        return int.from_bytes(self._buffer[8:8+8], byteorder='little')
    
    @property
    def gold(self):
        return int.from_bytes(self._buffer[28:28+4], byteorder='little')

    @property
    def playtime(self):
        framecount = int.from_bytes(self._buffer[0:4], byteorder='little')
        total_secs = framecount/30
        hours = secs//(60*60)
        mins = (secs-hours*60)//(60)
        secs = secs-hours*60*60-mins*60
        return secs, mins, hours

    @property
    def bank(self):
        return int.from_bytes(self._buffer[32:32+4], byteorder='little')

    @property
    def victories(self):
        return int.from_bytes(self._buffer[332:332+2], byteorder='little')

    @property
    def scouted(self):
        return int.from_bytes(self._buffer[334:334+2], byteorder='little')

    @property
    def synthesized(self):
        return int.from_bytes(self._buffer[336:336+2], byteorder='little')

    @property
    def x(self):
        pass

    @property
    def y(self):
        pass

    @property
    def z(self):
        pass

    @property
    def position(self):
        pass

    @property
    def map(self):
        pass

    @property
    def scout_ring_upgrade(self):
        return bool(self._buffer[(15986, 0)])

    @property
    def learnt_zoom(self):
        pass

    @property
    def learnt_zip(self):
        pass

    @property
    def learnt_nose_for_treasure(self):
        pass

    @property
    def learnt_vanish(self):
        pass #complicated, seems to edit three bits

    @property
    def unlocked_areas(self):
        pass

    @property
    def menu_order(self):
        pass

    @property
    def handbook(self):
        pass

    @property
    def party_slot_one(self):
        return int.from_bytes(self._buffer[40:44], byteorder='little') #scout id return atm
    
    @property
    def party_slot_two(self):
        return int.from_bytes(self._buffer[44:48], byteorder='little') #scout id return atm
    
    @property
    def party_slot_three(self):
        return int.from_bytes(self._buffer[48:52], byteorder='little') #scout id return atm
    
    @property
    def standby_slot_one(self):
        return int.from_bytes(self._buffer[52:56], byteorder='little') #scout id return atm
    
    @property
    def standby_slot_two(self):
        return int.from_bytes(self._buffer[56:60], byteorder='little') #scout id return atm
    
    @property
    def standby_slot_three(self):
        return int.from_bytes(self._buffer[60:64], byteorder='little') #scout id return atm