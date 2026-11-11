
# SKILLS TEST - 2ND QUARTER
from pyscript import document


# THE VOLLEYBALL POSITIONS DICTIONARY WITH THE POSITIONS, DESCRIPTIONS, PHYSICAL REQUIREMENTS, AND SKILLS REQUIRED TO PLAY THE ROLE~~~
Volleyball_positions = {
    "Setter": (
        "KING OF THE COURT - responsible for setting up the ball for attackers,controlling the game",
        "Agility, coordination, and endurance",
        "Accurate setting, decision-making,game reading, and communication"
    ),
    "Outside Hitter": (
        "WING SPIKER - Primary attacker on the front row, responsible for scoring points and receiving serves",
        "Strength, high vertical leap, and endurance",
        "Spiking, passing, communication, and receiving"
    ),
    "Middle Blocker": (
        "THE TEAM WALL - Defends the net and blocks opponents' attacks",
        "Height, high veritcal leap, and  agility",
        "Blocking, quick attacks, communication, and timing"
    ),
    "Opposite Hitter": (
        "WING ATTACKER - Attacks from the opposite side of the court, scoring when needed",
        "Strength, high vertical leap, and coordination",
        "Spiking, blocking, communication, and attacking"
    ),
    "Libero": (
        "TEAM DEFENDER - Specialized defensive player who wears a different colored jersey, protecting the backline",
        "Agility, speed, and endurance",
        "Digging, passing, communication, and receiving"
    ),
    "Defensive Specialist": (
        "TEAM ALL ROUNDER - Focuses on defense and serves as a backup for various positions",
        "Agility, coordination, and endurance",
        "Digging, passing, communication, and serving"
    )
}


#WE WILL USE THIS TO DISPLAY THE INFORMATION ABOUT THE VOLLEYBALL POSITION ENTERED BY THE USER
def element_checker(e):
    #THIS FUNCTION CLEARS THE PREVIOUS RESULTS TO PREVENT THE USER FROM GETTING A HEADACHE IF THEY INPUT THE WRONG INFO
    document.getElementById("result").innerHTML = ""

    # GETS THE ENTERED VOLLEYBALL POSSITION FROM THE INPUT FIELD AND FORMATS IT
    element1 = document.getElementById("element_name").value.strip().title()

    """
    LOKS UP THE VOLLEYBALL POSITION IN THE DICTIONARY AND RETURNS
    THE DESCRIPTION, PHYSICAL REQUIREMENTS, AND SKILLS REQUIRED.
    IF NOT FOUND, IT RETURNS A DEFAULT MESSAGE SET HERE
    """
    result = Volleyball_positions.get(
        element1, ("Position not found!", "-", "-")
    )

    # DISPLAYS THE RESULTS IN THE HTML PAGE USING F-STRINGS AND FORMATTING
    document.getElementById("result").innerHTML = f"""
        <b>Position:</b> {element1}<br>
        <b>Description:</b> {result[0]}<br>
        <b>Physical Requirements:</b> {result[1]}<br>
        <b>Skills Required:</b> {result[2]}
    """
