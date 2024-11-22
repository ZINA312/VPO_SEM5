<%@ page import="app.Person"%>
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
    <title>Управление данными о человеке</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        table {
            width: 100%;
            max-width: 600px;
            margin: auto;
            border-collapse: collapse;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        td {
            padding: 10px;
            border: 1px solid #ccc;
        }
        .error {
            color: red;
        }
        .center {
            text-align: center;
        }
        .link-button {
            color: blue;
            text-decoration: underline;
            cursor: pointer;
        }
        input[type="text"] {
            width: calc(100% - 20px);
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
        }
        input[type="submit"]:hover {
            background-color: #4cae4c;
        }
        a {
            display: inline-block;
            margin-top: 10px;
        }
        @media (max-width: 600px) {
            table {
                width: 100%;
            }
            input[type="text"], input[type="submit"] {
                width: 100%;
            }
        }
        .phone-item {
		    display: flex;
		    align-items: center;
		    margin-bottom: 10px; /* Space between phone entries */
		}
		
		.phone-input {
		    flex: 1; /* Allow input to take remaining space */
		    margin-right: 10px; /* Space between input and buttons */
		}
		
		.phone-actions {
		    display: flex;
		    gap: 10px; /* Space between action buttons */
		}
    </style>
</head>
<body>

<%
    HashMap<String,String> jsp_parameters = new HashMap<String,String>();
    Person person = new Person();
    String error_message = "";

    if (request.getAttribute("jsp_parameters") != null) {
        jsp_parameters = (HashMap<String,String>)request.getAttribute("jsp_parameters");
    }

    if (request.getAttribute("person") != null) {
        person = (Person)request.getAttribute("person");
    }
    
    error_message = jsp_parameters.get("error_message");
%>

<form action="<%=request.getContextPath()%>/" method="post">
    <input type="hidden" name="id" value="<%=person.getId()%>"/>
    <table>
        <% if (error_message != null && !error_message.equals("")) { %>
            <tr>
                <td colspan="2" class="center"><span class="error"><%=error_message%></span></td>
            </tr>
        <% } %>
        <tr>
            <td colspan="2" class="center">Информация о человеке</td>
        </tr>
        <tr>
            <td>Фамилия:</td>
            <td><input type="text" name="surname" value="<%=person.getSurname()%>"/></td>
        </tr>
        <tr>
            <td>Имя:</td>
            <td><input type="text" name="name" value="<%=person.getName()%>"/></td>        
        </tr>
        <tr>
            <td>Отчество:</td>
            <td><input type="text" name="middlename" value="<%=person.getMiddlename()%>"/></td>
        </tr>
        
        <% if ("edit".equals(jsp_parameters.get("current_action"))) { %>
			<tr>
			    <td>Телефоны:</td>
			    <td>
			        <div id="phoneList">
			            <%
			                HashMap<String, String> phones = person.getPhones();
			                for (HashMap.Entry<String, String> entry : phones.entrySet()) {
			                    String id = entry.getKey();
			                    String value = entry.getValue();
			                    String editUrl = request.getContextPath() + "/EditPhone.jsp?phoneId=" + id + "&personId=" + person.getId();
			            %>
			                <div class="phone-item">
			                    <input type="text" name="phones" value="<%=value%>" readonly class="phone-input"/>
			                    <input type="hidden" name="phoneId" value="<%=id%>"/>
			                    <div class="phone-actions">
			                        <a href="<%=editUrl%>" class="link-button">Редактировать</a>
			                        <a href="#" onclick="markForDeletion(this)">Удалить</a>
			                    </div>
			                </div>
			            <%
			                }
			            %>
			        </div>
			        <a href="<%=request.getContextPath()%>/AddPhone.jsp?personId=<%=person.getId() %>" class="link-button">Добавить телефон</a>
			    </td>
			</tr>
        <% } %>
        
        <tr>
            <td colspan="2" class="center">
                <input type="submit" name="<%=jsp_parameters.get("next_action")%>" value="<%=jsp_parameters.get("next_action_label")%>" />
                <br/>
                <a href="<%=request.getContextPath()%>/phonebook_jsp/">Вернуться к списку</a>
            </td>
        </tr> 
    </table>
</form>

<script>
    let phonesToDelete = [];

    function markForDeletion(element) {
    	const phoneDiv = element.parentElement.parentElement;
        const phoneId = phoneDiv.querySelector('input[name="phoneId"]').value;
        
        if (!phonesToDelete.includes(phoneId)) {
            phonesToDelete.push(phoneId);
        }
        phoneDiv.parentElement.removeChild(phoneDiv);
    }

    document.querySelector('form').onsubmit = function() {
        const phonesInput = document.createElement('input');
        phonesInput.setAttribute('type', 'hidden');
        phonesInput.setAttribute('name', 'phonesToDelete'); // Name for your deletion array
        phonesInput.value = JSON.stringify(phonesToDelete); // Convert to JSON string
        this.appendChild(phonesInput);
    };
</script>

</body>
</html>