import speech_recognition as sr
import streamlit as st
import google.generativeai as palm


palm.configure(api_key="AIzaSyBHFH2xfKgxvIxEJL7EVyXIg64a3JmKQkI") 

def main():
    st.title("code generator by speech")

    # Initialize speech recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Speak your programming request (say 'stop' to end):")

        # Continuously listen to the microphone
        while True:
            try:
                audio = r.listen(source)
                speech_text = r.recognize_google(audio).lower()

                # Stop listening if the user says 'stop'
                if speech_text == "stop":
                    break

                # Display what was said
                st.write(f"You said: {speech_text}")

                # Generate code
                prompt = f"generate a code for {speech_text} in the preferred language and give a explaination "
                response = palm.generate_text(prompt=prompt)

                st.subheader("Generated Code:")
                st.code(response.result)  # 

            except sr.UnknownValueError:
                st.write("Could not understand audio")
            except sr.RequestError as e:
                st.write(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
