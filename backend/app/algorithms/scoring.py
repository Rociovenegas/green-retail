def calculate_sustainability_score(
    pollution_score: float,
    social_score: float,
    economic_score: float,
    pollution_weight: float = 0.4,
    social_weight: float = 0.4,
    economic_weight: float = 0.2
) -> float:
    total = (
        normalization_pollution(pollution_score)*pollution_weight + 
        normalization_social(social_score)*social_weight + 
        normalization_economic(economic_score)*economic_weight)
    
    return total


# teoricamente esto deberian ser diferentes dependiendo del valor...
def normalization_pollution( pollution_score:float ):
    return pollution_score/100

def normalization_social( social_score: float ):
    return social_score/100

def normalization_economic( economic_score: float ):
    return economic_score


