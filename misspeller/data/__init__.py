from .en import symbols_map as en_symbols_map
from .ru import symbols_map as ru_symbols_map


symbols_map = {**en_symbols_map, **ru_symbols_map}


__all__ = ['symbols_map']
