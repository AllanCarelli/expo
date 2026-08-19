from Attack import Attack

def return_mutliplier(attack: Attack, enemy_type: str) -> float:
    """
    function to calculate the damage multiplier based on the type of the attack and the enemy type

    input:
    attack - Attack Object
    enemy_type - str representing enemy's type

    output:
    float - representing the multiplier that will use on the damage calculation
    """

    attack_type = attack.type

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
