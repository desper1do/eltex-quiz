# Тренажёр Элтекс

223 вопроса по курсу «Основы сетевых технологий. Часть 1».

## Открыть тест

Клонируй репо и открой `quiz.html` в браузере — интернет не нужен.

```bash
git clone https://github.com/USERNAME/eltex-quiz.git
cd eltex-quiz
```

Затем в терминале WSL:
```bash
explorer.exe quiz.html
```

Или просто дважды кликни на `quiz.html` в проводнике Windows.

## Добавить вопросы из скриншотов

Нужен [Gemini API key](https://aistudio.google.com/app/apikey):

```bash
pip install google-genai
export GEMINI_API_KEY=ваш_ключ
python main.py папка_со_скриншотами
```

Скрипт обработает фото и пересоберёт `quiz.html`.
