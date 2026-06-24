#!/usr/bin/env python3
"""Generates questions_draft.json with Eltex-style distractor options."""
import json

DRAFT = [
    {
        "question": "Специалисты IT-отдела заметили, что в последние несколько лет все больше сотрудников организации заходят в корпоративную сеть со своих мобильных телефонов и планшетов. На какой сегмент сети необходимо обратить внимание специалистам IT-отдела, и возможно его перепроектировать?",
        "options": [
            {"text": "Беспроводная локальная сеть (WLAN)", "isCorrect": True},
            {"text": "Проводная локальная сеть (LAN)", "isCorrect": False},
            {"text": "Глобальная сеть (WAN)", "isCorrect": False},
            {"text": "Демилитаризованная зона (DMZ)", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 8)"
    },
    {
        "question": "Что такое Интернет?",
        "options": [
            {"text": "Средство обеспечения подключений через взаимно подключенные глобальные сети", "isCorrect": True},
            {"text": "Частная корпоративная сеть, используемая только внутри одной организации", "isCorrect": False},
            {"text": "Протокол передачи данных между устройствами в локальной сети", "isCorrect": False},
            {"text": "Набор правил и стандартов для обмена данными в пределах одного здания", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 11)"
    },
    {
        "question": "В каком году передано первое в мире сообщение по компьютерной сети?",
        "options": [
            {"text": "1969", "isCorrect": True},
            {"text": "1976", "isCorrect": False},
            {"text": "1984", "isCorrect": False},
            {"text": "1991", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 21)"
    },
    {
        "question": "Какими методами малые и крупные предприятия могут подключиться к поставщику услуг Интернет? (Выберите три варианта)",
        "options": [
            {"text": "Выделенная арендованная линия", "isCorrect": True},
            {"text": "Спутниковая связь", "isCorrect": True},
            {"text": "DSL", "isCorrect": True},
            {"text": "Bluetooth-соединение", "isCorrect": False},
            {"text": "Подключение через USB-модем", "isCorrect": False},
            {"text": "Инфракрасная связь", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 35)"
    },
    {
        "question": "Зачем нужно кодирование сообщений при передаче данных по сетевой среде? (Выберите два варианта)",
        "options": [
            {"text": "Чтобы интерпретировать информацию.", "isCorrect": True},
            {"text": "Чтобы преобразовать информацию в формат, пригодный для передачи.", "isCorrect": True},
            {"text": "Чтобы сжать данные и уменьшить объём трафика.", "isCorrect": False},
            {"text": "Чтобы защитить данные от несанкционированного доступа.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 46)"
    },
    {
        "question": "Какое общее число комбинаций восьми битов в 8-битовом байте?",
        "options": [
            {"text": "256", "isCorrect": True},
            {"text": "128", "isCorrect": False},
            {"text": "512", "isCorrect": False},
            {"text": "64", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 89)"
    },
    {
        "question": "Укажите компоненты IP-конфигурации, которые используются для определения подсети компьютера. (Выберите два варианта)",
        "options": [
            {"text": "IP-адрес", "isCorrect": True},
            {"text": "Маска подсети", "isCorrect": True},
            {"text": "MAC-адрес сетевого адаптера", "isCorrect": False},
            {"text": "Адрес шлюза по умолчанию", "isCorrect": False},
            {"text": "Адрес DNS-сервера", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 91)"
    },
    {
        "question": "Какая маска подсети по умолчанию выделяет минимальное количество бит для адресации узлов в подсети?",
        "options": [
            {"text": "255.255.255.252", "isCorrect": True},
            {"text": "255.255.255.0", "isCorrect": False},
            {"text": "255.255.255.128", "isCorrect": False},
            {"text": "255.255.0.0", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 94)"
    },
    {
        "question": "Какие адреса можно использовать в качестве частных IP-адресов в локальной сети? (Выберите два варианта)",
        "options": [
            {"text": "10.10.1.200", "isCorrect": True},
            {"text": "172.31.100.254", "isCorrect": True},
            {"text": "172.32.10.5", "isCorrect": False},
            {"text": "192.169.10.1", "isCorrect": False},
            {"text": "11.0.0.1", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 97)"
    },
    {
        "question": "Какой IP-адрес назначения используется в пакете при одноадресной рассылке?",
        "options": [
            {"text": "Адрес заданного узла", "isCorrect": True},
            {"text": "Адрес группы узлов", "isCorrect": False},
            {"text": "Широковещательный адрес подсети", "isCorrect": False},
            {"text": "Адрес шлюза по умолчанию", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 98)"
    },
    {
        "question": "Учитель обращается ко всем ученикам в классе. К какому типу рассылки относится данное сообщение?",
        "options": [
            {"text": "Широковещательная", "isCorrect": True},
            {"text": "Одноадресная", "isCorrect": False},
            {"text": "Многоадресная", "isCorrect": False},
            {"text": "Групповая адресация", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 99)"
    },
    {
        "question": "Какую функцию выполняют логические адреса в IP-сети?",
        "options": [
            {"text": "Определение сети, в которой расположен узел", "isCorrect": True},
            {"text": "Идентификация физического устройства на канальном уровне", "isCorrect": False},
            {"text": "Шифрование данных при передаче между узлами", "isCorrect": False},
            {"text": "Управление скоростью передачи данных между узлами", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 104)"
    },
    {
        "question": "Сколько бит в записи адреса IPv4?",
        "options": [
            {"text": "32 бита", "isCorrect": True},
            {"text": "64 бита", "isCorrect": False},
            {"text": "16 бит", "isCorrect": False},
            {"text": "128 бит", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 107)"
    },
    {
        "question": "Какой класс IPv4 чаще других обеспечивает большинство сетей?",
        "options": [
            {"text": "Класс C", "isCorrect": True},
            {"text": "Класс A", "isCorrect": False},
            {"text": "Класс B", "isCorrect": False},
            {"text": "Класс D", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 109)"
    },
    {
        "question": "Какой класс IPv4 обеспечивает максимальное количество адресов узлов в расчёте на одну сеть?",
        "options": [
            {"text": "Класс A", "isCorrect": True},
            {"text": "Класс B", "isCorrect": False},
            {"text": "Класс C", "isCorrect": False},
            {"text": "Класс D", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 112)"
    },
    {
        "question": "Какой IP-адрес назначения используется в пакете при многоадресной рассылке?",
        "options": [
            {"text": "Адрес группы узлов", "isCorrect": True},
            {"text": "Адрес заданного узла", "isCorrect": False},
            {"text": "Широковещательный адрес подсети", "isCorrect": False},
            {"text": "Адрес шлюза по умолчанию", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 113)"
    },
    {
        "question": "Компания использует сетевой адрес 192.168.8.0 с маской 255.255.255.224 для создания подсетей. Какое максимальное количество узлов, пригодных для использования в каждой подсети?",
        "options": [
            {"text": "30", "isCorrect": True},
            {"text": "14", "isCorrect": False},
            {"text": "62", "isCorrect": False},
            {"text": "126", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 114)"
    },
    {
        "question": "Какое утверждение об адресации с использованием масок подсети произвольной длины (VLSM) является верным?",
        "options": [
            {"text": "Разбиение большего адресного диапазона на более мелкие в зависимости от требований.", "isCorrect": True},
            {"text": "Использование одной маски подсети для всех подсетей в сети.", "isCorrect": False},
            {"text": "Ограничение максимального количества подсетей до восьми.", "isCorrect": False},
            {"text": "Назначение одного IP-адреса сразу нескольким узлам.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 120)"
    },
    {
        "question": "Какие IP-адреса из подсети 198.18.77.32/27 можно назначить узлам? (Выберите два варианта)",
        "options": [
            {"text": "198.18.77.60", "isCorrect": True},
            {"text": "198.18.77.35", "isCorrect": True},
            {"text": "198.18.77.32", "isCorrect": False},
            {"text": "198.18.77.63", "isCorrect": False},
            {"text": "198.18.77.64", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 121)"
    },
    {
        "question": "Компания использует сетевой адрес 192.168.8.0 с маской 255.255.255.224. Какое максимальное количество узлов, пригодных для использования в каждой подсети?",
        "options": [
            {"text": "30", "isCorrect": True},
            {"text": "14", "isCorrect": False},
            {"text": "62", "isCorrect": False},
            {"text": "126", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 127)"
    },
    {
        "question": "Сколько адресов узлов могут быть присвоены каждой подсети при использовании сетевого адреса 131.69.0.0 с маской подсети 255.255.248.0?",
        "options": [
            {"text": "2046", "isCorrect": True},
            {"text": "1022", "isCorrect": False},
            {"text": "4094", "isCorrect": False},
            {"text": "510", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 128)"
    },
    {
        "question": "Какие три IP-адреса попадут в блок сети 198.18.4.0/22? (Выберите три варианта)",
        "options": [
            {"text": "198.18.5.128", "isCorrect": True},
            {"text": "198.18.5.255", "isCorrect": True},
            {"text": "198.18.7.64", "isCorrect": True},
            {"text": "198.18.3.255", "isCorrect": False},
            {"text": "198.18.8.0", "isCorrect": False},
            {"text": "198.18.8.64", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 130)"
    },
    {
        "question": "Компания использует для внутренней адресации пространство 172.16.0.0/16 и предполагает, что ей потребуется 150 сетей. Укажите правильную маску подсети для данной конфигурации сети.",
        "options": [
            {"text": "255.255.255.0", "isCorrect": True},
            {"text": "255.255.254.0", "isCorrect": False},
            {"text": "255.255.252.0", "isCorrect": False},
            {"text": "255.255.248.0", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 133)"
    },
    {
        "question": "Если сеть имеет маску /28, сколько IP-адресов может быть назначено узлам в этой сети?",
        "options": [
            {"text": "14", "isCorrect": True},
            {"text": "6", "isCorrect": False},
            {"text": "30", "isCorrect": False},
            {"text": "62", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 134)"
    },
    {
        "question": "Какие IP-адреса являются адресом сети и широковещательным адресом для сети, в которой 192.168.33.130/27 является адресом узла? (Выберите два варианта)",
        "options": [
            {"text": "Сетевой адрес 192.168.33.128", "isCorrect": True},
            {"text": "Широковещательный адрес 192.168.33.159", "isCorrect": True},
            {"text": "Сетевой адрес 192.168.33.112", "isCorrect": False},
            {"text": "Широковещательный адрес 192.168.33.191", "isCorrect": False},
            {"text": "Широковещательный адрес 192.168.33.127", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 136)"
    },
    {
        "question": "Что является преимуществом внедрения схемы адресации VLSM? (Выберите два варианта)",
        "options": [
            {"text": "Поддерживает возможность иерархической адресации", "isCorrect": True},
            {"text": "Позволяет эффективно использовать адресное пространство", "isCorrect": True},
            {"text": "Упрощает настройку маршрутизаторов за счёт единой маски", "isCorrect": False},
            {"text": "Исключает необходимость использования частных IP-адресов", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 137)"
    },
    {
        "question": "К какому типу относится адрес 192.168.17.111/28?",
        "options": [
            {"text": "Широковещательный адрес (Broadcast Address)", "isCorrect": True},
            {"text": "Адрес узла (Host Address)", "isCorrect": False},
            {"text": "Сетевой адрес (Network Address)", "isCorrect": False},
            {"text": "Адрес многоадресной рассылки (Multicast Address)", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 140)"
    },
    {
        "question": "VLSM для организации: 500 человек — главный офис; 200 — отдел продаж; 425 — производственный отдел; 50 — отдел исследований. Сеть 172.16.0.0/16. Верная схема адресации VLSM с минимальными потерями: (Выберите четыре варианта)",
        "options": [
            {"text": "172.16.0.0/23 — главный офис", "isCorrect": True},
            {"text": "172.16.2.0/23 — производственный отдел", "isCorrect": True},
            {"text": "172.16.4.0/24 — отдел продаж", "isCorrect": True},
            {"text": "172.16.5.0/26 — отдел исследований", "isCorrect": True},
            {"text": "172.16.0.0/24 — главный офис", "isCorrect": False},
            {"text": "172.16.3.0/26 — производственный отдел", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 142)"
    },
    {
        "question": "Какие два IP-адреса можно назначить узлам, если адрес сети 192.168.99.32/27? (Выберите два варианта)",
        "options": [
            {"text": "192.168.99.35", "isCorrect": True},
            {"text": "192.168.99.60", "isCorrect": True},
            {"text": "192.168.99.32", "isCorrect": False},
            {"text": "192.168.99.63", "isCorrect": False},
            {"text": "192.168.99.64", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 143)"
    },
    {
        "question": "VLSM для организации: 850 — главный офис; 220 — отдел продаж; 425 — производственный отдел; 50 — отдел исследований. Сеть 172.17.0.0/16. Верная схема адресации VLSM с минимальной потерей адресов: (Выберите четыре варианта)",
        "options": [
            {"text": "172.17.0.0/22 — главный офис", "isCorrect": True},
            {"text": "172.17.4.0/23 — производственный отдел", "isCorrect": True},
            {"text": "172.17.6.0/24 — отдел продаж", "isCorrect": True},
            {"text": "172.17.7.0/26 — отдел исследований", "isCorrect": True},
            {"text": "172.17.0.0/23 — главный офис", "isCorrect": False},
            {"text": "172.17.5.0/24 — производственный отдел", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 144)"
    },
    {
        "question": "Компания с IP-адресом Класса B и классовой маской планирует создать 60 подсетей, в каждой из которых может быть максимум 1000 компьютеров. Какая маска подсети будет использована при наименьшем количестве неиспользованных адресов?",
        "options": [
            {"text": "255.255.252.0", "isCorrect": True},
            {"text": "255.255.255.0", "isCorrect": False},
            {"text": "255.255.248.0", "isCorrect": False},
            {"text": "255.255.254.0", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 146)"
    },
    {
        "question": "Администратор добавляет в локальную сеть новый компьютер. После загрузки ОС пользователь открывает браузер и видит, что компьютер подключён к Интернету. Благодаря чему компьютер подключился к сети без дополнительной настройки?",
        "options": [
            {"text": "На ПК по умолчанию преднастроено получение IP-адреса по протоколу DHCP.", "isCorrect": True},
            {"text": "Компьютер автоматически назначает себе статический IP-адрес.", "isCorrect": False},
            {"text": "Коммутатор автоматически настраивает параметры подключения нового устройства.", "isCorrect": False},
            {"text": "Маршрутизатор передаёт параметры подключения через протокол ICMP.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 147)"
    },
    {
        "question": "Клиент декодировал кадр и начал процесс деинкапсуляции. В каком порядке выполняется этот процесс?",
        "options": [
            {"text": "1) Удаление заголовка Ethernet. 2) Удаление IP-заголовка. 3) Удаление заголовка TCP. 4) Передача данных в приложение.", "isCorrect": True},
            {"text": "1) Удаление заголовка TCP. 2) Удаление IP-заголовка. 3) Удаление заголовка Ethernet. 4) Передача данных.", "isCorrect": False},
            {"text": "1) Удаление IP-заголовка. 2) Удаление заголовка Ethernet. 3) Удаление заголовка TCP. 4) Передача данных.", "isCorrect": False},
            {"text": "1) Передача данных в приложение. 2) Удаление заголовка TCP. 3) Удаление IP-заголовка. 4) Удаление заголовка Ethernet.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 153)"
    },
    {
        "question": "Перечислите три характеристики протокола HTTPS. (Выберите три варианта)",
        "options": [
            {"text": "Поддерживается проверка подлинности.", "isCorrect": True},
            {"text": "Шифрование пакетов с помощью протокола SSL.", "isCorrect": True},
            {"text": "Требование дополнительного времени обработки на сервере.", "isCorrect": True},
            {"text": "Передаёт данные в открытом виде без шифрования.", "isCorrect": False},
            {"text": "Использует порт 80 по умолчанию.", "isCorrect": False},
            {"text": "Не требует цифровых сертификатов.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 159)"
    },
    {
        "question": "Что преобразует URL-адрес веб-сайта в IP-адрес?",
        "options": [
            {"text": "DNS-сервер.", "isCorrect": True},
            {"text": "DHCP-сервер.", "isCorrect": False},
            {"text": "Прокси-сервер.", "isCorrect": False},
            {"text": "Веб-сервер.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 160)"
    },
    {
        "question": "Укажите назначение сообщения HTTP GET.",
        "options": [
            {"text": "Запрос веб-страницы с веб-сервера", "isCorrect": True},
            {"text": "Отправка данных формы на веб-сервер", "isCorrect": False},
            {"text": "Удаление ресурса на веб-сервере", "isCorrect": False},
            {"text": "Обновление данных на веб-сервере", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 161)"
    },
    {
        "question": "Укажите основную цель службы DNS.",
        "options": [
            {"text": "Преобразование удобных для восприятия имён доменов в числовые IP-адреса.", "isCorrect": True},
            {"text": "Автоматическое назначение IP-адресов устройствам в сети.", "isCorrect": False},
            {"text": "Маршрутизация пакетов между различными сетями.", "isCorrect": False},
            {"text": "Шифрование данных при передаче между узлами.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 163)"
    },
    {
        "question": "Какие протоколы используются для веб-хостинга и передачи данных? (Выберите два варианта)",
        "options": [
            {"text": "HTTP", "isCorrect": True},
            {"text": "DNS", "isCorrect": True},
            {"text": "FTP", "isCorrect": False},
            {"text": "SMTP", "isCorrect": False},
            {"text": "ICMP", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 167)"
    },
    {
        "question": "Когда почтовые клиенты отправляют письма, какое устройство используется для преобразования имён доменов в соответствующие IP-адреса?",
        "options": [
            {"text": "DNS-сервер", "isCorrect": True},
            {"text": "SMTP-сервер", "isCorrect": False},
            {"text": "DHCP-сервер", "isCorrect": False},
            {"text": "POP3-сервер", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 170)"
    },
    {
        "question": "Когда узел взаимодействует с несколькими приложениями на одном сервере, какие два параметра будут одинаковыми для каждого сеанса? (Выберите два варианта)",
        "options": [
            {"text": "MAC-адрес.", "isCorrect": True},
            {"text": "IP-адрес.", "isCorrect": True},
            {"text": "Номер порта источника.", "isCorrect": False},
            {"text": "Номер порта назначения.", "isCorrect": False},
            {"text": "Адрес шлюза по умолчанию.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 171)"
    },
    {
        "question": "Что происходит при инкапсуляции сегмента в пакет?",
        "options": [
            {"text": "Добавляется заголовок с логическими адресами.", "isCorrect": True},
            {"text": "Добавляется заголовок с физическими адресами.", "isCorrect": False},
            {"text": "Добавляется заголовок с номерами портов.", "isCorrect": False},
            {"text": "Добавляется концевая метка с контрольной суммой.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 172)"
    },
    {
        "question": "Что указывается в поле «размер окна» в заголовке TCP?",
        "options": [
            {"text": "Объём данных, который может обработать узел назначения за один раз.", "isCorrect": True},
            {"text": "Количество сегментов, которые могут быть переданы за один сеанс.", "isCorrect": False},
            {"text": "Максимальный размер одного сегмента в байтах.", "isCorrect": False},
            {"text": "Время ожидания подтверждения от узла назначения.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 177)"
    },
    {
        "question": "Какие два утверждения о протоколе UDP верны? (Выберите два варианта)",
        "options": [
            {"text": "Он не поддерживает подтверждение приёма данных.", "isCorrect": True},
            {"text": "Это протокол без установления соединения.", "isCorrect": True},
            {"text": "Гарантирует надёжную доставку данных.", "isCorrect": False},
            {"text": "Выполняет повторную передачу при потере пакетов.", "isCorrect": False},
            {"text": "Устанавливает соединение перед передачей данных.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 178)"
    },
    {
        "question": "Какой транспортный протокол использует FTP для передачи файлов через Интернет?",
        "options": [
            {"text": "TCP", "isCorrect": True},
            {"text": "UDP", "isCorrect": False},
            {"text": "ICMP", "isCorrect": False},
            {"text": "ARP", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 180)"
    },
    {
        "question": "Каковы три уникальные характеристики протокола UDP? (Выберите три варианта)",
        "options": [
            {"text": "Отсутствие управления потоками.", "isCorrect": True},
            {"text": "Низкие непроизводительные издержки.", "isCorrect": True},
            {"text": "Отсутствие процедуры восстановления после ошибок.", "isCorrect": True},
            {"text": "Гарантия доставки пакетов.", "isCorrect": False},
            {"text": "Установление соединения перед передачей.", "isCorrect": False},
            {"text": "Нумерация и упорядочивание сегментов.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 181)"
    },
    {
        "question": "Какая единица данных протокола (PDU) обрабатывается, когда узловой компьютер декапсулирует сообщение на транспортном уровне модели TCP/IP?",
        "options": [
            {"text": "Сегмент", "isCorrect": True},
            {"text": "Пакет", "isCorrect": False},
            {"text": "Кадр", "isCorrect": False},
            {"text": "Бит", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 182)"
    },
    {
        "question": "Какой из диапазонов является диапазоном известных портов TCP и UDP?",
        "options": [
            {"text": "0 — 1023", "isCorrect": True},
            {"text": "1024 — 49151", "isCorrect": False},
            {"text": "49152 — 65535", "isCorrect": False},
            {"text": "0 — 65535", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 185)"
    },
    {
        "question": "Укажите одну из функций «Трёхстороннего рукопожатия TCP».",
        "options": [
            {"text": "Согласование порядковых номеров сегментов между отправителем и получателем.", "isCorrect": True},
            {"text": "Шифрование данных между отправителем и получателем.", "isCorrect": False},
            {"text": "Разрыв TCP-соединения после завершения передачи данных.", "isCorrect": False},
            {"text": "Подтверждение получения всех ранее отправленных сегментов.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 186)"
    },
    {
        "question": "Какие две опции соответствуют протоколу и номеру известного порта? (Выберите два варианта)",
        "options": [
            {"text": "SMTP = 25", "isCorrect": True},
            {"text": "HTTP = 80", "isCorrect": True},
            {"text": "FTP = 443", "isCorrect": False},
            {"text": "Telnet = 25", "isCorrect": False},
            {"text": "DNS = 443", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 192)"
    },
    {
        "question": "Что произойдет, если часть сообщения FTP не будет доставлена по адресу назначения?",
        "options": [
            {"text": "Утерянная часть сообщения FTP будет отправлена повторно.", "isCorrect": True},
            {"text": "Сессия FTP будет немедленно завершена с ошибкой.", "isCorrect": False},
            {"text": "Утерянная часть будет запрошена повторно протоколом ICMP.", "isCorrect": False},
            {"text": "Данные будут переданы по альтернативному маршруту автоматически.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 194)"
    },
    {
        "question": "Какой протокол транспортного уровня будет использоваться для передачи пакетов голосовых данных клиентом, использующим VoIP?",
        "options": [
            {"text": "UDP", "isCorrect": True},
            {"text": "TCP", "isCorrect": False},
            {"text": "ICMP", "isCorrect": False},
            {"text": "SCTP", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 198)"
    },
    {
        "question": "Почему номера портов включены в заголовок TCP-сегмента?",
        "options": [
            {"text": "Чтобы принимающий узел мог переслать данные в соответствующее приложение.", "isCorrect": True},
            {"text": "Чтобы идентифицировать узел источника в сети.", "isCorrect": False},
            {"text": "Чтобы обеспечить шифрование данных при передаче.", "isCorrect": False},
            {"text": "Чтобы управлять скоростью передачи данных между узлами.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 199)"
    },
    {
        "question": "Какой флаг в TCP-заголовке используется в ответ на сообщение FIN для разрыва соединения между двумя сетевыми устройствами?",
        "options": [
            {"text": "ACK", "isCorrect": True},
            {"text": "SYN", "isCorrect": False},
            {"text": "FIN", "isCorrect": False},
            {"text": "RST", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 200)"
    },
    {
        "question": "Какие три поля заголовков TCP и UDP совпадают? (Выберите три варианта)",
        "options": [
            {"text": "Контрольная сумма.", "isCorrect": True},
            {"text": "Порт назначения.", "isCorrect": True},
            {"text": "Порт источника.", "isCorrect": True},
            {"text": "Порядковый номер.", "isCorrect": False},
            {"text": "Флаги управления.", "isCorrect": False},
            {"text": "Размер окна.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 201)"
    },
    {
        "question": "Каким образом TCP обеспечивает надёжную передачу данных?",
        "options": [
            {"text": "Если в установленный промежуток времени из пункта назначения не будет получено подтверждение передачи сегментов, исходный пункт выполнит повторную передачу данных.", "isCorrect": True},
            {"text": "TCP использует контрольные суммы для исправления ошибок непосредственно в сегментах.", "isCorrect": False},
            {"text": "TCP ограничивает скорость передачи данных для предотвращения перегрузки канала.", "isCorrect": False},
            {"text": "TCP резервирует отдельный физический канал для каждого соединения.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 204)"
    },
    {
        "question": "Какие два флага в TCP-заголовке используются при Трёхстороннем рукопожатии TCP для установления соединения? (Выберите два варианта)",
        "options": [
            {"text": "SYN", "isCorrect": True},
            {"text": "ACK", "isCorrect": True},
            {"text": "FIN", "isCorrect": False},
            {"text": "RST", "isCorrect": False},
            {"text": "URG", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 205)"
    },
    {
        "question": "Какая комбинация образует Пару сокетов TCP?",
        "options": [
            {"text": "IP-адрес и порт источника вместе с IP-адресом и портом назначения.", "isCorrect": True},
            {"text": "MAC-адрес источника и MAC-адрес назначения.", "isCorrect": False},
            {"text": "IP-адрес источника и IP-адрес назначения без портов.", "isCorrect": False},
            {"text": "Порт источника и порт назначения без IP-адресов.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 207)"
    },
    {
        "question": "Какой фактор определяет размер окна TCP?",
        "options": [
            {"text": "Объём данных, который может обработать узел назначения за один раз.", "isCorrect": True},
            {"text": "Максимальный размер одного сегмента TCP в байтах.", "isCorrect": False},
            {"text": "Время ожидания подтверждения перед повторной передачей.", "isCorrect": False},
            {"text": "Количество одновременных соединений, которые сервер может обслуживать.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 210)"
    },
    {
        "question": "Клиент взаимодействует с сервером в другом сегменте сети. Как сервер определяет, какая служба запрашивается клиентом?",
        "options": [
            {"text": "Сервер определяет необходимую службу, исходя из поля «порт назначения».", "isCorrect": True},
            {"text": "Сервер определяет необходимую службу по IP-адресу источника.", "isCorrect": False},
            {"text": "Сервер определяет необходимую службу исходя из поля «порт источника».", "isCorrect": False},
            {"text": "Сервер определяет необходимую службу по MAC-адресу клиента.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 212)"
    },
    {
        "question": "Какая информация включена в заголовок транспортного уровня?",
        "options": [
            {"text": "Номера портов назначения и источника.", "isCorrect": True},
            {"text": "Логические адреса источника и назначения.", "isCorrect": False},
            {"text": "Физические адреса источника и назначения.", "isCorrect": False},
            {"text": "Флаги управления качеством обслуживания (QoS).", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 213)"
    },
    {
        "question": "Какая характеристика сетевого уровня в модели OSI позволяет передавать пакеты для различных типов связи между большим количеством узлов?",
        "options": [
            {"text": "Выбор путей и направление пакетов к узлу назначения.", "isCorrect": True},
            {"text": "Управление доступом к физической среде передачи данных.", "isCorrect": False},
            {"text": "Добавление физических адресов к единицам данных.", "isCorrect": False},
            {"text": "Сегментация данных на небольшие части для передачи.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 227)"
    },
    {
        "question": "В чём заключается назначение сообщений ICMP?",
        "options": [
            {"text": "Сообщать об успешной доставке IP-пакета или об ошибках при его передаче", "isCorrect": True},
            {"text": "Автоматически назначать IP-адреса узлам сети.", "isCorrect": False},
            {"text": "Выполнять маршрутизацию пакетов между различными сетями.", "isCorrect": False},
            {"text": "Устанавливать защищённые соединения между узлами.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 236)"
    },
    {
        "question": "Какой уровень модели OSI отвечает за выбор метода инкапсуляции, который используется в средах передачи данных определённого типа?",
        "options": [
            {"text": "Канальный.", "isCorrect": True},
            {"text": "Сетевой.", "isCorrect": False},
            {"text": "Физический.", "isCorrect": False},
            {"text": "Транспортный.", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 248)"
    },
    {
        "question": "Пользователю во всплывающем окне приходит сообщение о выигрыше. После запуска исполняемого файла злоумышленник получает доступ к компьютеру. К какому типу относится предпринятая атака?",
        "options": [
            {"text": "Троянский конь", "isCorrect": True},
            {"text": "Компьютерный вирус", "isCorrect": False},
            {"text": "Сетевой червь", "isCorrect": False},
            {"text": "Фишинговая атака", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 292)"
    },
    {
        "question": "При проектировании сети инженер предусматривает решения для назначения приоритетов трафику с учётом его степени важности и технических требований. Обеспечение какой характеристики сети было целью инженера?",
        "options": [
            {"text": "Производительность сети", "isCorrect": True},
            {"text": "Безопасность сети", "isCorrect": False},
            {"text": "Масштабируемость сети", "isCorrect": False},
            {"text": "Отказоустойчивость сети", "isCorrect": False},
        ],
        "source": "eltex-baza.md (вопрос 293)"
    },
]

with open('/home/danila/projects/eltex/questions_draft.json', 'w', encoding='utf-8') as f:
    json.dump(DRAFT, f, ensure_ascii=False, indent=2)

print(f"questions_draft.json записан: {len(DRAFT)} вопросов")
for i, q in enumerate(DRAFT):
    correct = sum(1 for o in q['options'] if o['isCorrect'])
    total = len(q['options'])
    print(f"  [{i:02d}] {correct}/{total} правильных | {q['question'][:60]}")
