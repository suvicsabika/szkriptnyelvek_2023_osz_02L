import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class Main
{
    // public static void main(String[] args)
    // {
    //     try
    //     {
    //         String line;
    //         BufferedReader br = new BufferedReader(new FileReader("szoveg.txt"));
    //         while ((line = br.readLine()) != null)
    //         {
    //             System.out.println(line);
    //         }
    //         br.close();
    //     }
    //     catch (FileNotFoundException e) {
    //         //e.printStackTrace();
    //         System.err.println("Hiba: nem talalhato az input fajl.");
    //     }
    //     catch (IOException e) {
    //         e.printStackTrace();
    //     }

    //     System.out.println("OK");
    // }
    public static void main(String[] args)
    {
        try
        {
            PrintWriter writer = new PrintWriter("output.txt", "utf-8");
            writer.println("The first line.");
            writer.println("The second line.");
            writer.close();
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }
}
