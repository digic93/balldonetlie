# Balldonetlie

Consulta del api [balldonetlie](https://www.balldontlie.io/).

## Installación

Cree un entorno y active un virtual de Python:
```bash
$ python3 -m venv .env 
```

Activando el entorno virtual .env:


```bash
source .env/bin/activate
```

Instalando las dependencias:

```bash
$ pip install -e .
```

## Ejecutar la aplicación

Para For Linux and Mac:
```bash
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```

En Windows cmd, use set en lugar de exportar

```bash
> set FLASK_APP=app
> set FLASK_ENV=development
> flask run
```

Usted vera also similar a lo siguiente:
```bash
* Serving Flask app "app"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```

Visite [localhost:5000](http://127.0.0.1:5000/) en un navegador y debería ver el la lista de jugadores 
