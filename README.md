### Ativar o ambiente virtual
```python
python -m venv .venv
```

```bash
.venv\Scripts\Activate
```
### Instalar os requirements
```python
pip install -r requirements.txt
```


### Para rodas as migrações
```python
python manage.py makemigrations
python manage.py migrate
```

### Para rodar os testes

```python
python manage.py test
```

### Para rodar o servidor
```python
python manage.py runserver
```