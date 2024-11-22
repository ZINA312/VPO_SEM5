<%@ page import="app.Person"%>
<%@ page import="app.Phonebook"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Редактирование телефона</title>
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
    String phoneId = request.getParameter("phoneId");
    
    Phonebook phonebook = Phonebook.getInstance();
    Person person = phonebook.getPerson(personId);
    String phoneNumber = phonebook.getPhoneNumberById(phoneId);
%>

<form action="<%=request.getContextPath()%>/ManagePhone" method="post">
    <input type="hidden" name="personId" value="<%=personId%>"/>
    <input type="hidden" name="phoneId" value="<%=phoneId%>"/>
    
    <table>
        <tr>
            <td colspan="2">Информация о телефоне владельца: <%=person.getSurname()%> <%=person.getName()%> <%=person.getMiddlename()%></td>
        </tr>
        <tr>
            <td><label for="phone">Номер:</label></td>
            <td><input type="text" name="phone" id="phone" value="<%=phoneNumber%>" required pattern="[\d+#-]{2,50}" title="Номер должен содержать от 2 до 50 символов: цифры, +, -, #" /></td>
        </tr>
        <tr>
            <td colspan="2" class="center">
                <input type="submit" value="Сохранить"/>
                <br/>
                <a href="<%=request.getContextPath()%>/phonebook_jsp/?action=edit&id=<%=personId%>">Вернуться к данным о человеке</a>
            </td>
        </tr>
    </table>
</form>

</body>
</html>