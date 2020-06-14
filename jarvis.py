import pyttsx3
''' 
Functionalities:
(1) Check weather (web scrap)
(2) Open browser to certain websites (D2L, lanagra, amazon, google)
(3) Search, using google
[x] (4) Get date/time
(5) Do some basic shell scripting work (test c++ code and python code)  ! typing is faster
(6) Tell a joke (web scrap jokes)
[x] (7) Answer who is the author
[x] (8) Greetings at the beginning
'''

class jarvis(object):
    
    def __init__(self, user_name=None, previous_sentence=None):
        super().__init__()
        self.previous_sentence = previous_sentence
        self.user_name = user_name
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate+25)


    def greetings(self):
        greeting_sentence = 'Hi! My name is Jarvis, and I am your personal voice assistance.'
        print('Jarvis is saying...')
        self.engine.say(greeting_sentence)
        self.engine.runAndWait()


    def who_created_you(self):
        answer = 'My creator is Ethan.'
        self.engine.say(answer)
        self.engine.runAndWait()


    def reply_date(self):
        from datetime import date
        today = date.today()
        today_in_string = today.strftime("%B %d, %Y")
        result_to_say = 'The date of today is {}'.format(today_in_string)
        print('Jarvis is saying: ' + result_to_say)
        self.engine.say(result_to_say)
        self.engine.runAndWait()
        

    def reply_time(self):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time_list = current_time.split(':')
        hours = (int)(time_list[0]) % 12
        mins = (int)(time_list[1])
        am_or_pm = ''
        if int(time_list[0]) > 12:
            am_or_pm = 'PM'
        else:
            am_or_pm = 'AM'
        result_to_say = "It's {}:{} {} right now.".format(str(hours), str(mins), am_or_pm)
        print('Jarvis is saying: ' + result_to_say)
        self.engine.say(result_to_say)
        self.engine.runAndWait()
        

    def dont_know(self):
        result_to_say = 'Sorry, I don\'t understand'
        self.engine.say(result_to_say)
        self.engine.runAndWait()

    def kevin_is_my_son(self):
        result_to_say = 'Kevin is Ethan\'s son, and he always will be'
        self.engine.say(result_to_say)
        self.engine.runAndWait()

    def reply_weather(self):
        pass

    def reply(self, user_sentence):
        if 'what' and 'date' in user_sentence:
            self.reply_date()

        elif 'what' and 'time' in user_sentence:
            self.reply_time()

        elif 'what' and 'weather':
            self.reply_weather()


        elif 'who' and 'kevin' in user_sentence:
            self.kevin_is_my_son()

        elif 'who' and ('creat' or 'created') in user_sentence:
            self.who_created_you()

        
        else:
            self.dont_know()
        