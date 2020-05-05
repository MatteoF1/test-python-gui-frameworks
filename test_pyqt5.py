''' App allowing to talk with a chatbot.
 Run the script to open a window and start discussing
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import PyQt5.QtWidgets as widgets
import sys

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great. And you?",
    "That is good to hear.",
    "Thank you.",
    "You're welcome.",
    "How old are you?",
    "I am 28.",
    "How are you?",
    "I'm doing great. And you?",
    "Hi",
    "Hi.",
    "Where do you live?",
    "In your heart.",
    "I am fine.",
    "I'm happy to hear that.",
    "Thanks.",
    "No problem.",
    "istest",
    "No, this is production.",
    "test",
    "No, this is production."
]

'''Class allowing to implement a discussion
'''
class Discussion(widgets.QWidget):

    '''Initialization'''
    def __init__(self, chatbot: ChatBot = None):
        super().__init__()

        # chatbot instance
        self.__chatbot = chatbot

        # configuring layout
        self.__layout = widgets.QFormLayout()

        # introduction
        self._print_text('Start','What do you want to say?')

        # configuring button to send text
        self.__send_button = widgets.QPushButton('Send', self)
        self.__send_button.setCheckable(True)

        # connect the button to the method that manages the click event
        self.__send_button.clicked[bool].connect(self._send_message)

        # configuring input element
        self.__input = widgets.QLineEdit()

        self.__layout.addRow('Write something: ', self.__input)
        self.__layout.addRow('Send: ', self.__send_button)

        # configuring window
        self.setLayout(self.__layout)
        self.setWindowTitle("Discussion")

    '''Sends user input to print out and makes another question'''
    def _send_message(self):
        self._print_text('B', self.__input.text(), self.__layout.rowCount() - 2)
        self._print_text('A', str(self._get_response(self.__input.text())), self.__layout.rowCount() - 2)
        self.__input.clear()
        widgets.QApplication.processEvents()
        pass

    '''Prints out'''
    def _print_text(self, sender: str, msg: str, index: int = None):
        if index != None:
            self.__layout.insertRow(index, sender + ': ', widgets.QLabel(msg))
        else:
            self.__layout.addRow(sender + ': ', widgets.QLabel(msg))

    def _get_response(self, input: str):
        if self.__chatbot:
            return self.__chatbot.get_response(input)
        else:
            return 'Test Response'

if __name__ == '__main__':

    # instantiating chatbot and training it a bit
    chatbot = ChatBot("Wolly")
    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    # instantiating widget
    app = widgets.QApplication(sys.argv)
    this_discussion = Discussion(chatbot)
    this_discussion.show()
    sys.exit(app.exec_())