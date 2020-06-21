def speak(msg):
    os.system('espeak "{}" --stdout | aplay'.format(msg))