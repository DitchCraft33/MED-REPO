import os, sys, time, json, random

def load_data():
    try:
        with open('medevac_data.json', 'r') as f:
            return json.load(f)
    except:
        print("\n  !! DATA FILE MISSING !!")
        sys.exit()

DATA = load_data()

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_hud(sitrep_text, timer_text=None):
    clear()
    header = timer_text if timer_text else "9L CASEVAC REQUEST"
    print(f"\n  [ {header} ]")
    print(f"\n  SITREP ...")
    print(f"\n  {sitrep_text}\n")

def run_9line():
    scenario = random.choice(DATA["SCENARIOS"])
    display_hud(scenario['sitrep'])
    
    print("  > PRESS ENTER TO START TRANSMISSION...")
    input()
    
    start_time = time.time()
    user_report = {}
    l5_timer_display = None

    for i in range(1, 10):
        key = f"L{i}"
        display_hud(scenario['sitrep'], l5_timer_display)
        
        if key in DATA["BREVITY"]:
            b = DATA["BREVITY"][key]
            print(f"  > LINE {i} : {b['header']}")
            print(f"  > {b['opts']}")
        else:
            label = DATA["LABELS"].get(key, "REQUIRED")
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
        print(f"\n  > HINT : {scenario['hint']}")

    input("\n\n  > ENTER TO RESET ...")

if __name__ == "__main__":
    while True:
        clear()
        choice = input("\n  > (D)RILL (E)XIT : ").upper()
        if choice == 'D': run_9line()
        elif choice == 'E': sys.exit()
