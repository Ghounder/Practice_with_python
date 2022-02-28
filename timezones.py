from datetime import datetime
import pytz as tz

def run():
    bogota = tz.timezone("America/Bogota")
    bogota_date = datetime.now(bogota)
    print("bogota: ", bogota_date.strftime("%d/%m/%Y , %H:%M:%S"))
    mexico = tz.timezone("America/Mexico_city")
    mexico_date = datetime.now(mexico)
    print("Cdmx: ", mexico_date.strftime("%d/%m/%Y , %H:%M:%S"))
    peru = tz.timezone("America/Lima")
    peru_date = datetime.now(peru)
    print("peru: ", peru_date.strftime("%d/%m/%Y , %H:%M:%S"))

if __name__ == "__main__":
    run()