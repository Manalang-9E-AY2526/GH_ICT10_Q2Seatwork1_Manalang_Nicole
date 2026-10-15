# Theater Club Member Checker
from pyscript import document


def verify_candidate(e):
    # list of theater club members
    club_members = [
        "nicole manalang",
        "alyanna barlisan",
        "shiloh briones",
        "sheirhalyn gaddi",
        "cady bower",
        "maryam ledesma",
        "josua ortiz",
        "mocha manalang"
    ]

    # get and combine the entered names
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name} {last_name}".strip()

    # check if the name is on the list
    member_checker = candidate_name.lower() in club_members

    # choose a message using the boolean result
    messages = (
        f"Sorry {candidate_name}, your name is not on the list.",
        f"Congratulations {candidate_name}! You are now part of the Theater Club."
    )

    # show the result
    document.getElementById("result").innerHTML = messages[member_checker]
