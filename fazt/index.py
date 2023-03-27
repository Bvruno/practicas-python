from tkinter import ttk
from tkinter import *
import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title("Product Application")

        #crendo frame container
        frame = LabelFrame(self.wind, text='Registrar nuevo producto')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        #name imput
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)
        #price imput
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)
        #boton para agregar el producto
        ttk.Button(frame, text='Agregar producto', command=self.add_product).grid(row=3, columnspan=2, sticky=W+E)
        ttk.Button(frame, text='Buscar producto', command=self.search_product).grid(row=4, columnspan=2, sticky=W+E)
        #mensaje
        self.message = Label(text='', fg='red')
        self.message.grid(row=5, column=0,columnspan=2,sticky=W+E)
        #tabla para mostrar
        self.tree = ttk.Treeview(height=10,columns=2)
        self.tree.grid(row=4,column=0,columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)
        #botones
        ttk.Button(text='Eliminar producto', command=self.delete_product).grid(row=6, column=0, sticky=W+E)
        ttk.Button(text='Modificar producto', command=self.modify_product).grid(row=6, column=1, sticky=W+E)

        self.get_products()

    def run_query(self, query, parameters = {}):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_products(self):
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)
        
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=(row[2]))

    def validate(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=0
    
    def get_product_name(self):
        name = self.name.get()
        query = 'SELECT * FROM product WHERE name =?'
        db_row = self.run_query(query, (name))
        return db_row[1]
    
    def add_product(self):
        if self.validate():
            query = 'INSERT INTO product (name, price) VALUES (?,?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Producto {} agregado con exito'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Ingrese todos los datos'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccionar producto'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name =?'
        self.run_query(query, (name,))
        self.message['text'] = 'Producto {} eliminado con exito'.format(name)
        self.get_products()

    def modify_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccionar producto'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title('Modificar producto: {}'.format(name))
        #old nombre
        Label(self.edit_wind, text='Antiguo nombre: ').grid(row=0,column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,value=name),state='readonly').grid(row=0,column=2)
        #new nombre
        Label(self.edit_wind, text='Nuevo nombre: ').grid(row=1,column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1,column=2)
        #old price
        Label(self.edit_wind, text='Antiguo precio: ').grid(row=2,column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,value=old_price),state='readonly').grid(row=2,column=2)
        #new price
        Label(self.edit_wind, text='Nuevo precio: ').grid(row=3,column=1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row=3,column=2)
        #botones
        ttk.Button(self.edit_wind,text='Editar', command=lambda:self.update_produc(
            new_name.get(),new_price.get(),name,old_price)).grid(row=4, columnspan=2, sticky=W+E)

        
        
    def update_produc(self,new_name,new_price,name,price):
        query = 'UPDATE product SET name =?, price =? WHERE name =? and price=?'
        parameters = (new_name,new_price,name,price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Producto {} modificado con exito'.format(name)
        self.get_products()
    
    def search_product(self):
        return
            
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
