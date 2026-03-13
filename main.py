import flet as ft
import os

def main(page: ft.Page):
    page.title = "Aseel Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Container(
            content=ft.Text("Welcome to Aseel Messenger!", size=30, weight="bold", color="blue"),
            alignment=ft.alignment.center
        )
    )

if __name__ == "__main__":
    # ربط المنفذ بالسيرفر بشكل صحيح للويب
    app_port = int(os.getenv("PORT", 8080))
    ft.app(target=main, view=None, port=app_port, host="0.0.0.0")
