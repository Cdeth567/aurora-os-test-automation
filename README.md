# Aurora OS Test Automation

Автоматизация тестирования демо-приложения **CallApiDBus** на **Aurora OS** с использованием **Python + pytest + Appium**.

## Что входит в проект

- автотесты на `pytest`
- page object структура
- локаторы, pages, utils
- запуск через Appium
- прогон на эмуляторе Aurora OS
- документация по статусам кейсов и найденным ограничениям

## Структура проекта

```text
aurora-os-test-automation/
├─ locators/
├─ pages/
├─ tests/
├─ utils/
├─ docs/
├─ pytest.ini
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## Требования

Перед запуском должны быть доступны:

- Windows
- Python 3.11+
- Docker Desktop
- Aurora OS SDK / Qt Creator
- эмулятор Aurora OS
- контейнер с Appium Aurora
- приложение `CallApiDBus`, установленное в эмулятор

## Подготовка окружения

### 1. Создать и активировать виртуальное окружение

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Установить зависимости

```powershell
pip install -r requirements.txt
```

### 3. Запустить Docker Desktop

Проверка:

```powershell
docker ps
```

### 4. Запустить эмулятор Aurora OS

Эмулятор можно запустить из Qt Creator.

### 5. Запустить Appium-контейнер

Если контейнер уже создан:

```powershell
docker start -ai appium-aurora
```

Если контейнера ещё нет:

```powershell
docker run -it --name appium-aurora -p 4723:4723 hub.omp.ru/public/appium-aurora:3.0.1
```

### 6. Проверить, что Appium слушает порт

В отдельном окне PowerShell:

```powershell
Test-NetConnection localhost -Port 4723
```

Ожидаемо:

```text
TcpTestSucceeded : True
```

## Запуск тестов

### Обычный запуск

```powershell
pytest
```

### Запуск с сохранением лога

```powershell
pytest 2>&1 | Tee-Object -FilePath pytest_log.txt
```

## Что покрыто

Автотестами покрыты воспроизводимые сценарии, которые стабильно работают в текущем окружении:

- открытие приложения
- проверка элементов главного экрана
- воспроизводимая часть сценария входящего вызова
- переключатель **Удержание**
- переключатель **DTMF**

## Известное ограничение

Сценарий **исходящего вызова** не проходит в эмуляторе: после нажатия на кнопку **"Исходящий вызов"** ожидаемый экран звонка не открывается.  
Этот дефект фиксируется автотестом `test_50556_outgoing_call_creation`, а также сохраняются debug-артефакты:

- `outgoing_call_not_opened.xml`
- `outgoing_call_not_opened.png`

## Полезные файлы

- `docs/TEST_RUN_REPORT.md`
- `docs/TEST_CASE_STATUS.md`
- `docs/KNOWN_ISSUES.md`

