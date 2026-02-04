def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    lower_case_name = combined_name.lower()
    match_true = ['t', 'r', 'u', 'e']
    match_love = ['l', 'o', 'v', 'e']
    digit1 = 0
    digit2 = 0
    love_score = 0
    
    for letter in lower_case_name:
        if letter in match_true:
            digit1 += 1
        if letter in match_love:
            digit2 += 1
    print(f"{digit1}{digit2}")
    
    
calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
