import customtkinter as ctk
from tkinter import messagebox

class PharmacyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.title('Farmácia San Paolo')
        self.geometry('500x700')
        
        # Configuração do tema
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')

        self.create_widgets()

    def create_widgets(self):
        # Título
        self.label_titulo = ctk.CTkLabel(self, text='Seja Bem Vindo(a)!', text_color='red', font=('Arial', 30, 'bold', 'italic'))
        self.label_titulo.pack(pady=20)

        # Entrada de Valor
        self.label_valor = ctk.CTkLabel(self, text='Digite o valor total da compra:', font=('Arial', 16))
        self.label_valor.pack(pady=(10, 5))

        self.entry_valor = ctk.CTkEntry(self, placeholder_text='R$ 0.00', width=200, font=('Arial', 14))
        self.entry_valor.pack(pady=5)

        # Seção de Pagamento
        self.label_pagamento = ctk.CTkLabel(self, text='Forma de Pagamento:', font=('Arial', 16, 'bold'))
        self.label_pagamento.pack(pady=(30, 10))

        # Botões de Pagamento
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(pady=10)

        self.btn_dinheiro = ctk.CTkButton(self.frame_botoes, text='Dinheiro', command=self.pagar_dinheiro, width=150, corner_radius=20, hover_color='#3385ff')
        self.btn_dinheiro.grid(row=0, column=0, padx=10, pady=10)

        self.btn_cartao_vista = ctk.CTkButton(self.frame_botoes, text='Cartão à Vista', command=self.pagar_cartao_vista, width=150, corner_radius=20, hover_color='#3385ff')
        self.btn_cartao_vista.grid(row=0, column=1, padx=10, pady=10)

        # Seção de Parcelamento
        self.frame_parcelado = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_parcelado.pack(pady=20)

        self.label_parcelado = ctk.CTkLabel(self.frame_parcelado, text='Cartão de Crédito Parcelado:', font=('Arial', 14))
        self.label_parcelado.pack(pady=5)

        self.combo_parcelas = ctk.CTkComboBox(self.frame_parcelado, values=['2x', '3x', '4x', '5x', '6x'], width=200)
        self.combo_parcelas.set('Selecione as parcelas')
        self.combo_parcelas.pack(pady=5)

        self.btn_confirmar_parcelado = ctk.CTkButton(self.frame_parcelado, text='Confirmar Parcelamento', command=self.pagar_cartao_parcelado, width=200, corner_radius=20, hover_color='#3385ff')
        self.btn_confirmar_parcelado.pack(pady=10)

        # Botão Finalizar
        self.btn_finalizar = ctk.CTkButton(self, text='Finalizar Compra', command=self.finalizar_compra, width=200, height=40, hover_color='#ff3333', fg_color='red', font=('Arial', 16, 'bold'))
        self.btn_finalizar.pack(side='bottom', pady=40)

    def validar_valor(self):
        try:
            valor_str = self.entry_valor.get().replace('R$', '').replace(',', '.').strip()
            valor = float(valor_str)
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido maior que zero.")
            return None

    def mostrar_mensagem_sucesso(self, titulo, mensagem):
        top = ctk.CTkToplevel(self)
        top.title(titulo)
        top.geometry('400x200')
        top.transient(self) # Mantém a janela na frente da principal
        
        label = ctk.CTkLabel(top, text=mensagem, text_color='green', font=('Arial', 20, 'bold'), wraplength=350)
        label.pack(expand=True, padx=20, pady=20)
        
        btn_fechar = ctk.CTkButton(top, text="Fechar", command=top.destroy)
        btn_fechar.pack(pady=20)

    def pagar_dinheiro(self):
        valor = self.validar_valor()
        if valor:
            self.mostrar_mensagem_sucesso('Dinheiro', f'Pagamento de R$ {valor:.2f} em Dinheiro recebido.\nVolte Sempre!')

    def pagar_cartao_vista(self):
        valor = self.validar_valor()
        if valor:
            self.mostrar_mensagem_sucesso('Cartão à Vista', f'Pagamento de R$ {valor:.2f} no Cartão à Vista aprovado.\nVolte Sempre!')

    def pagar_cartao_parcelado(self):
        valor = self.validar_valor()
        if not valor:
            return

        parcelas_str = self.combo_parcelas.get()
        if parcelas_str == 'Selecione as parcelas':
            messagebox.showwarning("Atenção", "Selecione o número de parcelas.")
            return

        num_parcelas = int(parcelas_str.replace('x', ''))
        valor_parcela = valor / num_parcelas
        
        self.mostrar_mensagem_sucesso('Cartão Parcelado', f'Pagamento de R$ {valor:.2f} parcelado em {num_parcelas}x de R$ {valor_parcela:.2f}.\nVolte Sempre!')

    def finalizar_compra(self):
        if messagebox.askyesno("Finalizar", "Deseja realmente finalizar o sistema?"):
            self.destroy()

if __name__ == "__main__":
    app = PharmacyApp()
    app.mainloop()








