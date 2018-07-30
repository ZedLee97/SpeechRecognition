import speech_recognition as sr
import time

def extract_data_from_sentence(result,keyword,stopcommand):
    #extract command or data from user's speech
    
    if result.find(stopcommand)>=0:
        print("Quiting Program")
        return [None,True]
            
    elif result.find(keyword)>=0:
        print(result[len(keyword):])
        return [result[len(keyword):],False]

    else:
        print("Bad input, please repeat")
        return [None,False]


def recognize_speech_from_mic(recognizer, microphone):
    # recieve input from microphone
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity and recieve input
    with microphone as source:
        print("Please get ready to speak, say 'stop' if you want to quit")
        r.adjust_for_ambient_noise(source)
        print("start")
        audio = r.listen(source)
        result = r.recognize_google(audio)
        keyword = "this is "
        stopcommand = "stop"
        return extract_data_from_sentence(result,keyword,stopcommand)
    
        
        
        
        
if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    Time_to_Stop=False
    while(not(Time_to_Stop)):
        time.sleep(1)
        [data,Time_to_Stop] = recognize_speech_from_mic(r, mic)
        
        
        
        
        

