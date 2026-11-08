# Flask App: Dockerized & CI/CD Automated

## 📌 О проекте
Этот репозиторий представляет собой демонстрацию **DevOps-практик** на примере простого веб-приложения на Python (Flask). 

Проект демонстрирует полный жизненный цикл приложения (SDLC): от написания кода до автоматической сборки артефакта (Docker-образа) с помощью пайплайна непрерывной интеграции (CI).

## 🛠️ Стек технологий и инструменты
*   **Приложение:** Python 3.12, Flask 3.0.0
*   **Контейнеризация:** Docker (multi-stage / layer caching optimization)
*   **CI/CD:** GitHub Actions (Automated Build Pipeline)
*   **VCS:** Git, GitHub
*   **Инфраструктура (локально):** Docker Engine

## 📂 Архитектура репозитория
```text
.
├── .github/workflows/
│   └── docker-build.yml   # CI-пайплайн: автосборка образа при push в main
├── .gitignore             # Изоляция артефактов (venv, __pycache__)
├── Dockerfile             # Декларативное описание сборки образа
├── app.py                 # Исходный код приложения
├── requirements.txt       # Пиннинг зависимостей (фиксация версий)
└── README.md              # Документация
