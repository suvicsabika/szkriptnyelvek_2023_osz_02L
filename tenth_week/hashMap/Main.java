import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class Main
{
    public static void main(String[] args)
    {
        Map<String, String> map = new HashMap<String, String>();
        map.put("a", "alfa");
        map.put("b", "beta");
        map.put("g", "gamma");
        map.put("d", "delta");

        String value = map.get("x");//Ha nincs benne a kulcs NULL értéket ad vissza
        if (value != null) {
            System.out.println(value.toUpperCase());
        }

        String value2 = map.getOrDefault("x", "");
        System.out.println(value2);

        System.out.println(map.containsKey("d"));
        System.out.println(map.containsKey("X"));

        System.out.println(map.containsValue("delta"));
        System.out.println(map.containsValue("sigma"));

        map.put("a", "ALFA");
        map.replace("b", "beta", "BETA");
        System.out.println(map);

        for (String k : map.keySet()) {
            System.out.println(k);
        }

        for (String v : map.values()) {
            System.out.println(v);
        }

        for (Entry e : map.entrySet())
        {
            System.out.printf("%s -> %s\n", e.getKey(), e.getValue());
        }

        map.remove("a");
        System.out.println(map);

	System.out.println(map.size());
    }
}