import os
from datetime import datetime
from math import log

class SaveFile:
    def __init__(self, path : str):
        self.path = path
        self.load()

    def __len__(self):
        return len(self._buffer)

    def save(self, path=None):
        with open(self.path if path is None else path, 'wb+') as file:
            self._buffer[0x0:0x2] = self._MAGIC_BYTES #Magic bytes
            self._buffer[0x90:] = self._data #overwrite data

            self._buffer[0x88:0x8B+1] = self._checksum(self._buffer[144:], 26884).to_bytes(4, 'little') #data checskum
            self._buffer[0x8C:0x8F+1] = self._checksum(self._buffer[:0x8B+1], 144-4).to_bytes(4, 'little') #header checksum
            
            file.write(self._buffer)

    def load(self, path=None):
        p = self.path if path is None else path
        with open(p, 'rb') as file:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_path = os.path.normpath(f'./backups/backup_{timestamp}.sav')
            with open(backup_path, 'wb+') as backup:
                content = file.read()
                backup.write(content)
                self._buffer = bytearray(content)

        self._MAGIC_BYTES = self._buffer[0x0:0x2]
        self._data = bytearray(self._buffer[0x90:])

        backups = sorted(os.listdir('./backups'), key=lambda x: os.path.getctime(os.path.join('./backups', x)))
        if len(backups) > 10:
            os.remove(os.path.join('./backups', backups[0]))

    def _checksum(self, bytes_ : bytes | bytearray, size : int):
        num, i, j = 0, 0, 0
        while i < size:
            value = int.from_bytes(bytes_[j*4:j*4+4], byteorder='little')
            num += value
            num = num & 0xffffffff
            i += 4
            j += 1
        return num
    
    @property
    def buffer(self):
        return self._data
    
    def __setitem__(self, i : int|slice|tuple, v : int|bytes|bytearray|bool):
        if isinstance(v, (int, bytes, bytearray)):
            if isinstance(v, int):
                length = int(log(v, 8))
                length += 1 if length % 8 != 0 else 0
                self._data[slice(start=i, stop=i+length) if isinstance(i, int) else i] = v.to_bytes(length, byteorder='little')
            
            else:
                self._data[slice(start=i, stop=i+len(v)) if isinstance(i, int) else i] = v
        
        elif isinstance(v, bool) and isinstance(i, tuple):
            byte_ = self._data[i[0]]
            mask = 1 << i[1]
            if v:
                byte_ |= mask
            else:
                byte_ &= ~mask
            self._data[i[0]] = byte_

        else:
            raise TypeError(f'Can only write bytes or bits, not {type(v)}, writing bit requires tuple index of byte id and bit id.')

    def __getitem__(self, i : int|slice|tuple):
        if isinstance(i, (int, slice)):
            return self._data[i]
        
        elif isinstance(i, tuple):
            byte_ = self._data[i[0]]
            return bool(byte_ & (1 << i[1]))
    
    @property
    def intbuffer(self):
        return [b for b in self._data]