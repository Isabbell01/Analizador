# ANALIZADOR (LÉXICO, SINTÁCTICO ) PARA PYTHON 

## DESCRIPCIÓN
Proyecto final en el cual se implementa un analizador para el lenguaje de Python utilizando ANTLR4 y StREAMLIT.

- **Análisis léxico**: Reconocimiento de tokens (palabras reservadas, operadores, identificadores, literales, etc.).
- **Análisis sintáctico**: Verificación de la estructura del código según la gramática oficial de Python (basada en la documentación de Python 3.14).
- **Análisis semántico**: Detección de variables no definidas, funciones y clases, utilizando un **Listener** de ANTLR.

La interfaz está desarrollada con **Streamlit**, lo cual permite una experiencia interactiva y visual: el usuario sube un archivo `.py` y como resultado de ello, obtiene un análisis detallado en tiempo real.


## ¿Cómo usar lo archivos del ejercico?
### PASO 1-
CLONAR EL REPOSITORIO EJECUTANDO LOS SIGUIENTES COMANDOS

```powershell
git clone https://github.com/Isabbell01/Analizador.git
```
### PASO 2-
ENTRAR A LA CARPETA 

```powershell
cd Analizador
```

### PASO 3-
CREAR Y ACTIVAR EL ENTORNO VIRTUAL EJECUTANDO LOS SIGUIENTES COMANDOS

```powershell
py -m venv .venv
```
```powershell
.\venv\Scripts\Activate.ps1
```

### PASO 4-
INSTALAR EL RUNTIME DE ANTLR PARA PHYTON EJECUTANDO EL SIGUIENTE COMANDO

```powershell
pip install -r requirements.txt
```

### PASO 5-
GENERAR EL PARSER Y EL LEXER EJECUTANDO EL SIGUENTE COMANDO 

```powershell
java -jar $env:CLASSPATH -Dlanguage=Python3 -no-listener.\Expr.g4
```
NOTA: Es importantes agregar al PATH el archivo:  **antlr-4.13.2-complete.jar** este archivo en el codigo se manda llamar por la variable de entorno CLASSPATH


### PASO 6- EJECUTAR EL SCRIPT
Opción 1 (ARCHIVO) 
```powershell
py Text.py 
```
