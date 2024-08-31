import win32com.client as w

if __name__=='__main__':
    speak=w.Dispatch("SAPI.SpVoice")
    print("Welcome")
    speak.speak("Welcome")
    while True:
        x=input("ENter what you want to speak: ")
        if x=='q':
            speak.speak("say 'bye bye friend'")
            break
        command=f"{x}";
        speak.speak(command)
