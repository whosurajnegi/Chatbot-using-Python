# Chatbot-using-Python
Chatbot with voice integration
Using voice commands has become pretty ubiquitous nowadays, as more mobile phone users use voice assistants such as Siri and Cortana, and as devices such as Amazon Echo and Google Home have been invading our living rooms. These systems are built with speech recognition software that allows their users to issue voice commands. Now, our web browsers will become familiar with to Web Speech API, which allows users to integrate voice data in web apps. In this project we will develop a Chatbot in python platform using Chatterbot (0.8.7) python library and speech recognition API to recognize voice and interact with the user. Before that lets know more about Chatbots. 
Software Requirements:
1.	Python 3.7
2.	Chatterbot (0.8.7)
3.	Speech Recognition API
4.	PyAudio 
5.	GTTS (Google text to speech)

Objectives:
  Now we have installed all the required software and API to start creating our Voice assistant.
•	First, we have to create a Bot for which we will call chatterbot API and create a chatbot with a list Trainer.
•	Once the chatbot is created we have to provide a voice input to our Bot, we will call speech recognition API to recognize user voice and convert it into text (Speech-to-text)
•	For the bot to reply back we have to call gTTS API which will convert text responses to speech (text-to-speech).

Source Code:
   First, we will create an instance to call gTTS API in the bot with two variables “text” and “language”. Text will define the statement that to be converted to speech language is to define the output audio type like ‘English-en’ ‘French-fn’ ‘Japanese-jp’. We called this as “speak”, Its source code is given below:

