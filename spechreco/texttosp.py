#$ pip install gTTS pyttsx3 playsound soundfile transformers datasets sentencepiece openai
from gtts import gTTS
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Path to the audio file
sound_file = "sound_file.mp3"

# Generate audio from text
text_to_speech = gTTS(text='‌ကောင်းထက်စံ ဆရာ ကြောက်လား မှန်မှန်ဖြေမှန်မှန်ဖြေ', lang='my')
text_to_speech.save(sound_file)

# Load the audio file into Pygame
sound = pygame.mixer.Sound(sound_file)

# Play the audio
sound.play()

# Wait for the sound to finish playing
while pygame.mixer.get_busy(): 
    pygame.time.delay(100)