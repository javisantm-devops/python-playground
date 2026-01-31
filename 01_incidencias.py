nombre = input("Tu nombre")
incidencia = input("Pasame una incidencia")
prioridad = input("Dame la prioridad baja|media|alta")

nombre = input("Tu nombre: ")
incidencia = input("Pásame una incidencia: ")
prioridad = input("Dame la prioridad (baja | media | alta): ")

if prioridad == "alta" or prioridad == "media" or prioridad == "baja":

    if prioridad == "alta":
        print("Es urgente")
    elif prioridad == "media":
        print("Es importante")
    else:
        print("No es urgente")

    ticket = open("ticket.txt", "a")
    ticket.write(nombre + " | ")
    ticket.write(prioridad + " | ")
    ticket.write(incidencia + "\n")
    ticket.close()

    print("Ticket bien creado")

else:
    print("Prioridad no válida")