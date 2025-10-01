
def gimme_da_odds(numbers: list) -> bool:
    if numbers[0]%2==1:
        for i in numbers[1:]:
            if not i%2==1:
                return True
    else:
        for i in numbers[1:]:
            if i%2==1:
                return True
    return False


