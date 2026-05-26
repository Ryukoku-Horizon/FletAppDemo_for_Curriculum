import flet as ft

def main(page: ft.Page):
    page.title = "Todoアプリ"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    todo_counter = 0
    new_task_input = ft.TextField(hint_text="やること(todo)を入力", width=300)
    todo_list_column = ft.Column(
        controls=[ft.Text("Nothing", size=20, color=ft.Colors.GREY)],
        spacing=10
    )
    edit_task_input = ft.TextField()
    current_editing_row = None

    def close_dlg(e):
        page.pop_dialog()
        page.update()

    def save_edit(e):
        nonlocal current_editing_row
        if current_editing_row and edit_task_input.value:
            text_control = current_editing_row.controls[0]
            text_control.value = f"・{edit_task_input.value}"
        close_dlg(e)

    dlg = ft.AlertDialog(
        title=ft.Text("Edit"),
        content=edit_task_input,
        actions=[
            ft.Row([
                ft.Button(content=ft.Text("変更"), on_click=save_edit),
                ft.Button(content=ft.Text("キャンセル"), on_click=close_dlg)
            ], alignment=ft.MainAxisAlignment.END)
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def delete_todo(e):
        target_key = e.control.key
        for row in todo_list_column.controls[:]: 
            if hasattr(row, 'key') and row.key == target_key:
                todo_list_column.controls.remove(row)
                break
        if len(todo_list_column.controls) == 0:
            todo_list_column.controls.append(ft.Text("Nothing", size=20, color=ft.Colors.GREY))
        page.update()

    def edit_todo(e):
        nonlocal current_editing_row
        target_key = e.control.key
        for row in todo_list_column.controls:
            if hasattr(row, 'key') and row.key == target_key:
                current_editing_row = row
                current_text = row.controls[0].value.lstrip("・")
                edit_task_input.value = current_text
                break
        page.show_dialog(dlg)
        page.update()

    def add_todo(e):
        nonlocal todo_counter
        task_text = new_task_input.value.strip()
        if not task_text:
            return
        if len(todo_list_column.controls) == 1 and isinstance(todo_list_column.controls[0], ft.Text) and todo_list_column.controls[0].value == "Nothing":
            todo_list_column.controls.clear()
        current_key = str(todo_counter)
        todo_counter += 1
        new_todo_row = ft.Row(
            key=current_key,
            controls=[
                ft.Text(f"・{task_text}", size=18, width=300),
                ft.IconButton(
                    icon=ft.Icons.EDIT,
                    key=current_key,
                    icon_color=ft.Colors.BLUE,
                    on_click=edit_todo
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                    key=current_key,
                    icon_color=ft.Colors.RED,
                    on_click=delete_todo
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        todo_list_column.controls.append(new_todo_row)
        new_task_input.value = ""
        page.update()

    input_row = ft.Row(
        controls=[
            new_task_input,
            ft.Button(content=ft.Text("追加"), on_click=add_todo)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Text("Todo App", size=40, weight=ft.FontWeight.BOLD),
        input_row,
        ft.Divider(),
        todo_list_column
    )

if __name__ == "__main__":
    ft.run(main)