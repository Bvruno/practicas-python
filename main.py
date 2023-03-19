from tkinter import *

raiz=Tk()
raiz.title("Bot Twitch")
raiz.resizable(True, True)#modifica el tamaño de la ventana
raiz.iconbitmap("twitchbot.ico")#modifica el icono de la ventana
raiz.config(bg="black")#modifica el color de la ventana
raiz.geometry("500x500")#modifica el tamaño de la ventana

miFrame=Frame(raiz, width=300,height=500)
miFrame.config(bg="white")#modifica el color de la ventana
miFrame.config(width=300,height=500)#modifica el color de la ventana
miFrame.pack(side="right")


entryToken=Entry(miFrame)
entryToken.config(show="*")
entryToken.grid(row=0, column=1, padx=5,pady=5)
labelToken=Label(miFrame, text="Token: ").grid(row=0, column=0, sticky="e", padx=5,pady=5)
entryNick=Entry(miFrame)
entryNick.grid(row=1, column=1, padx=5,pady=5)
labelNick=Label(miFrame, text="Nick: ").grid(row=1, column=0, sticky="e", padx=5,pady=5)
entryPath=Entry(miFrame)
entryPath.grid(row=2, column=1, padx=5,pady=5)
labelPath=Label(miFrame, text="Path: ").grid(row=2, column=0, sticky="e", padx=5,pady=5)

textDescripcion=Text(miFrame, width=15, height=5)
textDescripcion.grid(row=4,column=1, padx=5,pady=5)
scrollbarDescripcion=Scrollbar(miFrame, command=textDescripcion.yview)
scrollbarDescripcion.grid(row=4,column=2,sticky="nsew",pady=5)
textDescripcion.config(yscrollcommand=scrollbarDescripcion.set)
labelDescripcion=Label(miFrame, text="Descripcion: ").grid(row=4, column=0, sticky="e", padx=5,pady=5)

def enviar():
    print("El token es: " + entryToken.get())

botonEnvio=Button(miFrame, text="Enviar", command=enviar)
botonEnvio.grid(row=5,column=1,padx=10,pady=10)

def ocultar():
    entryToken.config(show="*")
    botonMostrar.config(text="Mostrar", command=mostrar)

def mostrar():
    print("El token es: " + entryToken.get())
    entryToken.config(show="")
    botonMostrar.config(text="Ocultar", command=ocultar)

botonMostrar=Button(miFrame, text="Mostrar", command=mostrar)
botonMostrar.grid(row=0,column=3,padx=10,pady=10)

opcion=StringVar()

def imprimir():
    print(opcion.get())


Label(miFrame, text="Seleccione una opcion").grid(row=6, column=0)
Radiobutton(miFrame, text="Evento", command=imprimir, variable=opcion, value="event").grid(row=7, column=0)
Radiobutton(miFrame, text="Comando", command=imprimir, variable=opcion, value="command").grid(row=8, column=0)

raiz.mainloop()