import tkinter as tk
from tkinter import filedialog, messagebox


# ==== Patrón Command ====
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class CambiarTexto(Command):
    def __init__(self, editor, texto_anterior, texto_nuevo):
        self.editor = editor
        self.texto_anterior = texto_anterior
        self.texto_nuevo = texto_nuevo

    def execute(self):
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", self.texto_nuevo)

    def undo(self):
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", self.texto_anterior)


# ==== Historial de comandos ====
class GestorHistorial:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def ejecutar(self, comando):
        comando.execute()
        self.undo_stack.append(comando)
        self.redo_stack.clear()

    def deshacer(self):
        if self.undo_stack:
            comando = self.undo_stack.pop()
            comando.undo()
            self.redo_stack.append(comando)

    def rehacer(self):
        if self.redo_stack:
            comando = self.redo_stack.pop()
            comando.execute()
            self.undo_stack.append(comando)


# ==== Interfaz gráfica ====
class EditorTexto:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto con Undo/Redo (Tkinter)")
        self.root.geometry("600x400")

        self.texto_anterior = ""
        self.historial = GestorHistorial()

        # Área de texto
        self.text_edit = tk.Text(root, wrap="word", undo=False)
        self.text_edit.pack(fill="both", expand=True)

        # Menú
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        menu_editar = tk.Menu(self.menu_bar, tearoff=0)
        menu_editar.add_command(label="Deshacer (Ctrl+Z)", command=self.deshacer)
        menu_editar.add_command(label="Rehacer (Ctrl+Y)", command=self.rehacer)
        self.menu_bar.add_cascade(label="Editar", menu=menu_editar)

        # Atajos de teclado
        root.bind("<Control-z>", lambda e: self.deshacer())
        root.bind("<Control-y>", lambda e: self.rehacer())

        # Detectar cambios en el texto
        self.text_edit.bind("<KeyRelease>", self.registrar_cambio)

    def registrar_cambio(self, event=None):
        texto_nuevo = self.text_edit.get("1.0", tk.END).rstrip("\n")
        if texto_nuevo != self.texto_anterior:
            comando = CambiarTexto(self.text_edit, self.texto_anterior, texto_nuevo)
            self.historial.ejecutar(comando)
            self.texto_anterior = texto_nuevo

    def deshacer(self):
        self.historial.deshacer()
        self.texto_anterior = self.text_edit.get("1.0", tk.END).rstrip("\n")

    def rehacer(self):
        self.historial.rehacer()
        self.texto_anterior = self.text_edit.get("1.0", tk.END).rstrip("\n")


if __name__ == "__main__":
    root = tk.Tk()
    editor = EditorTexto(root)
    root.mainloop()
