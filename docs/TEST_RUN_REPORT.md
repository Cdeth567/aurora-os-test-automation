# Отчёт о прогоне тестов

## Окружение

- ОС: Windows
- Python: 3.11.9
- Test runner: pytest 9.0.3
- Целевое окружение: эмулятор Aurora OS
- Стек автоматизации: Appium + Python + pytest

## Результат прогона

- Всего тестов: 6
- Успешно: 5
- Неуспешно: 1

## Успешные тесты

- `test_50556_open_app`
- `test_50557_incoming_call_creation`
- `test_50557_main_screen_elements_visible`
- `test_53609_holding_switch_can_be_enabled`
- `test_53610_dtmf_switch_can_be_enabled`

## Неуспешные тесты

- `test_50556_outgoing_call_creation`

## Детали падения

### 50556 - создание исходящего вызова

После нажатия на кнопку **"Исходящий вызов"** ожидаемый экран звонка не появился в эмуляторе в течение заданного таймаута.

Сохранённые debug-артефакты:

- `outgoing_call_not_opened.xml`
- `outgoing_call_not_opened.png`
