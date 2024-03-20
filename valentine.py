valentine = input("Will you be my valentine? (yes/no) ").lower()
match valentine:
    case "yes" :
        print("Yay! I'm so happy you said yes!")
    case  "no" :
        print("Aww, I understand. Maybe next year? :)")
    case _ :
        print(f"Sorry, I didn't understand '{valentine}' as a valid response. Please answer with 'yes' or 'no'.")
exitcode = input("Press ENTER to exit...")