import customtkinter as ctk

#abrir janela
app = ctk.CTk()

#definir tamanho janela e o nome
app.geometry('400x600')
app.title('Farmácia San Paolo')

#definir o tema
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

#escrever uma mensagem na janela
texto = ctk.CTkLabel(app, text='Seja Bem Vindo(a)!', text_color='red', font=('Arial', 35, 'bold', 'italic'))
texto.pack(padx=30, pady=30)
texto = ctk.CTkFont(family='Arial', size=200)
texto1 = ctk.CTkLabel(app, text='Digite o valor total da compra:')
texto1.pack(padx=0, pady=0)

#adicionar campo valores
valor = ctk.CTkEntry(app, placeholder_text='R$')
valor.pack(padx=10, pady=10)

#escrever uma mensagem na janela
text2 = ctk.CTkLabel(app, text='Forma de Pagamento:')
text2.pack(padx=20, pady=20)



# colocar botão
def dinheiro():
    app1 = ctk.CTkToplevel(app)
    app1.title('Dinheiro')
    app1.geometry('450x200')
    texto3 = ctk.CTkLabel(app1, text='Pagamento Realizado.\n\n Volte Sempre!', text_color='green', font=('Arial', 30, 'bold'))
    texto3.pack(padx=40, pady=40)

botao_dinheiro = ctk.CTkButton(app, text='Dinheiro', command=dinheiro, width=10,  corner_radius=20, hover_color='#3385ff')
botao_dinheiro.pack(side='top', padx=0, pady=0)
app.toplevel_window = None

# colocar botão
def cartao_vista():
    app2 = ctk.CTkToplevel(app)
    app2.title('Cartão à Vista')
    app2.geometry('450x200')
    texto4 = ctk.CTkLabel(app2, text='Pagamento Realizado.\n\n Volte Sempre!', text_color='green', font=('Arial', 30, 'bold'))
    texto4.pack(padx=40, pady=40)

botao_cartao = ctk.CTkButton(app, text='Cartão à Vista', command=cartao_vista, width=10, corner_radius=20, hover_color='#3385ff')
botao_cartao.pack(side='top', padx=10, pady=10)
app.toplevel_window = None


# colocar botão
def cartao_parcelado():

    botao_cartao1 = ctk.CTkButton(app, text='Cartão Parcelado', command=cartao_parcelado, width=10, corner_radius=20, hover_color='#3385ff')
    botao_cartao1.pack()

text5 = ctk.CTkLabel(app, text='Cartão de Crédito Parcelado:')
text5.pack(padx=20, pady=20)

parcelas = ctk.CTkComboBox(app, values=['Parcelado 2x', 'Parcelado 3x', 'Parcelado 4x', 'Parcelado 5x', 'Parcelado 6x'],
                               command=cartao_parcelado)
parcelas.set('')
parcelas.pack(side='top', padx=1, pady=1)


# colocar botao e definir a funçao do botao
def finalizar():
    app3 = ctk.CTkToplevel(app)
    app3.title('Compra Finalizada')
    app3.geometry('470x200')
    texto6 = ctk.CTkLabel(app3, text='Compra Finalizada Com Sucesso!\n\n Volte Sempre!', text_color='green', font=('Arial', 25, 'bold'))
    texto6.pack(side='top', padx=40, pady=40)
    app.toplevel_window = None


botao_finalizar = ctk.CTkButton(app, text='Finalizar Compra', command=finalizar,hover_color='#ff3333')
botao_finalizar.pack(padx=50, pady=50)



#mantém janela aberta
app.mainloop()







