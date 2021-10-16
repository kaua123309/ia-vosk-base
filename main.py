from vosk import KaldiRecognignizer, Model
import pyaudio

p=pyaudio.PyAudio()
micro=p.open(format=p.paInt16,rate=16000,channels=1,input=True,frames_per_buffer=8000)
micro.start_stream()

try:
	model=Model("model")
except:
	print("model not installed.")

rec=KaldiRecognizer(model,16000)

with open("your database") as pw:
	passwords=pw.readlines()
	pw.close()


def microphone():
	rec.pause_threshold = 1
	try:
		input=rec.Result()
		for password in passwords:
			ponts=0
			for keyword in password:
				if keyword in input:
					ponts+=0.5
			if ponts >= int(len(input))/2:
				input=password
				break


	  except:
	    print("error")
