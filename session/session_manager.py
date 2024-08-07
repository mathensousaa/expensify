import flet as ft


class SessionManager:
    _session_key = "user_session"

    @staticmethod
    def set_session(page: ft.Page, user_id, username):
        session_data = {"user_id": user_id, "username": username}
        page.client_storage.set(SessionManager._session_key, session_data)

    @staticmethod
    def get_session(page: ft.Page):
        return page.client_storage.get(SessionManager._session_key)

    @staticmethod
    def clear_session(page: ft.Page):
        page.client_storage.remove(SessionManager._session_key)
