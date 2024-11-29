from enum import Enum

class Turn(Enum):
    NONE = 0
    AI = 1
    HUMAN = 2

    @classmethod
    def from_int(cls, turn: int):
        if turn == 1:
            return cls.AI
        elif turn == 2:
            return cls.HUMAN
        else:
            raise ValueError("Invalid turn")

class Mode(Enum):
    MINIMAX = "minimax"
    PRUNING_MINIMAX = "pruning_minimax"
    EXPECTED_MINIMAX = "expected_minimax"

    @classmethod
    def from_int(cls, mode: int):
        if mode == 0:
            return cls.MINIMAX
        elif mode == 1:
            return cls.PRUNING_MINIMAX
        elif mode == 2:
            return cls.EXPECTED_MINIMAX
        else:
            raise ValueError("Invalid mode")