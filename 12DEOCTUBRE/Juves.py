class FiestaDisfraces:
    def __init__(self):
        self.asistentes_admitidos = []
        self.asistentes_rechazados = []
        self.temas_disfraz_permitidos = ["la muelona","muelona", "el hombre caiman","caiman", "la patasola","patasola", "la llorona","llorona", "el sombreron","sombreron", "la madremonte","madremonte", "el silbon","silbon", "juan machete","machete", "el mohan","mohan"]
        self.contador_admitidos = 0
        self.contador_rechazados = 0

    def ingresar_fiesta(self):
        continuar_ingreso = True

        while continuar_ingreso:
            edad = int(input("Ingresa la edad: "))
            estatura = int(input("Ingresa la estatura en cm: "))
            tema_disfraz = input("Ingresa nombre de su disfraz: ").lower()

            
            if edad >= 18 and estatura >= 160 and tema_disfraz in self.temas_disfraz_permitidos:
                print("¡Bienvenido a la fiesta , eres todo un colombiano!")
                self.asistentes_admitidos.append(f"Edad: {edad}, Estatura: {estatura}, Tema Disfraz: {tema_disfraz}")
                self.contador_admitidos += 1
            else:
                print("Lo siento, no cumples con los requisitos de ingreso , asi que vallase a la casa a reflexionar sobre su vida.")
                motivo_rechazo = "No cumple con los requisitos de edad, estatura o temática del disfraz, asi que mejor suerte la proxima."
                self.asistentes_rechazados.append(f"Edad: {edad}, Estatura: {estatura}, Tema Disfraz: {tema_disfraz}, Motivo Rechazo: {motivo_rechazo}")
                self.contador_rechazados += 1

            respuesta = input("¿Deseas ingresar a otro participante? (si/no): ")
            continuar_ingreso = respuesta.lower() == 'si'

    def generar_reporte(self):
        print("\nReporte de Asistentes Admitidos:")
        for asistente in self.asistentes_admitidos:
            print(asistente)

        print("\nReporte de Asistentes Rechazados:")
        for asistente in self.asistentes_rechazados:
            print(asistente)

        print(f"\nTotal de Asistentes Admitidos: {self.contador_admitidos}")
        print(f"Total de Asistentes Rechazados: {self.contador_rechazados}")


fiesta = FiestaDisfraces()
fiesta.ingresar_fiesta()
fiesta.generar_reporte()