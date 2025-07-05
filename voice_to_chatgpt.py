import speech_recognition as sr
import openai
import os

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Listening... Please ask your question.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Transcribing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return None

def ask_chatgpt(prompt):
    print("🤖 Sending to ChatGPT...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful customer service assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response['choices'][0]['message']['content']
    print("🗨️ ChatGPT says:", reply)
    return reply

def main():
    user_input = transcribe_speech()
    if user_input:
        response = ask_chatgpt(user_input)

if __name__ == "__main__":
    main()
