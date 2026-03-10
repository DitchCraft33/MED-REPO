import os, sys, time, json, random

def load_data():
    try:
        with open('medic_data.json', 'r') as f:
            return json.load(f)
    except:
        print("\n  !! ERROR : medic_data.json not found !!")
        sys.exit()

DATA = load_data()

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_hud(sitrep_text, header_text="MEDIC PROCEDURES"):
    clear()
    print(f"\n  [ {header_text} ]")
    print(f"\n  > SITREP ...")
    print(f"\n  {sitrep_text}\n")

def run_drill(stress=False):
    scenario = random.choice(DATA["SCENARIOS"])
    limit = 8.0 
    
    for key, val in DATA["MARCH_PAWS"].items():
        display_hud(scenario['sitrep'])
        display_key = key.replace("_", "")
        
        print(f"  > STEP : ({display_key}) {val['desc']}")
        print(f"\n  > TASK : {val['options']}")
        
        start_t = time.time()
        ans = input("\n  > ").lower().strip()
        elapsed = time.time() - start_t
        
        if stress and elapsed > limit:
            print(f"\n\n  !! TIMEOUT !! Casualty status degraded. ({elapsed:.1f}s)")
            print(f"\n  > HINT : {scenario['hint']}")
            input("\n  > ENTER TO RESET ..."); return

        correct_ans = scenario['solution'].get(key, "") 
        
        if ans == correct_ans:
            print(f"\n  [ OK ] ({elapsed:.1f}s)")
            time.sleep(3) # 3-second dwell for performance feedback
        else:
            expected = "N/A (Enter)" if correct_ans == "" else f"({correct_ans.upper()})"
            print(f"\n\n  !! INCORRECT !!")
            print(f"  ACTION REQUIRED : {expected}")
            print(f"\n  > HINT : {scenario['hint']}")
            input("\n  > ENTER TO RESET ..."); return

    print("\n\n  > PROTOCOL COMPLETE ... CASUALTY STABILIZED")
    input("\n  > ENTER FOR COMMS PHASE ...")
    run_comms()

def run_comms():
    clear()
    print("\n  > (M)IST REPORT (N)INE-LINE (E)XIT TO MENU")
    cmd = input("\n  > ").upper()
    if cmd == 'M':
        for line in ["M: Mechanism", "I: Injury", "S: Signs", "T: Treatment"]:
            input(f"  {line}: ")
    elif cmd == 'N':
        for i in range(1, 10):
            input(f"  LINE {i}: ")
    print("\n  > TRANSMITTED ...")
    time.sleep(1)

while True:
    clear()
    choice = input("\n  > (D)RILL (S)TRESS (E)XIT : ").upper()
    if choice == 'D': run_drill(stress=False)
    elif choice == 'S': run_drill(stress=True)
    elif choice == 'E': sys.exit()
