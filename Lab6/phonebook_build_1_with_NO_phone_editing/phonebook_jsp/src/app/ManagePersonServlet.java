package app;

import java.io.IOException;
import java.sql.SQLException;
import java.util.HashMap;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;


public class ManagePersonServlet extends HttpServlet {
	
	// Идентификатор для сериализации/десериализации.
	private static final long serialVersionUID = 1L;
	
	// Основной объект, хранящий данные телефонной книги.
	private Phonebook phonebook;
       
    public ManagePersonServlet()
    {
        // Вызов родительского конструктора.
    	super();
		
    	// Создание экземпляра телефонной книги.
        try
		{
			this.phonebook = Phonebook.getInstance();
		}
		catch (ClassNotFoundException e)
		{
			e.printStackTrace();
		}
		catch (SQLException e)
		{
			e.printStackTrace();
		}        
        
    }

    // Валидация ФИО и генерация сообщения об ошибке в случае невалидных данных.
    private String validatePersonFMLName(Person person)
    {
		String error_message = "";
		
		if (!person.validateFMLNamePart(person.getName(), false))
		{
			error_message += "Имя должно быть строкой от 1 до 150 символов из букв, цифр, знаков подчёркивания и знаков минус.<br />";
		}
		
		if (!person.validateFMLNamePart(person.getSurname(), false))
		{
			error_message += "Фамилия должна быть строкой от 1 до 150 символов из букв, цифр, знаков подчёркивания и знаков минус.<br />";
		}
		
		if (!person.validateFMLNamePart(person.getMiddlename(), true))
		{
			error_message += "Отчество должно быть строкой от 0 до 150 символов из букв, цифр, знаков подчёркивания и знаков минус.<br />";
		}
		
		return error_message;
    }
    
    // Реакция на GET-запросы.
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		
		response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // HTTP 1.1.
		response.setHeader("Pragma", "no-cache"); // HTTP 1.0.
		response.setHeader("Expires", "0");
		// Обязательно ДО обращения к любому параметру нужно переключиться в UTF-8,
		// иначе русский язык при передаче GET/POST-параметрами превращается в "кракозябры".
		request.setCharacterEncoding("UTF-8");
		
		// В JSP нам понадобится сама телефонная книга. Можно создать её экземпляр там,
		// но с архитектурной точки зрения логичнее создать его в сервлете и передать в JSP.
		request.setAttribute("phonebook", this.phonebook);
		
		// Хранилище параметров для передачи в JSP.
		HashMap<String,String> jsp_parameters = new HashMap<String,String>();

		// Диспетчеры для передачи управления на разные JSP (разные представления (view)).
		RequestDispatcher dispatcher_for_manager = request.getRequestDispatcher("/ManagePerson.jsp");
        RequestDispatcher dispatcher_for_list = request.getRequestDispatcher("/List.jsp");

		// Действие (action) и идентификатор записи (id) над которой выполняется это действие.
		String action = request.getParameter("action");
		String id = request.getParameter("id");
		
		// Если идентификатор и действие не указаны, мы находимся в состоянии
		// "просто показать список и больше ничего не делать".
        if ((action == null)&&(id == null))
        {
        	try {
				Phonebook phonebook = Phonebook.getInstance();
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	for (Person person : phonebook.getContents().values()) {
        		person.loadPhonesFromDatabase();
        	}
        	request.setAttribute("jsp_parameters", jsp_parameters);
            dispatcher_for_list.forward(request, response);
        }
        // Если же действие указано, то...
        else
        {
        	switch (action)
        	{
        		// Добавление записи.
        		case "add":
        			// Создание новой пустой записи о пользователе.
        			Person empty_person = new Person();
        			
        			// Подготовка параметров для JSP.
        			jsp_parameters.put("current_action", "add");
        			jsp_parameters.put("next_action", "add_go");
        			jsp_parameters.put("next_action_label", "Добавить");
        			
        			// Установка параметров JSP.
        			request.setAttribute("person", empty_person);
        			request.setAttribute("jsp_parameters", jsp_parameters);
        			
        			// Передача запроса в JSP.
        			dispatcher_for_manager.forward(request, response);
        		break;
			
        		// Редактирование записи.
        		case "edit":
        			// Извлечение из телефонной книги информации о редактируемой записи.        			
        			Person editable_person = this.phonebook.getPerson(id);
        			
        			editable_person.loadPhonesFromDatabase();
        			// Подготовка параметров для JSP.
        			jsp_parameters.put("current_action", "edit");
        			jsp_parameters.put("next_action", "edit_go");
        			jsp_parameters.put("next_action_label", "Сохранить");

        			// Установка параметров JSP.
        			request.setAttribute("person", editable_person);
        			request.setAttribute("jsp_parameters", jsp_parameters);
        			
        			// Передача запроса в JSP.
        			dispatcher_for_manager.forward(request, response);
        		break;
			
        		// Удаление записи.
        		case "delete":
        			
        			// Если запись удалось удалить...
        			if (phonebook.deletePerson(id))
        			{
        				jsp_parameters.put("current_action_result", "DELETION_SUCCESS");
        				jsp_parameters.put("current_action_result_label", "Удаление выполнено успешно");
        			}
        			// Если запись не удалось удалить (например, такой записи нет)...
        			else
        			{
        				jsp_parameters.put("current_action_result", "DELETION_FAILURE");
        				jsp_parameters.put("current_action_result_label", "Ошибка удаления (возможно, запись не найдена)");
        			}

        			// Установка параметров JSP.
        			request.setAttribute("jsp_parameters", jsp_parameters);
        			
        			// Передача запроса в JSP.
        			dispatcher_for_list.forward(request, response);
       			break;
       		}
        }
		
	}

	// Реакция на POST-запросы.
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	    request.setCharacterEncoding("UTF-8");
	    request.setAttribute("phonebook", this.phonebook);
	    HashMap<String, String> jsp_parameters = new HashMap<String, String>();
	    RequestDispatcher dispatcher_for_manager = request.getRequestDispatcher("/ManagePerson.jsp");
	    RequestDispatcher dispatcher_for_list = request.getRequestDispatcher("/List.jsp");

	    String add_go = request.getParameter("add_go");
	    String edit_go = request.getParameter("edit_go");
	    String id = request.getParameter("id");

	    // Добавление записи.
	    if (add_go != null) {
	        Person new_person = new Person(request.getParameter("name"), request.getParameter("surname"), request.getParameter("middlename"));
	        String error_message = this.validatePersonFMLName(new_person); 

	        if (error_message.equals("")) {
	            if (this.phonebook.addPerson(new_person)) {
	                jsp_parameters.put("current_action_result", "ADDITION_SUCCESS");
	                jsp_parameters.put("current_action_result_label", "Добавление выполнено успешно");
	            } else {
	                jsp_parameters.put("current_action_result", "ADDITION_FAILURE");
	                jsp_parameters.put("current_action_result_label", "Ошибка добавления");
	            }
	            request.setAttribute("jsp_parameters", jsp_parameters);
	            dispatcher_for_list.forward(request, response);
	        } else {
	            jsp_parameters.put("current_action", "add");
	            jsp_parameters.put("next_action", "add_go");
	            jsp_parameters.put("next_action_label", "Добавить");
	            jsp_parameters.put("error_message", error_message);
	            request.setAttribute("person", new_person);
	            request.setAttribute("jsp_parameters", jsp_parameters);
	            for(Person person : this.phonebook.getContents().values()) {
                	person.loadPhonesFromDatabase();
                }
	            dispatcher_for_manager.forward(request, response);
	        }
	    }

	    // Редактирование записи.
	    if (edit_go != null) {
	        String personId = request.getParameter("id");
	        Person updatable_person = this.phonebook.getPerson(personId); 
	        if (updatable_person != null) {
	            updatable_person.setName(request.getParameter("name"));
	            updatable_person.setSurname(request.getParameter("surname"));
	            updatable_person.setMiddlename(request.getParameter("middlename"));
	            updatable_person.loadPhonesFromDatabase();
	           
	            String[] phoneNumbers = request.getParameterValues("phonesToDelete");
	            HashMap<String, String> phonesMap = new HashMap<>();

	            if (phoneNumbers != null) {
	                for (String phone : phoneNumbers) {
	                    if (phone != null && !phone.trim().isEmpty()) {
	                        // Удаляем квадратные скобки и кавычки, затем разбиваем строку
	                        String cleanedPhones = phone.trim().replaceAll("[\\[\\]\"]", "");
	                        String[] individualPhones = cleanedPhones.split(",");

	                        for (String cleanedPhone : individualPhones) {
	                            cleanedPhone = cleanedPhone.trim(); // Удаляем пробелы
	                            if (!cleanedPhone.isEmpty()) {
	                                phonesMap.put(cleanedPhone, cleanedPhone);
	                            }
	                        }
	                    }
	                }
	            }

	            String error_message = this.validatePersonFMLName(updatable_person); 

	            if (error_message.equals("")) {
	                if (this.phonebook.updatePerson(personId, updatable_person)) {
	                    for (String deletePhone : phonesMap.keySet()) {
	                        if (updatable_person.getPhones().containsKey(deletePhone)) {
	                            this.phonebook.deletePhone(deletePhone);
	                        }
	                    }
	                    jsp_parameters.put("current_action_result", "UPDATE_SUCCESS");
	                    jsp_parameters.put("current_action_result_label", "Обновление выполнено успешно");
	                } else {
	                    jsp_parameters.put("current_action_result", "UPDATE_FAILURE");
	                    jsp_parameters.put("current_action_result_label", "Ошибка обновления");
	                }
	                
	                request.setAttribute("jsp_parameters", jsp_parameters);
	                for(Person person : this.phonebook.getContents().values()) {
	                	person.loadPhonesFromDatabase();
	                }
	                dispatcher_for_list.forward(request, response);
	            } else {
	                jsp_parameters.put("current_action", "edit");
	                jsp_parameters.put("next_action", "edit_go");
	                jsp_parameters.put("next_action_label", "Сохранить");
	                jsp_parameters.put("error_message", error_message);
	                request.setAttribute("person", updatable_person);
	                request.setAttribute("jsp_parameters", jsp_parameters);
	                dispatcher_for_manager.forward(request, response);
	            }
	        } else {
	            // Handle case where the person is not found
	            jsp_parameters.put("current_action_result", "UPDATE_FAILURE");
	            jsp_parameters.put("current_action_result_label", "Ошибка: запись не найдена");
	            request.setAttribute("jsp_parameters", jsp_parameters);
	            dispatcher_for_list.forward(request, response);
	        }
	    }
	}
}
