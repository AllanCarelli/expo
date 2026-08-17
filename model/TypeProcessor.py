def return_mutliplier(attack_type: str, enemy_type: str) -> float:
    if attack_type == "fire":
        if enemy_type == "fire":
            return 1.0
        if enemy_type == "water":
            return 0.5
        if enemy_type == "grass":
            return 2.0
    if attack_type == "water":
        if enemy_type == "fire":
            return 2.0
        if enemy_type == "water":
            return 1.0
        if enemy_type == "grass":
            return 0.5
    if attack_type == "grass":
        if enemy_type == "fire":
            return 0.5
        if enemy_type == "water":
            return 2.0
        if enemy_type == "grass":
            return 1.0
