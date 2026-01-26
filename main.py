from pyscript import display, document, HTML

def check_eligibility(e):
    reg_element = document.querySelector('input[name="registration"]:checked')
    med_element = document.querySelector('input[name="medical"]:checked')
    
    grade = document.getElementById("grade_level").value
    section = document.getElementById("section").value
    
    if not reg_element or not med_element or not grade or not section:
        display("𝒫𝓁𝑒𝒶𝓈𝑒 𝒸𝑜𝓂𝓅𝓁𝑒𝓉𝑒 𝒶𝓁𝓁 𝒻𝒾𝑒𝓁𝒹𝓈!", target="output", append=False)
        document.getElementById("image_container").innerHTML = ""
        return

    registration = reg_element.value
    medical = med_element.value
    grade_num = int(grade)

    # Registration logic
    if registration == "no":
        display("𝒫𝓁𝑒𝒶𝓈𝑒 𝓇𝑒𝑔𝒾𝓈𝓉𝑒𝓇 𝑜𝓃𝓁𝒾𝓃𝑒 𝒻𝒾𝓇𝓈𝓉 𝓉𝑜 𝓀𝓃𝑜𝓌 𝓎𝑜𝓊𝓇 𝓉𝑒𝒶𝓂.", target="output", append=False)
        document.getElementById("image_container").innerHTML = ""
        return
        
    # Medical clearance logic
    elif medical == "no":
        display("𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝑒𝒸𝓊𝓇𝑒 𝒶 𝓂𝑒𝒹𝒾𝒸𝒶𝓁 𝒸𝓁𝑒𝒶𝓇𝒶𝓃𝒸𝑒 𝒻𝓇𝑜𝓂 𝓉𝒽𝑒 𝒸𝓁𝒾𝓃𝒾𝒸.", target="output", append=False)
        document.getElementById("image_container").innerHTML = ""
        return

    # Eligibility and Team Assignment logic
    if 7 <= grade_num <= 10:
        team = ""
        img_url = ""
        
        # Mapping Grade Levels to Team Images via HTTPS
        if grade_num == 7:
            team = "Green Hornets"
            img_url = "https://image2url.com/r2/default/images/1769128301686-963161df-7925-401c-b8bb-fd19d9ea6d05.jpg"
        elif grade_num == 8:
            team = "Red Bulldogs"
            img_url = "https://image2url.com/r2/default/images/1769128261350-fb0d516a-14b2-4336-b729-70a56e7d72b4.jpg"
        elif grade_num == 9:
            team = "Yellow Tigers"
            img_url = "https://image2url.com/r2/default/images/1769128065235-3eff06e9-f4d8-47ec-9cd3-f4c2f38afac6.jpg"
        elif grade_num == 10:
            team = "Blue Bears"
            img_url = "https://image2url.com/r2/default/images/1769128322171-8184258e-ff9e-498a-ae1b-d97225bc6c9d.jpg"

        message = f"Congratulations!<br>You are part of the <b>{team}</b>."
        display(HTML(message), target="output", append=False)
        
        img_html = f"<img src='{img_url}' height='300' width='350' style='border: 4px solid #800000;' alt='{team}'>"
        document.getElementById("image_container").innerHTML = img_html
        
    else:
        display("Sorry, Intramurals are only for Grades 7 to 10.", target="output", append=False)
        document.getElementById("image_container").innerHTML = ""