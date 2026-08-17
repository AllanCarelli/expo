class Attack:
    def __init__(self, type: str, use: str, attack_type: str, accuracy: float, power: int = 0, special_buff: int = 0, special_atribute: str = None) -> None:
        self.power = power
        self.type = type
        self.use = use
        self.attack_type = attack_type
        self.accuracy = accuracy
        self.special_buff = special_buff
        self.special_atribute = special_atribute
