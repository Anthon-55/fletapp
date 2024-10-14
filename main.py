import flet as ft
#import sqlite3 as sq

"""
def conectDB():
    db = sq.connect('assets/database/db.db')
    cursor = db.cursor()
    return db, cursor
db, cursor = conectDB()
dados = cursor.execute('SELECT * FROM produtos').fetchall()
"""


def main(page:ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    #page.window_maximized = True

    def _topContainer():
        topContainer = ft.Row(
            controls=[
                ft.Container(
                    width=335*0.32,
                    height= 600*0.20,
                    bgcolor = ft.colors.WHITE70,
                    border_radius= 20
                )
            ]
        )
        return topContainer

    def _bottomContainer():
        bottomContainer = ft.Container(
            width = 335* 0.45,
            height = 600*0.25,
            bgcolor = ft.colors.GREEN_100,
            border_radius= 20
        )
        return bottomContainer


    def _top():
        top = ft.Container(
            bgcolor = ft.colors.RED,
            border_radius = 20,
            width = 335,
            height = 600 * 0.35,
            padding = ft.padding.only(top=8, left=8, right=8),

            content = ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value = "Da Banda food",
                                size=20,
                                weight="bold",
                                color="white"
                            ),
                            ft.Row(
                                controls=[
                                    ft.Stack(
                                        controls=[
                                            ft.IconButton(
                                                icon=ft.icons.SHOPPING_CART,
                                                icon_size=25,
                                                icon_color=ft.colors.WHITE
                                            ),
                                            ft.Container(
                                                width=40,
                                                height= 20,
                                                content=ft.Container(
                                                    width=10,
                                                    height= 20,
                                                    alignment=ft.alignment.top_right,
                                                    #bgcolor=ft.colors.BLACK,
                                                    # border_radius=30,
                                                    content=ft.Text(
                                                        value="9+",
                                                        size= 13,
                                                        color = ft.colors.BLACK,
                                                        weight = 'bold',
                                                    )
                                                )
                                                
                                            )
                                        ]
                                    )
                                ]
                               
                            )
                        ],
                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row(
                        controls=[
                            _topContainer() for _ in range(4)
                        ],
                        spacing=3,
                        scroll="auto"
                    )
                ]
            )
        )
        return top

    def _bottom():
        bottom = ft.Container(
            width=335,
            height=600*0.98,
            padding = ft.padding.only(top=600*0.35, left=8, right=8),
            border_radius=20,
            bgcolor = ft.colors.WHITE,

            content=ft.Column(
                controls=[
                    ft.Tabs(
                        selected_index = 0,

                        tabs=[
                            ft.Tab(
                                text='Especial',
                                content=ft.Container(
                                    padding=ft.padding.only(top=10),
                                    content = ft.Row(
                                        controls=[_bottomContainer() for _ in range(4)],
                                        wrap=True
                                    )
                                )
                            ),#tab 1,

                            ft.Tab(
                                text='Hamburgers',
                                content=ft.Container(
                                    padding=ft.padding.only(top=10),
                                    content = ft.Row(
                                        controls=[_bottomContainer() for _ in range(4)],
                                        wrap=True
                                    )
                                )
                            ),#tab 1,
                            
                            ft.Tab(
                                text='Bebidas',
                                content=ft.Container(
                                    padding=ft.padding.only(top=10),
                                    content = ft.Row(
                                        controls=[_bottomContainer() for _ in range(4)],
                                        wrap=True
                                    )
                                )
                            ),#tab 1,
                            
                            ft.Tab(
                                text='Outros',
                                content=ft.Container(
                                    padding=ft.padding.only(top=10),
                                    content = ft.Row(
                                        controls=[_bottomContainer()],
                                        wrap=True
                                    )
                                )
                            ),#tab 1,
                        ],

                    ),
                ]
            )
        )
        return bottom

    main = ft.Container(
        width=350,
        height = 620,
        bgcolor = ft.colors.BLACK,
        border_radius = 20,
        content = ft.Column(
            controls = [
                ft.Container(
                    width = 335,
                    height = 600,
                    bgcolor = ft.colors.RED,
                    border_radius = 20,

                    #controles principais da aplicação
                    content = ft.Stack(
                        controls=[
                            _bottom(),
                            _top()
                        ]
                    )
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )
    page.add(
        main
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets')
