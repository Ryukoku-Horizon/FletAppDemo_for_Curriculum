import flet as ft
import ToDoApp
import calculater
from urllib.parse import urlparse, parse_qs

def main(page: ft.Page):
    page.title = "Flet カリキュラム デモアプリ"

    parsed_url = urlparse(page.url)
    query_params = parse_qs(parsed_url.query)

    file_param = query_params.get("file", [None])[0]

    if file_param == "ToDoApp.py":
        ToDoApp.main(page)
        return
    elif file_param == "calculater.py":
        calculater.main(page)
        return

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def go_app(e):
        page.launch_url(f"?file={e.control.key}")

    page.add(
        ft.Text("Horizon Flet デモアプリ集", size=32, weight=ft.FontWeight.BOLD),
        ft.Text("さわってみたいアプリを選んでください", size=16, color=ft.Colors.GREY),
        ft.Container(height=20),

        ft.Button(
            content=ft.Text("📝 Todoアプリを開く"),
            width=250,
            height=50,
            key="ToDoApp.py",
            on_click=go_app
        ),
        
        ft.Container(height=10),

        ft.Button(
            content=ft.Text("🔢 電卓アプリを開く"),
            width=250,
            height=50,
            key="calculater.py",
            on_click=go_app
        ),
    )

if __name__ == "__main__":
    ft.run(main)