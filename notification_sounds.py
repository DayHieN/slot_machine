import winsound

notes = {
    'do1': 261,
    'do1#': 277,
    're1': 293,
    're1#': 311,
    'mi1': 329,
    'fa1': 349,
    'fa1#': 370,
    'sol1': 392,
    'sol1#': 415,
    'la1': 440,
    'la1#': 466,
    'si1': 493,
    'do2': 523,
    'do2#': 554,
    're2': 587,
    're2#': 622,
    'mi2': 659,
    'fa2': 698,
    'fa2#': 740,
    'sol2': 784,
    'sol2#': 831,
    'la2': 880,
    'la2#': 932,
    'si2': 987,
    'do3': 1047,
    'do3#': 1109,
    're3': 1175,
    're3#': 1245,
    'mi3': 1319,
    'fa3': 1397,
    'fa3#': 1480,
    'sol3': 1568,
    'sol3#': 1661,
    'la3': 1760,
    'la3#': 1865,
    'si3': 1975,
    'do4': 2093,
    'do4#': 2217,
    're4': 2349,
    're4#': 2489,
    'mi4': 2637,
    'fa4': 2794,
    'fa4#': 2960,
    'sol4': 3136,
    'sol4#': 3322,
    'la4': 3520,
    'la4#': 3729,
    'si4': 3951,
    'do5': 4186,
    'do5#': 4435,
    're5': 4699,
    're5#': 4978,
    'mi5': 5274,
    'fa5': 5588,
    'fa5#': 5920,
    'sol5': 6272,
    'sol5#': 6645,
    'la5': 7040,
    'la5#': 7459,
    'si5': 7902,
    'do6': 8372,
    'do6#': 8869,
    're6': 9397,
    're6#': 9956,
    'mi6': 10548,
    'fa6': 11175,
    'fa6#': 11840,
    'sol6': 12544,
    'sol6#': 13290,
    'la6': 14080,
    'la6#': 14917,
    'si6': 15804,
    'do7': 16744,
    'do7#': 17739,
    're7': 18794,
    're7#': 19912,
    'mi7': 21096,
    'fa7': 22350,
    'fa7#': 23680,
    'sol7': 25088,
    'sol7#': 26581,
    'la7': 28160,
    'la7#': 29834,
    'si7': 31608,
    'do8': 33488,
}


class Notifications:

    @classmethod
    def success_notification1(cls):

        

        winsound.Beep(notes['do2'], 100)
        winsound.Beep(notes['mi2'], 100)
        winsound.Beep(notes['sol2'], 100)
        winsound.Beep(notes['do3'], 250)
        winsound.Beep(notes['sol2'], 100)
        winsound.Beep(notes['do3'], 250)
    
    @classmethod
    def success_notification2(cls):

        

        winsound.Beep(notes['mi3'], 100)
        winsound.Beep(notes['re3'], 200)
        winsound.Beep(notes['si2'], 200)
        winsound.Beep(notes['sol2'], 100)
        winsound.Beep(notes['fa2#'], 200)
        winsound.Beep(notes['sol2'], 500)
        

    @classmethod
    def something_went_wrong(cls):

        

        winsound.Beep(notes['re2'], 300)
        winsound.Beep(notes['sol1#'], 500)




