from ExprVisitor import ExprVisitor

# Nombres que Python ya trae incorporados, para no marcarlos como error
BUILTINS = {
    "print", "len", "range", "str", "int", "float", "input",
    "list", "dict", "set", "tuple", "bool", "type", "sum",
    "min", "max", "abs", "sorted", "enumerate", "zip", "open"
}


class AnalizadorSemantico(ExprVisitor):

    def __init__(self):
        self.declaradas = set(BUILTINS)
        self.errores = []

    def analizar(self, tree):
        self.declaradas = set(BUILTINS)
        self.errores = []
        self.visit(tree)

    def obtener_errores(self):
        return self.errores

    # Extrae todos los NAME (nombres de variable) dentro de un nodo objetivo
    def _extraer_nombres(self, ctx):
        nombres = []

        if ctx is None:
            return nombres

        # Si el propio nodo es un token NAME
        texto = ctx.getText() if hasattr(ctx, "getText") else None

        for i in range(ctx.getChildCount()):
            hijo = ctx.getChild(i)

            if hasattr(hijo, "symbol") and hijo.symbol.type == hijo.symbol.type:
                pass

            if hijo.getChildCount() == 0:
                # Es una hoja (terminal). Revisamos si es un NAME
                if hasattr(hijo, "getSymbol"):
                    simbolo = hijo.getSymbol()
                    if simbolo.text.isidentifier() and simbolo.text not in (
                        "=", ":", ",", "(", ")", "[", "]"
                    ):
                        nombres.append(simbolo.text)
            else:
                nombres.extend(self._extraer_nombres(hijo))

        return nombres

    # Se dispara en cada asignacion: x = 5, x: int = 5, x += 1, etc.
    def visitAssignment(self, ctx):
        # Primero revisamos la parte derecha (lo que se usa/lee)
        rhs = None
        if ctx.annotated_rhs():
            rhs = ctx.annotated_rhs()
        elif ctx.expression():
            rhs = ctx.expression()

        if rhs is not None:
            self.visit(rhs)

        # Ahora registramos lo que se declara (la parte izquierda)
        if ctx.NAME():
            self.declaradas.add(ctx.NAME().getText())

        for star_targets in ctx.star_targets():
            for nombre in self._extraer_nombres(star_targets):
                self.declaradas.add(nombre)

        if ctx.single_target():
            for nombre in self._extraer_nombres(ctx.single_target()):
                self.declaradas.add(nombre)

        return None

    # Se dispara cuando se usa un nombre (variable, funcion, etc.)
    def visitAtom(self, ctx):
        if ctx.NAME():
            nombre = ctx.NAME().getText()
            if nombre not in self.declaradas:
                self.errores.append(
                    f"Linea {ctx.start.line}: la variable '{nombre}' no ha sido declarada"
                )
                # la agregamos para no repetir el mismo error varias veces
                self.declaradas.add(nombre)

        return self.visitChildren(ctx)