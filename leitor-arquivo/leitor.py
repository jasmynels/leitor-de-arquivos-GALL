import tkinter as tk
from tkinter import filedialog


def open_file():
    # abre a caixa de diálogo para selecionar o arquivo
    filepath = filedialog.askopenfilename()

    # lê o conteúdo do arquivo selecionado
    with open(filepath, 'r') as f:
        content = f.read()


    # separando o conteudo por espaços e transformando em um array
    content_arr = content.split(" ")
    # a partir da posição 42 que começa o nome da pessoa
    # content_new = content_arr[42]
    content_new = content_arr
    # criando a lista que vai receber o nome da pessoa
    nome = []
    # fazendo um for que começa pela posição 42 do array (pelo nome da pessoa) e termina no primeiro espaço longo;
    for i in range(15, len(content_new)):
        if (len(content_new[i]) > 80):
            pessoa = content_new[i][114:]
            nome.append(pessoa)
            if (content_new[i + 1] != ''):
                nome.append(content_new[i + 1])
            if (content_new[i + 2] != ''):
                nome.append(content_new[i + 2])
            if (content_new[i + 3] != ''):
                nome.append(content_new[i + 3])
            if (content_new[i + 4] != ''):
                nome.append(content_new[i + 4])
            if (content_new[i + 5] != ''):
                nome.append(content_new[i + 5])
            nome.append("\n")


    nome_new = " ".join(nome)
    print(nome_new)

    save_path = filedialog.asksaveasfilename(defaultextension='.txt')

    #  salvando o novo conteúdo no arquivo selecionado
    with open(save_path, 'w',  newline='') as file:
        file.write(nome_new)


# cria a janela principal
root = tk.Tk()
root.title("Leitor de Arquivo")

# define as dimensões da janela
largura = 400
altura = 350

# define a posição da janela na tela
posicao_x = (root.winfo_screenwidth() - largura) // 2
posicao_y = (root.winfo_screenheight() - altura) // 2

# define a geometria da janela
root.geometry("{}x{}+{}+{}".format(largura, altura, posicao_x, posicao_y))

# carrega a imagem de fundo
background_image = tk.PhotoImage(file='./logo-gall.png')

# cria um widget de label para a imagem de fundo e preenche toda a janela
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# cria o botão "Abrir arquivo" e o centraliza
button = tk.Button(root, text="Abrir arquivo",command=open_file, bg='orange', fg='white')
button.pack()


# inicia o loop principal da interface gráfica
root.mainloop()
