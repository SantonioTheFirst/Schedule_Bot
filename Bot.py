#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json, requests
from datetime import datetime
from typing import Dict, List

class Bot:
    def __init__(self, filename : str = 'schedule.json') -> None:
        assert len(filename) > 0, 'Пустое имя файла!'
        self.filename : str = filename
        self.base_url = 'https://api.telegram.org/bot1617354859:AAF_oiTlv9VYrjAbep1RJpXHkap0MPKfsBs/'
#         self.chat_id = '-1001086397685' #отладка '-413206784'
        self.send_message_url = f'{self.base_url}sendMessage?' #'#chat_id={self.chat_id}&text='
#         self.get_updates_url = f'{self.base_url}getUpdates?chat_id={self.chat_id}'
        
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
#             self.data : Dict[str, Dict[str, Dict[str, str]]] = json.load(f)
            self.data = json.load(f)
                
            
    def send_message_with_lessons(self) -> None:
        message : str = ''
        message += self.day.upper() + '\n'
        for group in self.data:
            if self.day in self.data[group]['days']:
                for lesson in self.data[group]['days'][self.day]:
                    message += f'\n\t{lesson} пара: \n'
                    for key, value in self.data[group]['days'][self.day][lesson].items():
                        message += f'\t\t{key}: {value} \n'
        #         message += '\nАвтор бота @mad_clocks\n'
                for chat_id in self.data[group]['chat_id']['id']:
                    url = self.send_message_url + f'chat_id={chat_id}&text={message}'
                print(url)
                requests.get(url + message)
        
    
    def send(self) -> None:
        for group in self.data:
            if self.day in self.data[group]['days']:
                message = f'🔴🔴🔴\n{group}\t{self.day}:\n\n'
                for lesson in self.data[group]['days'][self.day]:
                    for key, value in self.data[group]['days'][self.day][lesson].items():
                        message += f'\t{key}: {value}\n'
                    message += '\n'
                message += '\n'
                url = self.send_message_url + f'chat_id={self.data[group]["chat_id"]["id"]}&text='
                requests.get(url + message)
        
    
    def read_comand(self) -> None:
        print(requests.get(self.get_updates_url).json())


# In[153]:


#B = Bot()


# In[154]:


#B.load_data()


# In[155]:


#B.send()

