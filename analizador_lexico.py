# Importamos herramientas principales de ANTLR
from antlr4 import InputStream, CommonTokenStream, Token

# Importamos ErrorListener para capturar errores lexicos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el lexer generado por ANTLR
from ExprLexer import ExprLexer

# Importando el parser generado por ANTLR
from ExprParser import ExprParser


# Clase para guardar errores lexicos y sintacticos
class ErroresLexicos(ErrorListener):

    def __init__(self):
        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


class AnalizadorLexico:

    def __init__(self):
        self.lexer = None
        self.tokens = None
        self.errores = ErroresLexicos()
        self.errores_sintacticos = ErroresLexicos()  # nuevo
        self.parser = None  # nuevo
        self.tree = None    # nuevo

    def analizar(self, codigo):
        entrada = InputStream(codigo)

        self.lexer = ExprLexer(entrada)
        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.errores)

        self.tokens = CommonTokenStream(self.lexer)

        self.parser = ExprParser(self.tokens)

        # nuevo: capturamos errores sintacticos del parser
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.errores_sintacticos)

        self.tree = self.parser.file_()
        self.arbol = self.tree.toStringTree(recog=self.parser)

        self.tokens.fill()

    def obtener_tokens(self):
        resultado = []

        for token in self.tokens.tokens:
            if token.type == Token.EOF:
                continue

            nombre_token = self.lexer.symbolicNames[token.type]

            resultado.append({
                "lexema": token.text,
                "token": nombre_token,
                "tipo": token.type,
                "linea": token.line,
                "columna": token.column
            })

        return resultado

    def obtener_errores(self):
        return self.errores.lista

    def obtener_errores_sintacticos(self):  # nuevo
        return self.errores_sintacticos.lista

    def obtener_arbol(self):
        return self.arbol

    def obtener_tree(self):  # nuevo
        return self.tree

    def obtener_parser(self):  # nuevo
        return self.parser