import limjob
import nis
import time

def run(imgs: tuple[limjob.Image], Job: limjob.JobParam, macro: limjob.MacroParam, ctx: limjob.RunContext):
    port_id = 10
    mapa_mocy = {1: 10, 2: 40, 3: 70, 4: 100}
    
    # Bezpieczne pobranie parametru
    wybrany = macro.IntParam[0] if len(macro.IntParam) > 0 else 1
    procent = mapa_mocy.get(wybrany, 10)

    try:
        # 1. Próba otwarcia
        nis.mac.OpenPort(port_id, 9600, 8, "N", 1)
        time.sleep(0.05)  # KRUCIALNE: Krótka pauza na stabilizację portu
        
        # 2. Zmieniamy ostatni parametr na 0 (nie czekaj na odpowiedź), 
        # jeśli nie potrzebujemy potwierdzenia od Arduino. 
        # To zapobiega "wiszeniu" NISa, gdy Arduino milczy.
        nis.mac.WritePort(port_id, f"SET:{procent}\r", 1, 0)
        
        print(f"Wysłano: SET:{procent}%")
        time.sleep(0.05) # Pauza przed zamknięciem
        
    except Exception as e:
        print(f"Błąd komunikacji: {e}")
    finally:
        # Zawsze zamykamy, ale dodajemy mały margines bezpieczeństwa
        try:
            nis.mac.ClosePort(port_id)
        except:
            pass