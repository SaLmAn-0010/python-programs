from gtts import gTTS

text = "Hello, welcome my name is salman from bokaro jharkhand and doing some work in laptop for python coding for learing new topic audio!"
tts = gTTS(text=text, lang='en')

tts.save("output.mp3")

print("Audio file saved successfully as output.mp3")