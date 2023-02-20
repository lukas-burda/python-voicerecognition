import speech_recognition as sr

rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names())

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print('Ready to recognize! Start speak')
    audio = rec.listen(mic)
    # audiobg = rec.listen_in_background(mic, audio);

    print('Principal:')
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
    # print('De fundo:')
    # texto2 = rec.recognize_google_cloud(audio, language="pt-BR")
    # print(texto2)