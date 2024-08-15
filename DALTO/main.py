
result = 0
def operar_aritmetico(op, num_1, num_2):
    if op == "suma":
        return num_1 + num_2
    elif op == "resta":
        return num_1 - num_2
    elif op == "mult":
        return num_1 * num_2
    elif op == "div":
        return num_1 / num_2
    else:
        print("No se pudo operar")

