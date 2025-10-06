import random
data = [
    {"name": "Cristiano Ronaldo", "followers_count": 615000000, "country": "Portugal", "occupation": "Professional Footballer"},
    {"name": "Lionel Messi", "followers_count": 498000000, "country": "Argentina", "occupation": "Professional Footballer"},
    {"name": "Selena Gomez", "followers_count": 429000000, "country": "USA", "occupation": "Singer & Actress"},
    {"name": "Kylie Jenner", "followers_count": 399000000, "country": "USA", "occupation": "Businesswoman & Media Personality"},
    {"name": "Dwayne Johnson", "followers_count": 397000000, "country": "USA", "occupation": "Actor & Producer"},
    {"name": "Ariana Grande", "followers_count": 380000000, "country": "USA", "occupation": "Singer & Actress"},
    {"name": "Kim Kardashian", "followers_count": 364000000, "country": "USA", "occupation": "Media Personality & Businesswoman"},
    {"name": "Beyoncé", "followers_count": 319000000, "country": "USA", "occupation": "Singer & Businesswoman"},
    {"name": "Khloé Kardashian", "followers_count": 311000000, "country": "USA", "occupation": "Media Personality"},
    {"name": "Neymar Jr", "followers_count": 218000000, "country": "Brazil", "occupation": "Professional Footballer"},
    {"name": "Taylor Swift", "followers_count": 272000000, "country": "USA", "occupation": "Singer-Songwriter"},
    {"name": "Justin Bieber", "followers_count": 292000000, "country": "Canada", "occupation": "Singer"},
    {"name": "Kendall Jenner", "followers_count": 294000000, "country": "USA", "occupation": "Model & Media Personality"},
    {"name": "Jennifer Lopez", "followers_count": 252000000, "country": "USA", "occupation": "Singer & Actress"},
    {"name": "Nicki Minaj", "followers_count": 226000000, "country": "Trinidad and Tobago", "occupation": "Rapper & Singer"},
    {"name": "Kanye West", "followers_count": 18100000, "country": "USA", "occupation": "Rapper & Producer"},
    {"name": "Miley Cyrus", "followers_count": 216000000, "country": "USA", "occupation": "Singer & Actress"},
    {"name": "Katty Perry", "followers_count": 204000000, "country": "USA", "occupation": "Singer"},
    {"name": "Kevin Hart", "followers_count": 179000000, "country": "USA", "occupation": "Comedian & Actor"},
    {"name": "Ellen DeGeneres", "followers_count": 139000000, "country": "USA", "occupation": "Comedian & TV Host"},
    {"name": "Real Madrid CF", "followers_count": 158000000, "country": "Spain", "occupation": "Football Club"},
    {"name": "FC Barcelona", "followers_count": 124000000, "country": "Spain", "occupation": "Football Club"},
    {"name": "NASA", "followers_count": 97000000, "country": "USA", "occupation": "Space Agency"},
    {"name": "Virat Kohli", "followers_count": 256000000, "country": "India", "occupation": "Cricketer"},
    {"name": "Shakira", "followers_count": 215000000, "country": "Colombia", "occupation": "Singer"},
    {"name": "LeBron James", "followers_count": 158000000, "country": "USA", "occupation": "Basketball Player"},
    {"name": "Billie Eilish", "followers_count": 110000000, "country": "USA", "occupation": "Singer"},
    {"name": "Drake", "followers_count": 144000000, "country": "Canada", "occupation": "Rapper & Singer"},
    {"name": "Rihanna", "followers_count": 152000000, "country": "Barbados", "occupation": "Singer & Businesswoman"},
    {"name": "Ed Sheeran", "followers_count": 112000000, "country": "UK", "occupation": "Singer-Songwriter"}
]

def display_account_info(account):
    name = account["name"]
    country = account["country"]
    occupation = account["occupation"]
    return f"{name},a,{occupation}, from {country}"

def check_answer(user_guess, follower1, follower2):
    if follower1 > follower2:
        if user_guess == 1:
            return True
        else :
            return False
    else :
        if user_guess == 2:
            return True
        else :
            return False

score = 0
game_over = False
account2 = random.choice(data)
while not game_over:
    account1 = account2
    account2 = random.choice(data)
    while account1 == account2:
        account1 = random.choice(data)
        account2 = random.choice(data)
    print(f"compare 1: {display_account_info(account1)}")
    print(f"compare 2: {display_account_info(account2)}")
    guess = int(input("who has more followers? Type '1' or '2' :"))
    is_correct = check_answer(guess, account1["followers_count"], account2["followers_count"])
    if is_correct:
        score += 1
        print(f"your score is {score}")
    else:
        print(f"you lose ,your final score is {score}")
        game_over = True