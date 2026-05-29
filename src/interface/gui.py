import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from src.algorithms.fuerza_bruta import roFB
from src.algorithms.voraz import roV
from src.algorithms.programacion_dinamica import roPD

from src.utils.parser import leer_finca
from src.utils.formatter import guardar_resultado


def iniciar_gui():

    # ==========================================
    # VENTANA PRINCIPAL
    # ==========================================

    ventana = tk.Tk()

    ventana.title("Proyecto Riego Óptimo")

    ventana.geometry("450x500")

    ventana.resizable(False, False)

    # ==========================================
    # VARIABLES
    # ==========================================

    algoritmo_var = tk.StringVar(value="fb")

    # ==========================================
    # TÍTULO
    # ==========================================

    titulo = tk.Label(
        ventana,
        text="Selecciona un algoritmo",
        font=("Arial", 14, "bold")
    )

    titulo.pack(pady=15)

    # ==========================================
    # RADIO BUTTONS
    # ==========================================

    radio_fb = tk.Radiobutton(
        ventana,
        text="Fuerza Bruta",
        variable=algoritmo_var,
        value="fb",
        font=("Arial", 11)
    )

    radio_fb.pack(anchor="w", padx=20)

    radio_voraz = tk.Radiobutton(
        ventana,
        text="Voraz",
        variable=algoritmo_var,
        value="voraz",
        font=("Arial", 11)
    )

    radio_voraz.pack(anchor="w", padx=20)

    radio_pd = tk.Radiobutton(
        ventana,
        text="Programación Dinámica",
        variable=algoritmo_var,
        value="pd",
        font=("Arial", 11)
    )

    radio_pd.pack(anchor="w", padx=20)

    # ==========================================
    # SECCIÓN ARCHIVOS
    # ==========================================

    subtitulo = tk.Label(
        ventana,
        text="Selecciona un archivo",
        font=("Arial", 13)
    )

    subtitulo.pack(pady=20)

    # ==========================================
    # LISTA DE ARCHIVOS
    # ==========================================

    lista_archivos = tk.Listbox(
        ventana,
        width=30,
        height=10,
        font=("Arial", 10)
    )

    lista_archivos.pack()

    # ==========================================
    # CARGAR ARCHIVOS DESDE test/
    # ==========================================

    carpeta_test = Path("test")

    archivos = []

    if carpeta_test.exists():

        archivos = sorted(
            carpeta_test.glob("*_in.txt")
        )

        for archivo in archivos:

            lista_archivos.insert(
                tk.END,
                archivo.name
            )

    # ==========================================
    # FUNCIÓN EJECUTAR
    # ==========================================

    def ejecutar():

        seleccion = lista_archivos.curselection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Seleccione un archivo"
            )

            return

        nombre_archivo = lista_archivos.get(
            seleccion[0]
        )

        ruta_archivo = carpeta_test / nombre_archivo

        try:

            # ==============================
            # LEER FINCA
            # ==============================

            finca = leer_finca(
                str(ruta_archivo)
            )

            algoritmo = algoritmo_var.get()

            # ==============================
            # EJECUTAR ALGORITMO
            # ==============================

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

            # ==============================
            # CREAR NOMBRE SALIDA
            # ==============================

            nombre_salida = (
                ruta_archivo.stem.replace(
                    "_in",
                    ""
                )
                + "_out.txt"
            )

            output_path = (
                Path("output")
                / nombre_salida
            )

            # ==============================
            # GUARDAR RESULTADO
            # ==============================

            guardar_resultado(
                resultado,
                str(output_path)
            )

            # ==============================
            # MOSTRAR RESULTADO
            # ==============================

            texto_resultado = (
                f"Costo total: "
                f"{resultado.costo}\n\n"
                f"Orden:\n"
                f"{resultado.orden}\n\n"
                f"Guardado en:\n"
                f"{output_path}"
            )

            messagebox.showinfo(
                "Resultado",
                texto_resultado
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # BOTÓN INICIAR
    # ==========================================

    boton = tk.Button(
        ventana,
        text="Iniciar",
        font=("Arial", 11),
        command=ejecutar,
        width=10,
        height=1
    )

    boton.pack(pady=25)

    # ==========================================
    # INICIAR GUI
    # ==========================================

    ventana.mainloop()