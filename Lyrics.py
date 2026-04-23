import time
import sys

def print_lyrics():
    lyrics = [
        "Main ab kyun hosh mai aata nahi?",
        "Sukoon kyun dil yeh pata nahi?",
        "Kyun torrun khud sai jo thay waaday",
        "Ke ab yeh ishq nibhana nahi",
        "Main morrun tum sai jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaanay mera dard",
        "Tujey yeh nazar kyun aata nahi",
        "Sohneya Yoon Tera Sharmana",
        "Meri Jaan Na Le Le",
        "Kaan Ke Pichhe Zulf Chhupaana",
        "Meri Jaan Kya Kehne"
    ]

    delays = [
        0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.6,0.5, 0.4, 0.4
    ]

    print("Playing-Pal Pal... \n")
    time.sleep(0.8)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.2)
print_lyrics()
