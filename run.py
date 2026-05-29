import sys
from pathlib import Path



from src.algorithms.fuerza_bruta import roFB
from src.algorithms.voraz import roV
from src.algorithms.programacion_dinamica import roPD

from src.utils.parser import leer_finca
from src.utils.formatter import guardar_resultado

def main():

    algoritmo = sys.argv[1]
    archivo = sys.argv[2]

    finca = leer_finca(archivo)

    if algoritmo == "fb":
        resultado = roFB(finca)

    elif algoritmo == "voraz":
        resultado = roV(finca)

    elif algoritmo == "pd":
        resultado = roPD(finca)

    else:
        raise ValueError(
            "Algoritmo inválido"
        )

    print(resultado)

    # ==========================================
    # GENERAR NOMBRE DEL ARCHIVO DE SALIDA
    # ==========================================

    input_path = Path(archivo)

    nombre_salida = (
        input_path.stem.replace("_in", "")
        + "_out.txt"
    )

    output_path = Path("output") / nombre_salida

    # ==========================================
    # GUARDAR RESULTADO
    # ==========================================

    guardar_resultado(
        resultado,
        str(output_path)
    )

    print(f"\nResultado guardado en: {output_path}")


if __name__ == "__main__":
    main()