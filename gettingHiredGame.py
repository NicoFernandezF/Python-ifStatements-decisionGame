print(
    """
*******************************************************************************
    ._________________.
    |.---------------.|
    ||       _:'_    ||
    ||  .'` `-' ``.  ||
    || :(it's a  .'  ||
    || :macbook):    ||
    || :         `;  ||
    ||   `._.-._.'   ||
      ---------------
    /_/_|_|_|_|_|_|_\_\ 
    \__________________/
                             /^\/^\
                             \----|
                         _---'---~~~~-_
                          ~~~|~~L~|~~~~
                             (/_  /~~--    This is you, armed with your coding skills,
                           \~ \  /  /~      your great attitude, and your big ambitions!
                         __~\  ~ /   ~~----,
                         \    | |       /  \
                         /|   |/       |    |
                         | | | o  o     /~   |
                       _-~_  |        ||  \  /
                      (// )) | o  o    \\---'
                      //_- |  |          \
                     //   |____|\______\__\
                     ~      |   / |    |
                             |_ /   \ _|
                           /~___|  /____\
*******************************************************************************
"""
)
print("Welcome to Operation GettingHired.\n")
print(
    "Your mission is to infiltrate yourself into a big tech company as an intern and get to progress in your career and develop your skills in exchange for your great efforts and contributions.\n"
)

choice0 = input(
    "You apply for a position. Do you submit a cover letter? Type 'yes' or 'no'\n"
).lower()
if choice0 == "yes" or choice0 == "no":
    choice1 = input(
        "Yep, good choice either way buddy. ChatGPT makes most of them nowadays so yeah. Anyways, where were we..? You get to meet a recruiter, do you show them your resume or your portfolio? Type 'resume' or 'portfolio'.\n"
    ).lower()
    if choice1 == "portfolio":
        choice2 = input(
            "Great, the recruiter is not blown away by your portolio but it's a good start. They ask you if you prefer to code on VSCode or Notepad. Type 'vscode' or 'notepad'.\n"
        ).lower()
        if choice2 == "vscode":
            choice3 = input(
                "Good choice young padawan. Are you a team player or you like to work solo? Type 'team' or 'solo'.\n"
            ).lower()
            if choice3 == "team":
                choice4 = input(
                    "Good, good.. They like what they see. They throw a technical question at you..: What data structure method is commonly used to implement a cache with fast retrieval and insertion operations? Type 'hashing', 'stacking' or 'linking'.\n"
                ).lower()
                if choice4 == "hashing":
                    print(
                        "Great job! The company is hiring you for their entry level role!!"
                    )
                else:
                    print("Sorry wrong answer.. Game Over.")
            else:
                print(
                    "Sorry.. Team together is more than the sum of its parts!. Game Over."
                )
        else:
            print(
                "You have to be kidding me. Do you also cook your rice on the microwave? Definitely Game Over."
            )

    else:
        print("They want to see your work. Game Over.")
