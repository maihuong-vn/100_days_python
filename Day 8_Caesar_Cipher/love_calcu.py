def calculate_love_score(name1, name2):
    
    #Combine names and convert to lowercase as we count the letters from BOTH NAMES
    combined_names = (name1 + name2).lower()

    #Counting the letters in TRUE and LOVE
    true_str = "TRUE"
    love_str = "LOVE"
    true_count = 0
    love_count = 0

    for char in true_str:
        true_count += combined_names.count(char.lower())

    for char in love_str:
        love_count += combined_names.count(char.lower())

    #Calculating the love score by combining the counts
    love_score = int(str(true_count) + str(love_count))
    
    
    print(f"Your love score is: {love_score}.")
    
    
calculate_love_score("Donald Trump", "Joe Biden")