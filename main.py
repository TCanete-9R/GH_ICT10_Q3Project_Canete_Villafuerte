from pyscript import display, document

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

    elif len(username) < 7:
        display("Username must contain at least 7 characters.",
                target="signup_output", append=False)

    elif len(password) < 10:
        display("Password must be at least 10 characters long.",
                target="signup_output", append=False)

    elif password.isdigit():
        display("Password must contain at least one letter.",
                target="signup_output", append=False)

    elif password.isalpha():
        display("Password must contain at least one number.",
                target="signup_output", append=False)

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
        
        images = {
            7: "https://image2url.com/r2/default/images/1771857704372-0d6456f3-d345-4d4f-a694-8e4cbee631c8.jpg",
            8: "https://image2url.com/r2/default/images/1771857684992-a4d3ac12-bdd7-4931-a2d0-8b04a411577d.jpg",
            9: "https://image2url.com/r2/default/images/1771857649943-38c4ecca-1b26-4dd7-90fb-19aa606566d0.jpg",
            10: "https://image2url.com/r2/default/images/1771857556522-bbc19453-cb69-403c-9194-81e76fa39dda.jpg"
        }

        team_name = teams[grade]
        team_img = images[grade]

        result = f"Congratulations! You are part of the {team_name}. <br><br> <img src='{team_img}' width='200'>"
        
        display(HTML(result), target='output', append=False)
        
    else:
        display("Intramurals are only for Grades 7-10.",
                target='output', append=False)
