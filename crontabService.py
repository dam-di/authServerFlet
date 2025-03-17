from crontab import CronTab
import os

def eliminar_tarer(comentario):
    cron = CronTab(user=True)
    print(comentario)
    for job in cron:
        print(job.comment)
        if job.comment == comentario:

            cron.remove(job)
            cron.write()
            break

def crear_tarea(min, hora, dia, mes, evento):
    # Crear objeto crontab para el usuario actual
    cron = CronTab(user=True)

    script_path = os.path.join(os.getcwd(), "recordatorio.sh")  # Obtiene la ruta absoluta del scrip

    # Crear nueva tarea
    #job = cron.new(command=f'$HOME/pythonFlet/recordatorio.sh {recordatorio}', comment=f'Recordatorio')
    job = cron.new(command=f'{script_path} "{evento}"', comment=f'Recordatorio: {evento}')



    # Configurar para que se ejecute cada minuto
    job.minute.on(min)
    job.hour.on(hora)
    job.day.on(dia)
    job.month.on(mes)


    # Guardar cambios
    cron.write()

    print("Tarea programada con éxito.")
    return True

def retornar_cron():
    cron = CronTab(user=True)
    return cron

#crear_tarea(47,12,17,3,'Dar mucha claseeeee ')
