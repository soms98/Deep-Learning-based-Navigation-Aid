def suggest(detection):
    d = {
        "person": "ask person to move aside.",
        "chair": "Chair is movable",
        "bicycle": "Move left or move right",
        "bottle": "Bottle is movable so you can move it",
        "bus": "move away",
        "car": "move away",
        "diningtable": "move gently",
    }
    return d[detection] if detection in d else ""
