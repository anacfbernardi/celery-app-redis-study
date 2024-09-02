# LEARNING CELERY WITH REDIS

### How to run
- Install python
- Create .venv:
```bash
python -m venv .venv
```
- Activate venv:
```bash
. .venv/Scripts/activate
```
- Install requirements:
```bash
pip install -r requirements.txt
```
- Start Redis container:
```bash
docker compose pull
docker compose up --build
```
- Initialize celery worker:
```bash
celery -A main worker -l INFO -P threads
```
>  for some reason, the option `-P threads` is necessary on Windows environments
- Run the code:
```bash
python main.py
```