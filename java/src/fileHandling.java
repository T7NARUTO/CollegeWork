import java.io.*;

public class fileHandling {
    public static void main(String[] args){
        /* File creation
        try{
            File file = new File("file.txt");
            if (file.createNewFile()){
                System.out.println("File created successfully");
            }
            else{
                System.out.println("File exists");
            }
        }
        catch (IOException e) {
            e.printStackTrace();;
        }
        */
        /* File writing
        try{
            FileWriter fw = new FileWriter("file.txt");
            String line = "new line";
            fw.write(line);
            System.out.println("successfully created");
            fw.close();
        }catch (IOException e) {
            e.printStackTrace();
        }
        */
        try {
            BufferedReader fr = new BufferedReader(new FileReader("file.txt"));
            String line = fr.readLine();
            System.out.println(line);
            fr.close();
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
}