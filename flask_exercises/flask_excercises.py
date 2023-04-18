from typing import Dict

from flask import Flask, request, jsonify, Response


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users: Dict[str, Dict] = {}

        @app.post("/user")
        def create_user() -> tuple[Response, int]:
            request_data = request.get_json()
            if "name" not in request_data:
                response_value = {"name": "This field is required"}
                return jsonify(errors=response_value), 422

            user_name = request_data["name"]
            users[user_name] = {}
            return jsonify(data=f"User {user_name} is created!"), 201

        @app.get("/user/<name>")
        def show_user(name: str) -> tuple[Response, int]:
            if name in users:
                response = jsonify(data=f"My name is {name}"), 200
            else:
                response = jsonify(""), 404
            return response

        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name: str) -> tuple[Response, int]:
            new_data = request.get_json()
            new_name = new_data["name"]
            if name in users:
                user_data = users.pop(name)
                users[new_name] = user_data
                return jsonify(data=f"My name is {new_name}"), 200
            else:
                return jsonify(""), 404

        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name: str) -> tuple[str, int]:
            if name in users:
                del users[name]
                return "", 204
            else:
                return "", 404
