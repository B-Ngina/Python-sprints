from collections import Counter
def triage_blood(bank, patients):
    #Count available inventory and incoming patient requests
    inv = Counter(bank)
    req = Counter(patients)

    total_patients = len(patients)
    patients_served = 0

    #Priority 1: Serve 'O' Patients (Most restrictive)
    # They can ONLY take 'O' blood
    served_o = min(req['O'], inv['O'])
    patients_served += served_o
    inv['O'] -= served_o

    #Priority 2: Serve 'A' Patients
    #Try exact match 'A' first, then fall back to leftover 'O'
    served_a_exact = min(req['A'], inv['A'])
    patients_served += served_a_exact
    inv['A'] -= served_a_exact
    req['A'] -= served_a_exact

    served_a_fallback = min(req['A'], inv['O'])
    patients_served += served_a_fallback
    inv['O'] -= served_a_fallback

    #Priority 3: Serve 'B' Patients
    #Try exact match 'B' first, then fall back to leftover 'O'
    served_b_exact = min(req['B'], inv['B'])
    patients_served += served_b_exact
    inv['B'] -= served_b_exact
    req['B'] -= served_b_exact
    
    served_b_fallback = min(req['B'], inv['O'])
    patients_served += served_b_fallback
    inv['O'] -= served_b_fallback

    #Priority 4: Serve 'AB' Patients (Universal Recipient)
    #They can sweep up whatever remaining blood types are left in the bank
    for blood_type in ['AB', 'A', 'B', 'O']:
        if req['AB'] > 0:
            served_ab = min(req['AB'], inv[blood_type])
            patients_served += served_ab
            inv[blood_type] -= served_ab
            req['AB'] -= served_ab

    #Return the string formatted exactly as requested
    return f"{patients_served} of {total_patients} patients served"

triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"])
#Returns; "4 of 4 patients served" 
