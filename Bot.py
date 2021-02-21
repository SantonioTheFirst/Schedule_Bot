#!/usr/bin/env python
# coding: utf-8

# In[333]:


#https://github.com/SantonioTheFirst/Schedule_Bot
import json, requests, os
from datetime import datetime
from typing import Dict, List


#отладка '-413206784'
class Bot:
    def __init__(self, filename : str = 'schedule.json') -> None:
        assert len(filename) > 0, 'Пустое имя файла!'
        
        with open('token.txt', 'r', encoding = 'utf-8') as f:
            self.base_url : str = f.read().replace('\n', '')

        self.filename : str = filename
        self.send_message_url : str = f'{self.base_url}sendMessage?'
        self.send_photo_url : str = f'{self.base_url}sendPhoto?'
        self.photo_url : str = 'https://drive.google.com/file/d/1mOOgEoCm2UAV5Vgmj1WmXSJ8e3VSC5jk/view?usp=sharing'
        
        #нужно для того, чтобы связать кириллические названия дней в .json файле и английские названия дней
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
           
        #текущий день на русском
        self.day : str = self.rus_days[self.eng_days.index(datetime.today().strftime('%A'))]
        
        
    def __repr__(self) -> str:
        '''
        Возвращает текстовое представление объекта.
        '''
        return f'Telegram bot:\n\tbase_url = {self.base_url}\n\tfilename = {self.filename}\n\tday = {self.day}'
        
    
    def load_data(self) -> None:
        '''
        Данный метод загружает содержимое .json'а в словарь.
        '''
        
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            self.data : Dict[str, Dict[str, Dict[str, Dict[str, str]]]] = json.load(f)
                
    
    def read_comand(self) -> None:
        '''
        Считывает и выводит (пока что) команды из чатов.
        Мне пока что лень запариваться с этим функционалом, ибо тогда комп должен
        все время быть включенным, а скрипт все время слушать чаты. В дальнейшем, если будет 
        переезд на полноценный хостинг, то эта функция, будет реализована и позволит получать
        расписание на сегодня/неделю вперед и тд.
        '''
        
        print(requests.get(self.get_updates_url).json())
        
        
    def send_schedule_message(self) -> None:
        '''
        Формирует и отправляет сообщения по чатам. 
        '''
        
        for group in self.data:
            chat_id = self.data[group]['chat_id']['id']
            if self.day in self.data[group]['days']:
                message = f'🔴🔴🔴\n{group.upper()} {self.day.upper()}:\n\n'
                for lesson in self.data[group]['days'][self.day]:
                    message += '🔶'
                    for key, value in self.data[group]['days'][self.day][lesson].items():
                        message += f'{key}: {value}\n'
                    message += '\n'
                message += '\n'
                url = f'{self.send_photo_url}chat_id={chat_id}&photo={self.photo_url}&caption='
                requests.get(url + message)
                title = f'🟢{group.upper()} отправлено'
            else:
                title = f'🔴{group}: нет дня {self.day.lower()}'
            os.system(f'notify-send \'{title}\'')
    
    
    def send_custom_message_to_all(self, message : str) -> None:
        '''
        Позволяет админу сделать рассылку произвольного сообщения по всем чатам.
        '''
        
        for group in self.data:
            chat_id = self.data[group]['chat_id']['id']
            url = f'{self.send_message_url}chat_id={chat_id}&text={message}'
            requests.get(url)
            os.system(f'notify-send \'🟢{group.upper()} отправлено\'')
    
    
    def send_custom_message_to_current_chat(self, message : str, chat_id : str = '-413206784') -> None:
        '''
        Отправка сообщения в определенный чат.
        '''
        
        url = f'{self.send_message_url}chat_id={chat_id}&text={message}'
        requests.get(url)
        os.system(f'notify-send \'🟢{chat_id} отправлено\'')
        
    
    '''
    В дальнейшем, если данный бот зайдет группам ФИ, ФБ, ФФ и ФЕ, возможен перенос бота на
    полноценную библиотеку с апишкой телеги. Но пока и этого хватает с головой.
    '''

