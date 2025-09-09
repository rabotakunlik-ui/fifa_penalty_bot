import random

def generate_coupon():
    # 4 ta o'yin kombinatsiyasi
    matches = ["A vs B", "C vs D", "E vs F", "G vs H"]
    selections = [random.choice(["1","X","2"]) for _ in matches]
    coupon = "\n".join([f"{m}: {s}" for m, s in zip(matches, selections)])
    confidence = random.randint(70, 95)
    return coupon, confidence

def check_confidence(conf):
    return conf >= 75
