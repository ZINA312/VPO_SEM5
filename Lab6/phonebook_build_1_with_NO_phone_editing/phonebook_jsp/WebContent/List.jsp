<?xml version="1.0" encoding="UTF-8" ?>
<%@ page import="app.Phonebook"%>
<%@ page import="app.Person"%>
<%@ page import="java.util.ArrayList"%>
<%@ page import="java.util.HashMap"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
   response.setHeader( "Pragma", "no-cache" );
   response.setHeader( "Cache-Control", "no-cache" );
   response.setDateHeader( "Expires", 0 );
%>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список людей</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        table {
            width: 90%;
            margin: auto;
            border-collapse: collapse;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        th, td {
            padding: 10px;
            border: 1px solid #ccc;
            text-align: center;
        }
        th {
            background-color: #5bc0de;
            color: white;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        a {
            color: #337ab7;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .message {
            color: green;
            font-weight: bold;
        }
        .add-button {
            text-align: center;
            padding: 10px;
        }
        .add-button a {
            background-color: #5cb85c;
            color: white;
            padding: 10px 15px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .add-button a:hover {
            background-color: #4cae4c;
        }
        @media (max-width: 600px) {
            table {
                width: 100%;
            }
            th, td {
                font-size: 14px;
            }
        }
        .add-button {
    		height: 60px; /* Задаем высоту строки */
		}
		
		.button-container {
		    display: flex;
		    justify-content: center; /* Центрируем по горизонтали */
		    align-items: center; /* Центрируем по вертикали */
		    height: 100%; /* Занимаем всю высоту строки */
		}
    </style>
</head>
<body>

<%
    String user_message = "";
    HashMap<String,String> jsp_parameters = new HashMap<String,String>();
    Phonebook phonebook = (Phonebook)request.getAttribute("phonebook");
    
    if (request.getAttribute("jsp_parameters") != null) {
        jsp_parameters = (HashMap<String,String>)request.getAttribute("jsp_parameters");
    }
    
    user_message = jsp_parameters.get("current_action_result_label");
%>

<table>
    <%
    if ((user_message != null) && (!user_message.equals(""))) {
    %>
    <tr>
        <td colspan="6" class="message"><%=user_message%></td>
    </tr>
    <%
    }
    %>
    
    <tr class="add-button">
    <td colspan="6">
        <div class="button-container">
            <a href="<%=request.getContextPath()%>/?action=add">Добавить запись</a>
        </div>
    </td>
</tr>
    <tr>
        <th>Фамилия</th>
        <th>Имя</th>
        <th>Отчество</th>
        <th>Телефон(ы)</th>
        <th>&nbsp;</th>
        <th>&nbsp;</th>
    </tr>
    
    <%
    for (Person person : phonebook.getContents().values()) {
    %>
    <tr>
        <td><%=person.getSurname()%></td>
        <td><%=person.getName()%></td>
        <td><%=person.getMiddlename()%></td>
        <td>
            <%
            for(String phone : person.getPhones().values()) {
            %>
            <%=phone%><br />
            <%
            }
            %>
        </td>
        <td><a href="<%=request.getContextPath()%>/?action=edit&id=<%=person.getId()%>">Редактировать</a></td>
        <td><a href="<%=request.getContextPath()%>/?action=delete&id=<%=person.getId()%>">Удалить</a></td>
    </tr>
    <%
    }
    %>
</table>

</body>
</html>