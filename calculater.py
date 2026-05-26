import flet as ft

def main(page: ft.Page):
    result = ft.Text("")

    def num_click(e):
        btn_text = e.control.content.value
        if btn_text == "C":
            result.value = ""
        elif btn_text == "BS":
            result.value = str(result.value)[:-1]
        elif btn_text == "税込":
            if result.value:
                try:
                    current_val = float(eval(result.value))
                    result.value = str(current_val * 1.1)
                except:
                    result.value = "Error"
        elif btn_text == "=":
            if result.value:
                try:
                    result.value = str(eval(result.value))
                except:
                    result.value = "Error"
        else:
            result.value = str(result.value) + btn_text            
        result.update()

    def create_btn(text):
        return ft.CupertinoFilledButton(
            height=60,
            width=60,
            padding=0,
            content=ft.Text(text),
            on_click=num_click
        )

    button_layout = [
        ["C", "税込", "BS", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", "00", ".", "="]
    ]

    calc_column = ft.Column(
        controls=[
            ft.Row(controls=[create_btn(btn) for btn in row])
            for row in button_layout
        ]
    )

    page.add(result, calc_column)

ft.run(main)