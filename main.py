import flet as ft
import ToDoApp
import calculater

def main(page: ft.Page):
    page.title = "Flet カリキュラム デモアプリ"

    def route_change(e):
        page.controls.clear()

        current_route = page.route if page.route else "/"

        if current_route == "/todo":
            ToDoApp.main(page)
        elif current_route == "/calc":
            calculater.main(page)
        else:
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            page.add(
                ft.Text("Horizon Flet デモアプリ集", size=32, weight=ft.FontWeight.BOLD),
                ft.Text("さわってみたいアプリを選んでください", size=16, color=ft.Colors.GREY),
                ft.Container(height=20),

                ft.Button(
                    content=ft.Text("📝 Todoアプリを開く"),
                    width=250,
                    height=50,
                    on_click=lambda _: page.push_route("/todo")
                ),
                
                ft.Container(height=10),

                ft.Button(
                    content=ft.Text("🔢 電卓アプリを開く"),
                    width=250,
                    height=50,
                    on_click=lambda _: page.push_route("/calc")
                ),
            )
        page.update()

    page.on_route_change = route_change
    initial_route = page.route if page.route else "/"
    page.push_route(initial_route)

if __name__ == "__main__":
    ft.run(main)