from tkinter import*
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog


def long_encypt_tran():
    tran = scroll.get('1.0', END)
    tran = tran[:-1]

    if  var.get() == 0:
        scroll.delete("1.0", END)
        for char in tran:
            ind_m = m.index(char)
            scroll.insert("1.0", a[ind_m])      

    if  var.get() == 1:
        scroll.delete("1.0", END) 
        for char_2 in tran:
            ind_a = a.index(char_2)
            scroll.insert("1.0", m[ind_a])
    
tk = Tk()  
tk.title('EnCoder') 
tk.geometry('900x485+480+200') 
tk.resizable(width = False, height= False)  
tk.iconbitmap('EnCoder.ico')
var = IntVar()
var.set(0)

decr = Radiobutton(text = "Зашифрувати", font = ('Times New Roman', 16, 'bold'), variable = var, value = 0)
encr = Radiobutton(text = "Розшифрувати", font = ('Times New Roman', 16, 'bold'), variable = var, value = 1)

decr.place(x = 15, y = 90,  anchor = W)
encr.place(x = 15, y = 120, anchor = W)


coder_name = Label(
    tk,
    text = 'Шифратор',
    bg = 'light gray',
    fg = 'black',
    font = ('Comic Sans MS', 20, 'bold'),
    relief = GROOVE,
)
coder_name.place(x = 15, y = 15, width = 870, height = 45)

scroll = ScrolledText(
    wrap = 'word'
)
scroll.insert('1.0', 'Введіть текст:')
scroll.place(x = 15, y = 140, width = 870, height = 200)

delete_butt = Button(
    tk,
    text = 'Очистити поле',
    bg = 'gray',
    fg = 'black',
    relief = RAISED,
    font = ('Times New Roman', 19, 'bold'),
    command = lambda:(
        scroll.delete(1.0, END),
    )
)
delete_butt.place(x = 40, y = 355, width = 250, height = 45)

process_butt = Button(
    tk, 
    text = 'Обробити',
    bg = 'gray',
    fg = 'black',
    relief = RAISED,
    font = ('Times New Roman', 19, 'bold'),
    command = lambda:(
            long_encypt_tran(),
    )
)
process_butt.place(x = 325, y = 355, width = 250, height = 45)


def open_file():
    filepath = filedialog.askopenfilename()
    
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            scroll.delete("1.0", END)
            scroll.insert("1.0", text)

    if filepath == "":
        count_filepath = 0
        count_filepath += 1

open_button = Button(
    tk,
    text="Відкрити файл",
    bg = 'grey',
    fg = 'black',
    relief = RAISED,
    font = ('Times New Roman', 19, 'bold'),
    command=open_file
)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
open_button.place(x = 40, y = 420, width = 350, height = 45)
 

def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        initialfile = 'EnCoder.txt',
        filetypes=[
            ('Текстовий документ', '*.txt'), 
            ('CSV', '*.csv'),
            ('Усі файли','*.*')
        ]
    )
    if filepath != "":
        text = scroll.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)

save_button = Button(
    tk,
    text="Зберегти файл",
    bg = 'grey',
    fg = 'black',
    relief = RAISED,
    font = ('Times New Roman', 19, 'bold'),
    command=save_file
)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)
save_button.place(x = 510, y = 420, width = 350, height = 45)

def copy_butt_():
    text = scroll.get('1.0', END)
    if scroll.insert('1.0', '') == ' ':
        print('space')
    if not(text) == ' ':
        tk.clipboard_clear()
        tk.clipboard_append(text)

copy_butt = Button(
    tk,
    text = 'Копіювати',
    bg = 'gray',
    fg = 'black',
    relief = RAISED,
    font = ('Times New Roman', 19, 'bold'),
    command = lambda:(
        copy_butt_()
    )
)
copy_butt.place(x = 610, y = 355, width = 250, height = 45)

m = [' ','\n',
     'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     '0','1','2','3','4','5','6','7','8','9',
     '!','?','"','№','#',';',':','%','@','*','+','-','=','&','^','_','$','(',')','[',']','{','}','/','<','>','.',',','—',

     'А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І','Ї','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ь','Ю','Я',
     'а','б','в','г','ґ','д','е','є','ж','з','и','і','ї','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ю','я']

a = [' ','\n',
     'Z','q','G','R','k','m','A','z','F','I','c','S','w','K','o','i','f','u','h','n','N','T','t','l','x','p',
     'j','P','L','g','v','M','E','C','W','b','Q','U','H','Y','V','s','y','X','a','D','B','d','J','e','r','O',
     '4','6','8','9','1','0','7','5','2','3',
     '%','$','(','^','*','<','/','{',';','[','&','@',',','-','?','_','.','}','+','>','#','"','№','=','!',':',']',')','—',

     'к','Н','б','Л','р','О','Р','Ш','є','н','ф','я','Т','Ц','Д','Г','и','ь','П','с','Ґ','ц','Б','м','у','Ю','Й','В','ж','е','С','л','д',
     'І','а','в','М','ч','Ч','Ж','з','щ','И','Е','х','г','Ф','Щ','К','ю','Ї','ш','п','ґ','Я','З','Х','о','й','ї','і','А','Є','т','Ь','У']

tk.mainloop()
