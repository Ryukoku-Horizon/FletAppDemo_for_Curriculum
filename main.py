import flet as ft
import ToDoApp
import calculater

def main(page: ft.Page):
    page.title = "Flet カリキュラム デモアプリ"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def go_todo(e):
        page.controls.clear()
        ToDoApp.main(page)
        page.update()

    def go_calc(e):
        page.controls.clear()
        calculater.main(page)
        page.update()

    page.add(
        ft.Text("Horizon Flet デモアプリ集", size=32, weight=ft.FontWeight.BOLD),
        ft.Text("さわってみたいアプリを選んでください", size=16, color=ft.Colors.GREY),
        ft.Container(height=20),
        
        ft.Button(
            content=ft.Text("📝 Todoアプリを開く"),
            width=250,
            height=50,
            on_click=go_todo
        ),
        
        ft.Container(height=10),
        
        ft.Button(
            content="🔢 電卓アプリを開く",
            width=250,
            height=50,
            on_click=go_calc
        ),
    )

if __name__ == "__main__":
    ft.run(main)