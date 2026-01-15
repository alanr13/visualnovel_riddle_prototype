label riddle:

    "Co robisz?"

    while(True):
        menu:
            "Plaża":
                call plaza
            # "Bagażnik":

            # "Woda":
            
    return

label plaza:
    default powrot = False
    "Co robisz?"
    while(True):
        if(hunterVisited == True and szpilkaObtained == True):
            menu:
                "Powrót":
                    return

        elif(hunterVisited == True and szpilkaObtained == False):
            menu:
                "Szpilka":
                    "W szpilkach na takim obozie chodzi. Co za idiotka."
                    $szpilkaObtained = True
                "Powrót":
                    return
        
        elif(hunterVisited == False and szpilkaObtained == True):
            menu:
                "Hunter":
                    h "Nie potrzebujemy cię w naszym składzie."
                    $hunterVisited = True
                "Powrót":
                    return
        
        else:
            menu:
                "Hunter":
                    h "Nie potrzebujemy cię w naszym składzie."
                    $hunterVisited = True
                "Szpilka":
                    "W szpilkach na takim obozie chodzi. Co za idiotka."
                    $szpilkaObtained = True
                "Powrót":
                    return
    
    

