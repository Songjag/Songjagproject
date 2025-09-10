import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hãy nói gì đó...")
    audio = r.listen(source)

try:
    text = r.recognize_bing(audio, language="vi-VN")
    print("Bạn nói:", text)
except sr.UnknownValueError:
    print("Không nghe rõ.")
except sr.RequestError as e:
    print(f"Lỗi API hoặc kết nối: {e}")