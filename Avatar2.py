import pyttsx4
import speech_recognition as sr

#open avatar

class Avatar:

    def __init__(self, name="tenOutOfTenRestraunt Bot"): # constructor method, name will default to elsa if you don't add name
        self.name = name
        self.initVoice()
        self.initSR()
        # self.introduce()

    def initSR(self):
        self.sample_rate = 48000
        self.chunk_size = 2048
        self.r = sr.Recognizer()
        self.userSR = True #set this to True if using Speech Recognition

    def initVoice(self):
        '''
        Method: Initialise Text to Speech
        '''
        self.__engine = pyttsx4.init()
        self.__voices = self.__engine.getProperty('voices')
        self.__vix = 2
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)
        self.__engine.setProperty('rate', 150)
        self.__engine.setProperty('volume', 1.0)

    def say(self, words):
        self.__engine.say(words, self.name)
        self.__engine.runAndWait()
    
    def listen(self, prompt = "I am listening, please speak: ",useSR = True):
        words =""
        if not useSR:
            useSR = self.userSR
        if useSR:
            try:
                #print(sr.Microphone.list_microphone_names())
                with sr.Microphone(sample_rate=self.sample_rate, chunk_size=self.chunk_size) as source:
                    # listen for 1 second to calibrate the energy threshold for ambient noise levels
                    self.r.adjust_for_ambient_noise(source)
                    self.say(prompt)
                    audio = self.r.listen(source)
                try:
                    #print("You said: '" + r.recognize_google(audio)+"'")
                    words = self.r.recognize_google(audio)
                except sr.UnknownValueError:
                    self.say("Could not understand what you said.")
                except sr.RequestError as e:
                    self.say("Could not request results; {0}".format(e))

            except:
                self.say(prompt, True)
                words = input(": ")
        else:
            self.say(prompt, False)
            words = input(": ")
        return words

    def introduce(self):
        self.say(f"Hello. My name is {self.name}")

# This is our test harness - that tests the Avatar functions to see if they work properly
def main():
    teacher = Avatar("Owen Calleia")
    teacher.say("How are you today?")
    print("hello")
    #word = "hello"
    #for letter in word:
    #    teacher.say(letter)
    teacher.say(f"You said: {teacher.listen("say something: ")}")

if __name__ == "__main__":
    main()