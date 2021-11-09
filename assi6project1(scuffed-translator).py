from tkinter import*
from tkinter.font import Font
from tkinter import messagebox
WORDBANK = []



def translatorENGtoPers(input_text):
    global WORDBANK

    with open('text.txt', 'r') as f:
            text = f.read()
            words = text.split('\n')


    for i in range(0, len(words), 2):
        WORDBANK.append({'english': words[i], 'persian': words[i + 1]})
    text_string = ""

    user_words = input_text.split(' ')
    for user_word in user_words:
        for word in WORDBANK:
            if user_word == word['english']:
                text_string += word['persian'] + ' '
                break
        else:
            text_string += user_word + ' '

    return text_string
    f.close()

def translatorPersToEng(input_text):
    global WORDBANK

    with open('text.txt', 'r') as f:
            text = f.read()
            words = text.split('\n')



    for i in range(0, len(words), 2):
        WORDBANK.append({'english': words[i], 'persian': words[i + 1]})
    text_string = ""

    user_words = input_text.split(' ')
    for user_word in user_words:
        for word in WORDBANK:
            if user_word == word['persian']:
                text_string += word['english'] + ' '
                break
        else:
            text_string += user_word + ' '

    return text_string
    f.close()



def EngToPers():

    root1 = Tk()
    root1.title("English to Persian")
    root1.geometry("950x100")

    input = Entry(root1, width=30, bg="#D3D3D3", fg='black', font=(10))
    input.grid(row=1, column=1)


    def clicker():
        user_input = input.get()  # input
        result = translatorENGtoPers(user_input)
        Cosmetic_Label = Label(root1, text=result, bg='#D3D3D3', padx=120, font=(10))
        Cosmetic_Label.grid(row=1, column=3)



    Cosmetic_Label = Label(root1,text = ' ',bg= '#D3D3D3',padx = 120,font = (10))
    Cosmetic_Label.grid(row = 1, column = 3)

    Cosmetic_Label = Label(root1, text=' ', padx=95)
    Cosmetic_Label.grid(row=2, column=2)

    Cosmetic_Label = Label(root1, text='input your sentence(ENGLISH)', padx=95)
    Cosmetic_Label.grid(row=2, column=1)

    Cosmetic_Label = Label(root1, text='Persian Translation', padx=95)
    Cosmetic_Label.grid(row=2, column=3)

    button_final = Button(root1, text = "Translate",width = 10,font = ("bold",10),command = clicker)
    button_final.grid(row = 1 , column = 2)


    mainloop()


def PersToEng():
    root1 = Tk()
    root1.title("Persian to English")
    root1.geometry("950x100")

    input = Entry(root1, width=30, bg="#D3D3D3", fg='black', font=(10))
    input.grid(row=1, column=1)

    def clicker():
        user_input = input.get()  # input
        result = translatorPersToEng(user_input)
        Cosmetic_Label = Label(root1, text=result, bg='#D3D3D3', padx=120, font=(10))
        Cosmetic_Label.grid(row=1, column=3)

    Cosmetic_Label = Label(root1, text=' ', bg='#D3D3D3', padx=120, font=(10))
    Cosmetic_Label.grid(row=1, column=3)

    Cosmetic_Label = Label(root1, text=' ', padx=95)
    Cosmetic_Label.grid(row=2, column=2)

    Cosmetic_Label = Label(root1, text='input your sentence(PERSIAN)', padx=95)
    Cosmetic_Label.grid(row=2, column=1)

    Cosmetic_Label = Label(root1, text='English Translation', padx=95)
    Cosmetic_Label.grid(row=2, column=3)

    button_final = Button(root1, text="Translate", width=10, font=("bold", 10), command=clicker)
    button_final.grid(row=1, column=2)

    mainloop()

def word_adder():
    root = Tk()
    root.title("Add new word")
    root.geometry("400x100")
    input1 = Entry(root, width=15, bg="#D3D3D3", fg='black', font=(10))
    input1.grid(row=1, column=1)
    input2 = Entry(root, width=15, bg="#D3D3D3", fg='black', font=(10))
    input2.grid(row=2, column=1)

    def clicker():
        with open('text.txt', 'a+') as f:
            f.write(f'\n{input1.get()}')
            f.write(f'\n{input2.get()}')
        myLabel = Label(root,text = "task successfully completed")
        myLabel.grid(row=5,column=1)
        f.close()

    Cosmetic_Label = Label(root, text=' <--- Enter the English word here', padx=15)
    Cosmetic_Label.grid(row=1, column=2)
    Cosmetic_Label = Label(root, text=' <--- Enter the Persian word here', padx=15)
    Cosmetic_Label.grid(row=2, column=2)
    button = Button(root,text = 'Add' , width = 20,command = clicker)
    button.grid(row=4, column =1)


    mainloop()


def exiter():
    quit()







def main():


    root = Tk()
    root.title("Translator")
    root.geometry("320x165")
    try:
        f = open("text.txt",'r')
        f.close()
    except:
        messagebox.showerror("showerror", "File couldnt load")
        quit()

    #gui
    MyLabel = Label(root, text = "BETTER THAN GOOGLE TRANSLATE",pady=5,padx = 65,fg= "black",bg = "silver" )
    MyLabel.grid(row = 0 , column = 20)
    MyButton1 = Button(root,text ="Persian to English",pady=5,padx = 110 ,fg= "black",bg = "#32CD32",command =PersToEng )
    MyButton1.grid(row = 1, column = 20)
    MyButton2 = Button(root, text="English to Persian", pady=5, padx=110, fg="black", bg="white" ,command = EngToPers )
    MyButton2.grid(row=2, column=20)
    MyButton3 = Button(root, text="Add new word to text", pady=5, padx=100, fg="black", bg="#FF4433",command = word_adder)
    MyButton3.grid(row=3, column=20)
    MyButton4 = Button(root, text="Exit", pady=5, padx=148, fg="black", bg="gold",command = exiter)
    MyButton4.grid(row=4, column=20)


    mainloop()





if __name__ == '__main__':
    main()

