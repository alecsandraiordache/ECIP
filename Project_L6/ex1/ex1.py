#a. use 2 machines (PCs/ laptops) inn which one is the emitter of sound and the other is one receptor 
#at a distance of 2m. Use the microphone of the 2nd machine to capture the specific sound, via
#Mathlab scheme. Use mathlab ro apply different strategies (discussed at the beggining of the
#semester) to amplify and clarify this received input. The test must imply a voice conversation,
#that we emitted by machine 1, received by machine 2.
#use native code, not libraries

#b. use the AI to transform the conv of the output signal into a text: STT
# measure the error in relation to distance and make a chart


import wave
import struct

nume_fisier = 'ceva.wav'
print(f"Deschidem {nume_fisier}...")

with wave.open(nume_fisier, 'rb') as wav_file:
    Fs = wav_file.getframerate()
    n_frames = wav_file.getnframes()
    n_channels = wav_file.getnchannels()
    
    raw_bytes = wav_file.readframes(n_frames)
    formata_string = f"<{n_frames * n_channels}h"
    amplitudini = struct.unpack(formata_string, raw_bytes)
    
    if n_channels == 2:
        raw_audio = [(amplitudini[i] + amplitudini[i+1]) / 2.0 / 32768.0 for i in range(0, len(amplitudini), 2)]
    else:
        raw_audio = [x / 32768.0 for x in amplitudini]


print("Aplicăm Low-Pass...")
alpha = 0.4 
smoothed_audio = [0.0] * len(raw_audio)
smoothed_audio[0] = raw_audio[0]

for i in range(1, len(raw_audio)):
    smoothed_audio[i] = alpha * raw_audio[i] + (1.0 - alpha) * smoothed_audio[i-1]


print("Aplicăm Amplificare la volum optim...")
target_peak = 0.95 
current_peak = max(abs(x) for x in smoothed_audio)

if current_peak > 0:
    final_audio = [x * (target_peak / current_peak) for x in smoothed_audio]
else:
    final_audio = smoothed_audio

fisier_final = 'ceva_f1.wav'
print(f"Salvăm rezultatul în {fisier_final}...")

amplitudini_finale = [int(max(min(x, 1.0), -1.0) * 32767) for x in final_audio]
raw_bytes_final = struct.pack(f"<{len(amplitudini_finale)}h", *amplitudini_finale)

with wave.open(fisier_final, 'wb') as wav_out:
    wav_out.setnchannels(1)
    wav_out.setsampwidth(2)
    wav_out.setframerate(Fs)
    wav_out.writeframes(raw_bytes_final)

print("Gata!")