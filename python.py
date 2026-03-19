import limjob
import nis
import time

def run(imgs: tuple[limjob.Image], Job: limjob.JobParam, macro: limjob.MacroParam, ctx: limjob.RunContext):
    port_id = 10
    
    # Przykładowa jasność, którą chcesz ustawić (0 do 100)
    jasnosc = 20  

    try:
        nis.mac.OpenPort(port_id, 9600, 8, "N", 1)
        
        # Wysyłamy nową komendę SET:wartość
        # Formatowanie f-string w Pythonie wstawi liczbę do tekstu
        command = f"SET:{jasnosc}"
        
        print(f"Ustawiam jasność na: {jasnosc}%")
        nis.mac.WritePort(port_id, command, 1, 1)
        
        # Czekamy np. 2 sekundy, żeby zobaczyć efekt
        time.sleep(2.0)
        
    except Exception as e:
        print(f"Python Error: {e}")
        
    finally:
        # Możesz zgasić diodę na koniec lub zostawić zapaloną
        # nis.mac.WritePort(port_id, "STOP", 1, 1)
        nis.mac.ClosePort(port_id)