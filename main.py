import flet as ft
import os

def main(page: ft.Page):
    page.title = "Aseel Messenger"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text("Welcome to Aseel Messenger!", size=30, weight="bold"))

if __name__ == "__main__":
    # هذا السطر هو مفتاح الحل لربط السيرفر
    app_port = int(os.getenv("PORT", 8080))
    ft.app(target=main, view=None, port=app_port, host="0.0.0.0")
