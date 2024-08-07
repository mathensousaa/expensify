import flet as ft


class SessionManager:
    _session_key = "user_session"

    @staticmethod
    def set_session(page: ft.Page, user_id, username):
        session_data = {"user_id": user_id, "username": username}
        page.storage.set(SessionManager._session_key, session_data)

    @staticmethod
    def get_session(page: ft.Page):
        return page.storage.get(SessionManager._session_key)

    @staticmethod
    def clear_session(page: ft.Page):
        page.storage.remove(SessionManager._session_key)
