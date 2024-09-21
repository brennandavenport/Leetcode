
/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        SimpleLinkedList<Integer> intList = new SimpleLinkedList<Integer>();
        
        intList.add(10);
        intList.add(20);
        intList.add(30);
        intList.add(40);
        intList.add(50);
        intList.add(60);

       

        // for(int i = 0; i < intList.size(); i++) {
        //     System.out.println("Element at: " + i + ", " + intList.get(i));
        // }

        // Suspicous bug program can only handle 7 bits
        intList.add(0, 100);
        intList.add(7, 90);
        intList.add(4, 11130);

        // System.out.println(intList.size());

        for(int i = 0; i < intList.size(); i++) {
            System.out.println("Element at: " + i + ", " + intList.get(i));
        }

        System.out.println(intList.indexOf(11130));
        
        intList.remove(8);
        intList.remove(5);
        intList.remove(0);
        intList.remove(0);
        intList.remove(0);
        intList.remove(0);
        intList.remove(0);
        intList.remove(0);
        intList.remove(0);


        for(int i = 0; i < intList.size(); i++) {
            System.out.println("Element at: " + i + ", " + intList.get(i));
        }
    
    }
}
