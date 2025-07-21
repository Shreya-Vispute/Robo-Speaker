import os

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 Created by Shreya")
    while True:
        x = input("Enter what you want me to speak: ")
        if x== "q":
            os.system('''mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""Bye Bye Friend"")(window.close)")''')
            break
        command = f'''
              mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{x}"")(window.close)")
        '''
        os.system(command)


        