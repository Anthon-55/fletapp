import flet as ft

def main(page: ft.Page):
    lt = ["Maca", "vinho"]

    lista_prod = ft.ListView()

    def cadastrar(e):
        try:
            lista_prod.controls.append(
                ft.Container(
                    ft.Text(produto.value),
                    bgcolor = ft.colors.BLACK12,
                    padding = 15,
                    alignment = ft.alignment.center,
                    margin=3,
                    border_radius = 100
                )
            )
            txt_error.visible = False
            txt_acerpt.visible = True
        except:
            txt_error.visible = True
            txt_acerpt.visible = False
        page.update()

    txt_error = ft.Container(ft.Text("Erro ao cadastrar o produto"), visible=False, bgcolor = ft.colors.RED, padding=10, alignment = ft.alignment.center)
    txt_acerpt = ft.Container(ft.Text("Sucesso ao cadastrar o produto"), visible=False, bgcolor = ft.colors.GREEN, padding=10, alignment = ft.alignment.center)

    
    page.title = "Cadastro app"
    txt_title = ft.Text("titulo de produto")
    produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT)

    txt_preco = ft.Text("Preço do produto")
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align = ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    
    page.add(
        txt_error,
        txt_acerpt,
        txt_title,
        produto,
        txt_preco,
        preco,
        btn_produto
    )
    for p in lt:
        lista_prod.controls.append(
            ft.Container(
                ft.Text(p),
                bgcolor = ft.colors.BLACK12,
                padding = 15,
                alignment = ft.alignment.center,
                margin=3,
                border_radius = 100
            )
        )

    page.add(
        lista_prod,
    )
        

ft.app(target=main)
