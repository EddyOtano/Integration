__author__ = "Eddy Otano-Hidalgo"
# This program will calculate the chance of being admitted to an University
# based on user input, then tell user if they "got accepted" or not.
# w3schools.com was a good help.
# Every requirement listed for every sprint is in here.

# Design plan
# Select from predesignated list of colleges
# Amount of credits
# GPA
# SAT
# Meaningful Extracurriculars
# In state or out of state

Schools = ["UF", "FSU", "UCF", "FIU", "FGCU"]
# List of supported schools that will be paired with other lists with
# admissions info.

# Average GPAs and SAT scores come from school websites for class of 2025.
# Average GPA is weighted on 5 point scale.
# Acceptance rate come from U.S. News rankings for class of 2024.
# ExampleSchool = [AvgGPA,AvgSAT,AcceptanceRate]
UF = [4.5, 1400, 31]
FSU = [4.4, 1325, 32]
UCF = [4.25, 1325, 45]
FIU = [4.0, 1195, 58]
FGCU = [4.0, 1141, 77]


# On a sidenote, there is no way FGCU actually has an Average HS GPA of 4.
# Biggest lie I've ever seen.

# I have decisions from these universities to compare calculations against.
# For more accuracy, more decisions from other students would be needed.

def tryLoop(function):  # Prevents crashes by looping until answered correctly.
    trying = True
    retry = False
    while trying:
        try:
            x = function()
            if x != "redo":
                retry = False
                return (x)
            else:
                retry = True
        except:
            print("Invalid input. Please respond according to instructions.\n")
        else:
            if not retry:
                trying = False
            else:
                print(
                    "Invalid input. Please respond according to "
                    "instructions.\n")
                retry = False


def AskSchool():
    SelectSchool = str(input()).upper()
    if SelectSchool == "FGCU":
        SelectSchool = FGCU
    elif SelectSchool == "FIU":
        SelectSchool = FIU
    elif SelectSchool == "FSU":
        SelectSchool = FSU
    elif SelectSchool == "UCF":
        SelectSchool = UCF
    elif SelectSchool == "UF":
        SelectSchool = UF
    else:
        return ("redo")
    return (SelectSchool)


def AskGPA():
    GPA = float(input("What is your current GPA?\
 Enter a decimal in number form, not alphabetically.\n"))
    return (GPA)


def AskSAT():
    SAT = int(input("What is your SAT score?\
 Enter a whole number in number form, not alphabetically.\n"))
    return (SAT)


def AskExtras():
    Extras = int(input("How many MEANINGFUL extracurriculars have you "
                       "taken?\ Meaningful meaning an impactful club, "
                       "head or key member of a club, top player\ in sports "
                       "team, etc.\nAlso, add 1 to this number for every 50 "
                       "hours of\ volunteering done.\ Type in numerical form "
                       "as a whole number.\n"))
    return (Extras)


running = True
while running:
    print("Start" + "ing" + ("." * 3))
    for x in range(5):
        print(x + 1)
    # For strings, + combines strings, * repeats strings by that amount.
    print("Hello, this program will attempt to calculate the chances of you "
          "being \ admitted into an University from a predesignated list of "
          "choices.")
    print("Co", end="")
    print("ntinue?")
    print("Type", "yes", "if", "you", "wish", "to", "continue.", sep=" ")

    if str(input()).upper() == "YES":  # User wants to continue
        print("Please type the name of one of the Universities listed below "
              "that\ you want your chance of admission to be calculated for\ "
              ", exactly as seen in the list.")
        for i in Schools:  # Prints out the names of the schools
            print(i)
        SelectSchool = tryLoop(AskSchool)
        GPA = 0
        GPA += tryLoop(AskGPA)
        SAT = tryLoop(AskSAT)
        Extras = tryLoop(AskExtras)
        # / = divide, * = multiply, + = add, - = subtract
        PretentiousnessLevel = 9 / (SelectSchool[2] * .1)
        # "Pretentiousness level" goes up the lower the acceptance rate.
        # "Pretentiousness level" determines the amount of extracurriculars
        # and volunteering required.
        # // does division and cuts off decimal, ** does exponentiation
        # % gets remainder
        ChanceBase = ((GPA / SelectSchool[0]) / 2 + (
                SAT / SelectSchool[1]) / 2 + (
                              Extras / PretentiousnessLevel)) / 1.8
        ChanceEllipticIntegral = ChanceBase - (
                (1 // (SelectSchool[2])) * .01) ** (
                                         ChanceBase % PretentiousnessLevel)
        # Some further "refinement" to the chance to make it more "accurate."
        if SAT == 69:
            print("Please keep numbers appropiate for school!")
        if Extras != 0:
            print("Look at you, being an overachiever.")
        if SAT <= 1000 and GPA <= 2:
            print("Wow, the school system really failed you.")
        elif SAT >= 1500 or GPA >= 4:
            print("Or maybe the school system failed me.")
        if SelectSchool != FGCU:
            print("Yea, I'm thinking of switching too.")
        if ChanceEllipticIntegral >= .7:
            print("\nYou're probably getting accepted.\n")
        elif ChanceEllipticIntegral >= .5:
            print("\nYou may or may not get accepted, it's hard to tell,\
 you may also get put on a summer semester or a waitlist.\n")
        else:
            print("\nYou're probably not getting accepted.\n")
