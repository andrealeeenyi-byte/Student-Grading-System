# Calculate grades with colors
def calculate_grade(marks):

    if marks >= 80:
        return (f"{TextColors.GREEN_BOLD}A{TextColors.RESET}")
    elif marks >= 70:
        return (f"{TextColors.GREEN_BOLD}B{TextColors.RESET}")
    elif marks >= 60:
        return (f"{TextColors.YELLOW_BOLD}C{TextColors.RESET}")
    elif marks >= 50:
        return (f"{TextColors.YELLOW_BOLD}D{TextColors.RESET}")
    elif marks >= 40:
        return (f"{TextColors.YELLOW_BOLD}E{TextColors.RESET}")
    else:
        return (f"{TextColors.RED_BOLD}F{TextColors.RESET}")