import speech_recognition as sr
import matplotlib.pyplot as plt
import jiwer

text_referinta = "Buna dimineata! Bine ai venit! Bine ati venit! Bine ne-am gasit! Aspecte frumoase pentru un inceput de zi si de saptamana! Hai sa vedem."

fisiere_test = [
    {"nume": "/Users/alecsandraiordache/Documents/an4/sem2/ECIP/Project_L6/ex1/ceva1.wav", "distanta": 1},
    {"nume": "/Users/alecsandraiordache/Documents/an4/sem2/ECIP/Project_L6/ex1/ceva.wav",  "distanta": 2},
    {"nume": "/Users/alecsandraiordache/Documents/an4/sem2/ECIP/Project_L6/ex1/ceva2.wav", "distanta": 3},
    {"nume": "/Users/alecsandraiordache/Documents/an4/sem2/ECIP/Project_L6/ex1/ceva3.wav", "distanta": 4}
]

recognizer = sr.Recognizer()

rezultate_distante = []
rezultate_erori = []

print(f"TEXT DE REFERINȚĂ: '{text_referinta}'\n")

for test in fisiere_test:
    fisier = test["nume"]
    distanta = test["distanta"]
    text_obtinut = ""
    eroare_procentuala = 100.0 
    
    print(f"-> Procesăm {fisier} (Distanță: {distanta}m)...")
    try:
        with sr.AudioFile(fisier) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            audio_data = recognizer.record(source)
            
        text_obtinut = recognizer.recognize_google(audio_data, language="ro-RO")
        print(f"   AI a auzit: '{text_obtinut}'")
        
        eroare = jiwer.wer(text_referinta, text_obtinut)
        eroare_procentuala = min(eroare * 100, 100.0)
        
    except sr.UnknownValueError:
        print("   AI nu a înțeles absolut nimic (zgomot încă prea mare).")
    except Exception as e:
        print(f"   Eroare de sistem: {e}")
        continue
        
    print(f"   Eroare calculată (WER): {eroare_procentuala:.2f}%\n")
    
    rezultate_distante.append(distanta)
    rezultate_erori.append(eroare_procentuala)

if rezultate_distante:
    print("Generăm graficul...")
    plt.figure(figsize=(9, 5))
    
    plt.plot(rezultate_distante, rezultate_erori, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5, markersize=8)
    
    plt.title('Impactul Distanței asupra STT (După Reducerea Zgomotului)', fontsize=14, fontweight='bold')
    plt.xlabel('Distanța (Metri)', fontsize=12)
    plt.ylabel('Rata de eroare - WER (%)', fontsize=12)
    
    plt.ylim(-5, 105)
    plt.xticks(rezultate_distante) 
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()