

def owl_count(intake: str) -> int:
    intake = intake.lower()
    if "owl" in intake:
        total = 0
        for i in intake.split():
            if i == "owl":
                total += 1
        return total
    return  0

text = "Did you know that an owl has eyes that are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl too."
print(owl_count(text))