import java.sql.*;
public class JDBC {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {

        String url = "jdbc:mysql://localhost:3306/book";
        String username = "root";
        String password = "root";
        Connection conn = DriverManager.getConnection(url, username, password);
        Statement st = conn.createStatement();
        ResultSet rs = st.executeQuery("SELECT * FROM student;");
        while (rs.next()) {
            String name = rs.getString("stuent_name");
            int id = rs.getInt("student_id");
            System.out.println("name = " + name + " id = " + id);
        }
        rs.close();
        st.close();
        conn.close();
    }
}
