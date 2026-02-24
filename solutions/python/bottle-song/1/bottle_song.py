INT_TO_STR = {0:'no',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

def recite(start, take=1):
    result = []
    while take:
        repeated_line = f"{INT_TO_STR[start].title()} green {'bottle' if start == 1 else 'bottles'} hanging on the wall,"
        result += [repeated_line, repeated_line, "And if one green bottle should accidentally fall,",
        f"There'll be {INT_TO_STR[start-1]} green {'bottle' if start-1 == 1 else 'bottles'} hanging on the wall.",]
        start,take = start-1,take-1
        if take: result.append("")
    return result
