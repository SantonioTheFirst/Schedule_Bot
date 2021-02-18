#!/usr/bin/env python3
# coding: utf-8


from Bot import Bot


def main():
    B = Bot()
    B.load_data()
    B.send_message_with_lessons()

if __name__ == '__main__':
    main()
