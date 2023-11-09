import java.util.Set;
import java.util.HashSet;
import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        Set<String> a = new HashSet<String>(List.of("alma", "banan", "citrom"));
        Set<String> b = new HashSet<String>(List.of("banan", "narancs"));

        //Unió, ez módosítja a-t
        // a.addAll(b);
        // System.out.println(a);

        // //Metszet, retain = "megtart", ez is módosítja a-t
        // a.retainAll(b);
        // System.out.println(a);

        // //Különbség, ez is módosítja a-t
        // a.removeAll(b);
        // System.out.println(b);

        System.out.println(a);
        System.out.println(b);
        Set<String> unio = new HashSet<String>(a);
        unio.addAll(b);
        System.out.println(unio);
        System.out.println(a);
    }
}