from flask import Flask, render_template, request
import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# ========================================
# MRU
# ========================================

@app.route("/mru")
def mru():
    return render_template("mru.html")


@app.route("/calcular_mru", methods=["POST"])
def calcular_mru():

    try:

        x0 = float(request.form["x0"])
        v = float(request.form["v"])
        t_max = float(request.form["t"])

        if t_max < 0:
            raise ValueError

    except ValueError:

        return render_template(
            "mru.html",
            error="Ingrese valores numéricos válidos."
        )

    # --------------------------------
    # CREAR LOS VALORES DE TIEMPO
    # --------------------------------

    t = np.linspace(0, t_max, 100)

    # --------------------------------
    # ECUACIÓN DEL MRU
    # --------------------------------

    x = x0 + v * t

    # --------------------------------
    # RESULTADOS
    # --------------------------------

    resultados = []

    for i in range(10):

        resultados.append({
            "tiempo": round(t[i], 2),
            "posicion": round(x[i], 2)
        })

    # --------------------------------
    # CREAR GRÁFICA
    # --------------------------------

    plt.figure(figsize=(8, 5))

    plt.plot(
        t,
        x,
        linewidth=2
    )

    plt.title("Movimiento Rectilíneo Uniforme")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")

    plt.grid(True)

    # --------------------------------
    # GUARDAR GRÁFICA
    # --------------------------------

    graph_path = os.path.join(
        app.root_path,
        "static",
        "mru_graph.png"
    )

    plt.savefig(
        graph_path,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------
    # DEVOLVER RESULTADOS
    # --------------------------------

    return render_template(
        "mru.html",
        resultados=resultados,
        graph=True
    )


# ========================================
# MRUA
# ========================================

@app.route("/mrua")
def mrua():
    return render_template("mrua.html")


@app.route("/calcular_mrua", methods=["POST"])
def calcular_mrua():

    try:

        x0 = float(request.form["x0"])
        v0 = float(request.form["v0"])
        a = float(request.form["a"])
        tf = float(request.form["tf"])

        if tf < 0:
            raise ValueError

    except ValueError:

        return render_template(
            "mrua.html",
            error="Ingrese valores numéricos válidos."
        )

    # --------------------------------
    # ECUACIÓN MRUA
    # --------------------------------

    t = np.linspace(0, tf, 100)

    x = x0 + v0 * t + 0.5 * a * t**2

    # --------------------------------
    # CREAR GRÁFICA
    # --------------------------------

    plt.figure(figsize=(8, 5))

    plt.plot(
        t,
        x,
        linewidth=2
    )

    plt.title(
        "Movimiento Rectilíneo Uniformemente Acelerado"
    )

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")

    plt.grid(True)

    # --------------------------------
    # GUARDAR GRÁFICA
    # --------------------------------

    graph_path = os.path.join(
        app.root_path,
        "static",
        "mrua_graph.png"
    )

    plt.savefig(
        graph_path,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------
    # RESULTADOS
    # --------------------------------

    resultados = []

    for i in range(10):

        resultados.append({
            "tiempo": round(t[i], 2),
            "posicion": round(x[i], 2)
        })

    # --------------------------------
    # DEVOLVER RESULTADOS
    # --------------------------------

    return render_template(
        "mrua.html",
        resultados=resultados,
        graph=True
    )
# ========================================
# CAÍDA LIBRE
# ========================================

@app.route("/caida_libre")
def caida_libre():
    return render_template("caida_libre.html")


@app.route("/calcular_caida_libre", methods=["POST"])
def calcular_caida_libre():

    try:

        h0 = float(request.form["h0"])
        v0 = float(request.form["v0"])
        g = float(request.form["g"])
        t_max = float(request.form["t_max"])

        if h0 <= 0 or g <= 0 or t_max <= 0:
            raise ValueError

    except ValueError:

        return render_template(
            "caida_libre.html",
            error="Ingrese valores numéricos válidos."
        )


    # --------------------------------
    # TIEMPO
    # --------------------------------

    t = np.linspace(0, t_max, 100)


    # --------------------------------
    # ECUACIONES DE CAÍDA LIBRE
    # --------------------------------

    y = h0 + v0 * t - 0.5 * g * t**2

    v = v0 - g * t


    # --------------------------------
    # EVITAR ALTURAS NEGATIVAS
    # --------------------------------

    y = np.maximum(y, 0)


    # --------------------------------
    # RESULTADOS
    # --------------------------------

    resultados = []

    for i in range(10):

        resultados.append({
            "tiempo": round(t[i], 2),
            "altura": round(y[i], 2),
            "velocidad": round(v[i], 2)
        })


    # --------------------------------
    # DEVOLVER RESULTADOS
    # --------------------------------

    return render_template(
        "caida_libre.html",
        resultados=resultados,
        h0=h0,
        v0=v0,
        g=g,
        t_max=t_max
    )
# ========================================
# QUÍMICA
# ========================================

elementos = {
    1: ("Hidrógeno", "H"),
    2: ("Helio", "He"),
    3: ("Litio", "Li"),
    4: ("Berilio", "Be"),
    5: ("Boro", "B"),
    6: ("Carbono", "C"),
    7: ("Nitrógeno", "N"),
    8: ("Oxígeno", "O"),
    9: ("Flúor", "F"),
    10: ("Neón", "Ne"),
    11: ("Sodio", "Na"),
    12: ("Magnesio", "Mg"),
    13: ("Aluminio", "Al"),
    14: ("Silicio", "Si"),
    15: ("Fósforo", "P"),
    16: ("Azufre", "S"),
    17: ("Cloro", "Cl"),
    18: ("Argón", "Ar"),
    19: ("Potasio", "K"),
    20: ("Calcio", "Ca")
}


def distribucion_bohr(electrones):

    niveles = [2, 8, 18, 32]

    resultado = []

    for nivel in niveles:

        if electrones > 0:

            cantidad = min(electrones, nivel)

            resultado.append(cantidad)

            electrones -= cantidad

        else:

            resultado.append(0)

    return resultado


@app.route("/quimica")
def quimica():

    return render_template("quimica.html")


@app.route("/calcular_quimica", methods=["POST"])
def calcular_quimica():

    try:

        protones = int(request.form["protones"])

        neutrones = int(request.form["neutrones"])

        if protones < 1 or neutrones < 0:
            raise ValueError

    except ValueError:

        return render_template(
            "quimica.html",
            error="Ingrese valores numéricos válidos."
        )


    # En un átomo neutro:
    electrones = protones

    # Número atómico
    numero_atomico = protones

    # Número de masa
    numero_masa = protones + neutrones


    # Buscar elemento
    elemento = elementos.get(
        numero_atomico,
        ("Desconocido", "")
    )


    # Distribución de electrones según Bohr
    bohr = distribucion_bohr(electrones)


    resultado = {

        "protones": protones,

        "neutrones": neutrones,

        "electrones": electrones,

        "z": numero_atomico,

        "a": numero_masa,

        "nombre": elemento[0],

        "simbolo": elemento[1],

        "bohr": bohr

    }


    return render_template(
        "quimica.html",
        resultado=resultado
    )

# ========================================
# INICIAR SERVIDOR
# ========================================

if __name__ == "__main__":
    app.run(debug=True)