import flet as ft

def main(page: ft.Page):
    page.title = "Flet カリキュラム デモアプリ"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def go_app(e):
        app_file = e.control.key
        page.launch_url(f"?file={app_file}", web_window_name="_self")

    page.add(
        ft.Text("Horizon Flet デモアプリ集", size=32, weight=ft.FontWeight.BOLD),
        ft.Text("さわってみたいアプリを選んでください", size=16, color=ft.Colors.GREY),
        ft.VerticalDivider(height=20),

        ft.ElevatedButton(
            text="📝 Todoアプリを開く",
            width=250,
            height=50,
            key="ToDoApp.py",
            on_click=go_app
        ),
        ft.VerticalDivider(height=10),
        ft.ElevatedButton(
            text="🔢 電卓アプリを開く",
            width=250,
            height=50,
            key="calculater.py",
            on_click=go_app
        ),
    )

ft.run(main)