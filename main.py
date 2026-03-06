import flet as ft
import os

def main(page: ft.Page):
    page.title = "Aseel Messenger"
    page.add(ft.Text("Welcome to Aseel Messenger!"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    ft.app(target=main, view=None, port=port)
