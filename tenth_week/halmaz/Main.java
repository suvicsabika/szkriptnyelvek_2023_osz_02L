import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main
{
    public static void main(String[] args)
    {
        // Set<String> set = new HashSet<String>();//Meglehet adni a konstruktornak egy kollekciót
        // set.add("geza");
        // set.add("geza");
        // set.add("kek");
        // set.add("az");
        // set.add("eg");
        // set.add("eg");

        // System.out.println(set);
        // System.out.println(set.size());

        //Listából -> Halmaz
        Set<String> set = new HashSet<>(List.of("xx", "aa", "dd", "bb", "aa", "cc"));
        System.out.println(set);

        for (String e: set) {
            System.out.println(e);
        }

        System.out.println(set.contains("ee"));
        System.out.println(set.contains("xx"));

        set.remove("xx");

        System.out.println(set);

        //Halmazból -> Lista
        // List<String> vissza = new ArrayList<>(set);//Meglehet adni a konstruktornak egy kollekciót
        // System.out.println(vissza);
    }
}