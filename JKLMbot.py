import time
import random
import pyautogui
import unicodedata
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

def sans_accents(texte):
    return ''.join(c for c in unicodedata.normalize('NFD', texte)
                   if unicodedata.category(c) != 'Mn').lower()

MON_PSEUDO = "thib"
FICHIER_DICTO = "mots.txt"
EN_PAUSE = False

url_partie = input("Lien de la partie : ")

print("Chargement du dictionnaire...")
with open(FICHIER_DICTO, "r", encoding="utf-8", errors="ignore") as f:
    mots_bruts = {sans_accents(ligne.strip()) for ligne in f if len(ligne.strip()) > 2}
    dictionnaire = sorted(list(mots_bruts), key=len)

driver = webdriver.Edge()
driver.get(url_partie)

mots_utilises = set()

def toggle_pause():
    global EN_PAUSE
    EN_PAUSE = not EN_PAUSE
    print(f"--- BOT EN {'PAUSE' if EN_PAUSE else 'REPRISE'} ---")

keyboard.add_hotkey('9', toggle_pause)

print("\n--- BOT LANCÉ ---")
print("Touche [9] pour Pause | Touche [0] pour Quitter")

try:
    while True:
        if keyboard.is_pressed('0'): break
        if EN_PAUSE:
            time.sleep(0.5)
            continue

        driver.switch_to.default_content()
        # Recherche de l'iframe de BombParty
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        found = False
        for ifr in iframes:
            try:
                src = ifr.get_attribute("src")
                if src and "bombparty" in src:
                    driver.switch_to.frame(ifr)
                    found = True
                    break
            except: continue
        
        if not found:
            time.sleep(1)
            continue

        try:
            # --- DÉTECTION PAR LA VISIBILITÉ DE L'INPUT ---
            # Sur JKLM, quand c'est ton tour, la div .selfTurn devient visible
            # ou l'input de texte est affiché.
            input_field = driver.find_elements(By.CSS_SELECTOR, "form input")
            
            # On vérifie si l'input existe et s'il est affiché à l'écran
            if len(input_field) > 0 and input_field[0].is_displayed():
                
                syllabe_el = driver.find_element(By.CLASS_NAME, "syllable")
                syllabe = sans_accents(syllabe_el.text).strip()
                
                if syllabe:
                    # On cherche un mot
                    mot_a_taper = next((m for m in dictionnaire if syllabe in m and m not in mots_utilises), None)
                    
                    if mot_a_taper:
                        print(f"Tour détecté ! Syllabe: {syllabe} | Envoi: {mot_a_taper}")
                         # Clique au milieu pour le focus
                        pyautogui.click(x=pyautogui.size().width//2, y=pyautogui.size().height//2)
                        # Petite attente "humaine"
                        time.sleep(random.uniform(0.4, 0.9))

                        # Simulation de l'erreur
                        faire_erreur = random.random() < 0.15
                        idx_err = random.randint(1, len(mot_a_taper)-1) if faire_erreur else -1

                        for i, lettre in enumerate(mot_a_taper):
                            if i == idx_err:
                                pyautogui.write(random.choice("azerty"))
                                time.sleep(random.uniform(0.2, 0.4))
                                pyautogui.press('backspace')
                            
                            pyautogui.write(lettre)
                            time.sleep(random.uniform(0.05, 0.12))
                        
                        # Validation
                        time.sleep(random.uniform(0.1, 0.3))
                        pyautogui.press('enter')
                        
                        mots_utilises.add(mot_a_taper)
                        # On attend que le champ disparaisse (fin du tour)
                        time.sleep(2) 
            
        except Exception as e:
            pass

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

driver.quit()