from guizero import App, Text, TextBox, PushButton, Slider, Window

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value
    
def generate():
    textApp = Window(app, title="Ticket")
    nameHeader = Text(textApp, text="Name:")
    name = Text(textApp, text=my_name.value)
    textApp.show()

app = App(title="Hello world")
#Add widgets below this line.
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="Green")
my_name = TextBox(app, width="50")
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=40)
generator = PushButton(app, command=generate, text="Generate Text")
#Add widgets above this line.
app.display()
