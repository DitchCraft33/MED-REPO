import os, sys, time, json, random

def load_all_data():
    try:
        with open('medic_data.json', 'r') as f:
            medic_data = json.load(f)
        with open('medic_procs.json', 'r') as f:
            procs = json.load(f)
        with open('medevac_data.json', 'r') as f:
            medevac_data = json.load(f)
        return medic_data, procs, medevac_data
    except Exception as e:
        print(f"\n  !! ERROR : Data files missing !!\n  {e}")
        sys.exit()

DATA, PROCS, EVAC = load_all_data()

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_evac_hud(sitrep_text, timer_text=None):
    clear()
    header = timer_text if timer_text else "9L CASEVAC REQUEST"
    print(f"\n  [ {header} ]")
    print(f"\n  SITREP ...")
    print(f"\n  {sitrep_text}\n")

def run_9line_trainer():
    scenario = random.choice(EVAC["SCENARIOS"])
    display_evac_hud(scenario['sitrep'])
    
    print("  > PRESS ENTER TO START TRANSMISSION...")
    input()
    
    start_time = time.time()
    user_report = {}
    l5_timer_display = None

    for i in range(1, 10):
        key = f"L{i}"
        display_evac_hud(scenario['sitrep'], l5_timer_display)
        
        if key in EVAC["BREVITY"]:
            b = EVAC["BREVITY"][key]
            print(f"  > LINE {i} : {b['header']}")
            print(f"  > {b['opts']}")
        else:
            label = EVAC["LABELS"].get(key, "REQUIRED")
            print(f"  > LINE {i} : {label}")
        
        ans = input("\n  > ").upper().strip()
        user_report[key] = ans
        
        if i == 5:
            l5_elapsed = time.time() - start_time
            l5_timer_display = f"LINE 5 SENT AT {l5_elapsed:.1f}s"

    total_time = time.time() - start_time
    
    clear()
    print(f"\n  --- VALIDATING TRANSMISSION ---")
    errors = 0
    for k in range(1, 10):
        key = f"L{k}"
        correct = scenario['solution'].get(key, "")
        if user_report[key] != correct:
            print(f"\n  !! ERROR {key} !! Entered: {user_report[key]} | Correct: {correct}")
            errors += 1
    
    if errors == 0:
        print(f"\n\n  > TRANSMISSION CLEAN ({total_time:.1f}s)")
    else:
        print(f"\n\n  > {errors} ERRORS DETECTED.")
        print(f"  > HINT: {scenario['hint']}")

    input("\n\n  > ENTER TO RETURN TO MENU ...")

def run_procedures():
    while True:
        clear()
        print("\n  PROCEDURES : (M.A.R.C.H)-(P)AWS (B)URNS (F)CPR (I)MIST (9)LINE-EXT (E)xit")
        print("\n  MARCH // ... // PAWS  ")
        print(" ")
        print("  > (M)ASSIVE HEMORRHAGE")
        print("  > (A)IRWAY MANAGEMENT")
        print("  > (R)ESPIRATION")
        print("  > (C)IRCULATION")
        print("  > (H)YPOTHERMIA / HEAD")
        print("  ")
        print("  > (P)AIN MANAGEMENT // ANTIBIOTICS // WOUNDS // SPLINTING")
        print("\n  > (B)URNS // SEVERITY  ")
        print("  ")
        print("  > (F)CPR  // CONSIDERATIONS")
        print("\n  IMIST HANDOVER REPORT // 9 LINE MEDEVAC")
        print("  ")
        print("  > (I)DENTIFICATION // MECHANISM // INJURIES // SYMPTOMS // TREATMENT")
        print("  > (9)LINE EXTRACTION ... REQ ASAP // LINES 1 ... 5 // LINES 6 ... 9  ")
        print("\n  > ", end="")
        
        choice = input().upper().strip()
        if choice == 'E': break
        if choice in PROCS:
            clear()
            print(f"\n  {PROCS[choice]['title']}")
            for line in PROCS[choice]['lines']:
                print(f"  {line}")
            print("\n  > ", end="")
            input()

def display_hud(sitrep_text, header_text="MEDIC DRILL"):
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
            input("\n  > ENTER TO RESET ..."); return

        correct_ans = scenario['solution'].get(key, "") 
        if ans == correct_ans:
            print(f"\n  [ OK ] ({elapsed:.1f}s)")
            time.sleep(1) 
        else:
            print(f"\n\n  !! INCORRECT !!")
            print(f"  > HINT : {scenario['hint']}")
            input("\n  > ENTER TO RESET ..."); return

    print("\n\n  > PROTOCOL COMPLETE ... CASUALTY STABILIZED")
    input("\n  > ENTER TO RETURN TO MENU ...")

while True:
    clear()
    print("\n  TACMED TRAINER : (D)RILL (S)TRESS (9)LINER // (P)ROCEDURES // (E)XIT")
    print("\n  CUF Priorities ( Return Fire // Take Cover )")
    print("\n  > Direct casualty to remain engaged as combatant if appropriate")        
    print("  > Direct casualty to move to cover and apply self-aid if able")
    print("  > Try to keep casualty from sustaining additional wounds")
    print("  > Stop life-threatening external hemorrhage if tactically feasible")        
    print("\n  CUF Assessment ( H2T // Mass Hem // Airway )")                
    print("\n  > Rapid head-to-toe survey (10-15 seconds or as tactically feasible)") 
    print("  > Identifying life-threatening hemorrhage only")                                     
    print("  > Airway management (other than positioning) deferred to TFC")
    print("\n  TFC Initial Actions ( TRI // PRI // MEDEVAC )")                
    print("\n  > Consolidate casualties and Conduct triage to identify priority")
    print("  > Casualties with altered mental status: disarm, secure weapons and comms")
    print("  > Communicate casualty status and MEDEVAC requirements to C2")
                                                                            
    choice = input("\n  > ").upper().strip()    
    if choice == 'D': run_drill(stress=False)
    elif choice == 'S': run_drill(stress=True)
    elif choice == '9': run_9line_trainer()
    elif choice == 'P': run_procedures()
    elif choice == 'E': sys.exit()
