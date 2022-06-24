# Main File for ValoTools

# Imports
from os import system as runCommand
from time import sleep as wait
from random import choice
from text_ui import textUI

# Variables
ascentListAppended = False

# Functions
def selectUI():
    runCommand("title ValoTools - Selecting UI Type")
    print("ValoTools\n---------------------------\nSelect your UI type.\n1. Text-based\n2. Graphics-based\n")

    uiChoice = input()

    if uiChoice == "1":
        print("\nLoading text-based ui...")
        wait(1)
        textUI()
    elif uiChoice == "2":
        print("\nGraphics-based ui is in progress, loading text-based ui...")
        wait(1)
        textUI()
    else:
        print("\nNot a valid option. Select 1 or 2.\n")
        selectUI()

# Call Function
selectUI()