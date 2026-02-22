from pyscript import display, document, HTML

def show_signup(e):
    document.getElementById("signup_section").style.display = "block"
    document.getElementById("checker_section").style.display = "none"
    document.getElementById("players_section").style.display = "none"

def show_checker(e):
    document.getElementById("signup_section").style.display = "none"
    document.getElementById("checker_section").style.display = "block"
    document.getElementById("players_section").style.display = "none"

def show_players(e):
    document.getElementById("signup_section").style.display = "none"
    document.getElementById("checker_section").style.display = "none"
    document.getElementById("players_section").style.display = "block"

def create_account(e):
    username = document.getElementById("new_username").value
    password = document.getElementById("new_password").value

    if not username or not password:
        display("Please fill in all fields.", target="signup_output", append=False)
    else:
        display("Account created. You may now log in using your credentials.",
                target="signup_output", append=False)

def check_eligibility(e):
    reg = document.querySelector('input[name="registration"]:checked')
    med = document.querySelector('input[name="medical"]:checked')
    grade = document.getElementById("grade_level").value
    section = document.getElementById("section").value

    if not reg or not med or not grade or not section:
        display("Please complete all fields!", target='output', append=False)
        return

    if reg.value == "no":
        display("Please register online first.", target='output', append=False)
        return

    if med.value == "no":
        display("Please secure a medical clearance.", target='output', append=False)
        return

    grade = int(grade)

    if 7 <= grade <= 10:
        teams = {
            7: "Green Hornets",
            8: "Red Bulldogs",
            9: "Yellow Tigers",
            10: "Blue Bears"
        }
        display(f"Congratulations! You are part of the {teams[grade]}.",
                target='output', append=False)
    else:
        display("Intramurals are only for Grades 7-10.",
                target='output', append=False)
