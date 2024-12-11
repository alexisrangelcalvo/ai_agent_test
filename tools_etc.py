

def calculator_tool(expression: str) -> str:
    """
    Una herramienta de cálculo simple que puede interpretar algunos patrones en texto.
    Por ejemplo, "average of 100 and 200" -> "150"
    """
    import re
    
    # Ejemplo: promedio de dos números
    match = re.match(r"average of (\d+(?:\.\d+)?) and (\d+(?:\.\d+)?)", expression)
    if match:
        x = float(match.group(1))
        y = float(match.group(2))
        return str((x + y) / 2)
    
    # Como fallback, intentamos un eval sencillo (ten en cuenta la seguridad si lo usas en producción)
    try:
        result = eval(expression)
        return str(result)
    except:
        return "No pude calcular la expresión."