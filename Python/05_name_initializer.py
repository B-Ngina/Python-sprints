def get_initials(name):
    parts = name.split()
    initials = []
    for part in parts:
        initials.append(f"{part[0].upper()}.")

    return "".join(initials)
