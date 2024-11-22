package app;

import java.io.IOException;
import java.sql.SQLException;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/ManagePhone")
public class ManagePhoneServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");
        response.setHeader("Pragma", "no-cache");
        response.setHeader("Expires", "0");

        String personId = request.getParameter("personId");
        String newPhone = request.getParameter("phone");

        Phonebook phonebook = null;
        try {
            phonebook = Phonebook.getInstance();
            if (newPhone != null && !newPhone.trim().isEmpty()) {
                boolean addSuccess = phonebook.addPhone(personId, newPhone.trim());
                if (addSuccess) {
                    response.sendRedirect(request.getContextPath() + "/?action=edit&id=" + personId + "&addedPhone=" + newPhone);
                } else {
                    request.setAttribute("errorMessage", "Ошибка добавления номера телефона");
                    request.getRequestDispatcher("/AddPhone.jsp").forward(request, response);
                }
            } else {
                request.setAttribute("errorMessage", "Номер телефона не может быть пустым");
                request.getRequestDispatcher("/AddPhone.jsp").forward(request, response);
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
            request.setAttribute("errorMessage", "Ошибка сервера");
            request.getRequestDispatcher("/AddPhone.jsp").forward(request, response);
        }
    }
}