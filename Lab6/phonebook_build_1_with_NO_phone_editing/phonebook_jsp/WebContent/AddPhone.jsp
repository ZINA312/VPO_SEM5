<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="app.Person"%>
<%@ page import="app.Phonebook"%>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Добавление телефона</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        table {
            width: 70%;
            margin: auto;
            border-collapse: collapse;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        td, th {
            padding: 10px;
            border: 1px solid #ccc;
            text-align: left;
        }
        th {
            background-color: #5bc0de;
            color: white;
        }
        .center {
            text-align: center;
        }
        .error {
            color: red;
        }
        input[type="text"] {
            width: calc(100% - 22px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #5cb85c;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: #4cae4c;
        }
        a {
            margin-top: 10px;
            display: inline-block;
            color: #337ab7;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        @media (max-width: 600px) {
            table {
                width: 100%;
            }
            input[type="text"], input[type="submit"] {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <%
        String personId = request.getParameter("personId");
        Phonebook phonebook = Phonebook.getInstance();
        Person person = phonebook.getPerson(personId);
    %>

    <form action="<%=request.getContextPath()%>/ManagePhone" method="post" onsubmit="return validateForm()">
        <input type="hidden" name="personId" value="<%=request.getParameter("personId")%>"/>
        <table>
            <tr>
                <td colspan="2">Информация о телефоне владельца: <%=person.getSurname()%> <%=person.getName()%> <%=person.getMiddlename()%></td>
            </tr>
            <tr>
                <td><label for="phone">Номер:</label></td>
                <td><input type="text" name="phone" id="phone" required pattern="[\d+#-]{2,50}" title="Номер должен содержать от 2 до 50 символов: цифры, +, -, #" /></td>
            </tr>
            <tr>
                <td colspan="2" class="center">
                    <input type="submit" value="Добавить номер"/>
                    <br/>
                    <a href="<%=request.getContextPath()%>/phonebook_jsp/">Вернуться к списку</a>
                </td>
            </tr>
        </table>
    </form>

    <script>
        function validateForm() {
            const phoneInput = document.getElementById('phone');
            const pattern = /^[\d+#-]{2,50}$/; // Регулярное выражение для проверки

            if (!pattern.test(phoneInput.value)) {
                alert("Номер не соответствует формату!");
                return false; // Останавливаем отправку формы
            }
            return true; // Разрешаем отправку формы
        }
    </script>
</body>
</html>