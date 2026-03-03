import flet as ft
import os
def main(page: ft.Page):
    page.title = "أصيل ميسنجر"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # قائمة الرسائل
    chat_list = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    # وظيفة استقبال الرسائل عبر البث (PubSub)
    def on_broadcast(data):
        if "text" in data:
            chat_list.controls.append(
                ft.Text(f"{data['user']}: {data['text']}", size=16)
            )
            page.update()
    page.pubsub.subscribe(on_broadcast)
    # حقل إدخال الرسالة
    msg_input = ft.TextField(hint_text="اكتب رسالتك هنا يا أصيل...", expand=True)
    # وظيفة زر الإرسال
    def send_click(e):
        if msg_input.value:
            user_name = page.session.get("u") or "مستخدم جديد"
            page.pubsub.send_all({"user": user_name, "text": msg_input.value})
            msg_input.value = ""
            page.update()
    # واجهة التطبيق
    page.add(
        ft.Column(
            [
                ft.Text("مرحباً بك في أصيل ميسنجر", size=20, weight="bold"),
                chat_list,
                ft.Row([msg_input, ft.ElevatedButton("إرسال", on_click=send_click)]),
            ],
            expand=True,
        )
    )
if __name__ == "__main__":
    # تشغيل كنسخة ويب متوافقة مع سيرفر Render والمنفذ 8000
    # تم إلغاء flet_desktop ليعمل السيرفر بنجاح
    port = int(os.environ.get("PORT", 8000))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port)
