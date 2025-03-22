import random
import re

def roll_dice(code: str) -> str:
    valid_dice_types = {3,4,6,8,10,12,20,100}

    # Try to match the input string like "2D10+5"
    match = re.match(r'(?:([0-9]*)D([0-9]+))([+-][0-9]+)?', code.strip().upper())
    #If format doesn't match return error
    if not match:
        return "Invalid input"
    
    #Extract parts from the match
    num_dice_str, dice_type_str, modifier_str = match.groups()
    #If number of dice is missing (like in "D6"), assume 1
    num_dice = int(num_dice_str) if num_dice_str else 1
    #Convert dice type to integer (like 6 from D6)
    dice_type = int(dice_type_str)
    #Convert string to int (like "+3" or "-1") default to 0
    modifier = int(modifier_str) if modifier_str else 0
    
    #Check if the dice type is valid
    if dice_type not in valid_dice_types:
        return f"Invalid dice type: D{dice_type}"
    
    #Roll the dice
    rolls = []
    for _ in range(num_dice):
        #Random rolls between 1 and dice type
        rolls.append(random.randint(1, dice_type))
    
    #Calculate the total result
    total = sum(rolls) + modifier

    # Showing individual rolls and modifier


    #str(r) for r prevede kazdy result string do stringu
    #join spoji zaznamy do jednoho stringu a da pred ne " + "
    textove_hody = []
    for r in rolls:
        textove_hody.append(str(r))

    result_string = " + ".join(textove_hody)

    if modifier != 0:
        result_string += f" {'+' if modifier > 0 else '-'} {abs(modifier)}"
    
    return f"Rolling {code}: ({result_string}) = {total}"

print(roll_dice("2D10+10"))
print(roll_dice("D6"))
print(roll_dice("D12-1"))
print(roll_dice("3D100+50"))
print(roll_dice("2D7"))  # Invalid
