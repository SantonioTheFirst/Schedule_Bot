#!/usr/bin/env python3
# coding: utf-8

# In[7]:


import json, requests
from datetime import datetime
from typing import Dict, List

class Bot:
    def __init__(self, filename : str = 'schedule.json') -> None:
        assert len(filename) > 0, 'Пустое имя файла!'
        self.filename : str = filename
        self.base_url = 'https://api.telegram.org/bot1617354859:AAF_oiTlv9VYrjAbep1RJpXHkap0MPKfsBs/'
        self.chat_id = '-1001086397685' #отладка '-413206784'
        self.send_message_url = f'{self.base_url}sendMessage?chat_id={self.chat_id}&text='
        self.get_updates_url = f'{self.base_url}getUpdates?chat_id={self.chat_id}'
        
        self.eng_days : List[str] = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
        ]
        self.rus_days : List[str] = [
            'Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье'
        ]
        self.day : str = self.rus_days[self.eng_days.index(datetime.today().strftime('%A'))]
        
    
    def load_data(self) -> None:
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            self.data : Dict[str, Dict[str, Dict[str, str]]] = json.load(f)
                
            
    def send_message_with_lessons(self) -> None:
        message : str = ''
        message += self.day.upper() + '\n'
        for lesson in self.data[self.day]:
            message += f'\n\t{lesson} пара: \n'
            for key, value in self.data[self.day][lesson].items():
                message += f'\t\t{key}: {value} \n'
#         message += '\nАвтор бота @mad_clocks\n'
        requests.get(self.send_message_url + message)
        
    
    def read_comand(self) -> None:
        print(requests.get(self.get_updates_url).json())


# In[8]:


#B = Bot()


# In[9]:


#B.load_data()


# In[10]:


#B.send_message_with_lessons()


# In[116]:


#B.read_comand()

