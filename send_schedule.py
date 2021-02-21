#!/usr/bin/env python3
# coding: utf-8


from Bot import Bot
import os


def main():
    B = Bot()
    B.load_data()
    B.send_schedule_message()
    os.system('notify-send "Schedule bot" "Сообщение отправлено!"')

if __name__ == '__main__':
    main()
