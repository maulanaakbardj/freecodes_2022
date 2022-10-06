import java.util.Iterator;
import java.util.NoSuchElementException;



public class Deque<Item> implements Iterable<Item> {
    private Node<Item> first;    // beginning of queue
    private Node<Item> last;     // end of queue
    private int n;               // number of elements on queue

    // helper linked list class
    private static class Node<Item> 
    {
        private Item item;
        private Node<Item> prev;
        private Node<Item> next;
    }
    // construct an empty deque
    public Deque()
    {
        first = null;
        last  = null;
        n = 0;
    }
    
    // is the deque empty?
    public boolean isEmpty()
    {
        return n == 0;
    }
    
    // return the number of items on the deque
    public int size()
    {
        return n;
    }
    
    // add the item to the front
    public void addFirst(Item item)
    {
        if (item == null) throw  new IllegalArgumentException();
        Node<Item> oldfirst = first;
        first = new Node<Item>();
        first.item = item;
        first.next = oldfirst;
        first.prev = null;
        
        if (isEmpty()) last = first;
        else oldfirst.prev = first;
        n++;
    }
    
    // add the item to the back
    public void addLast(Item item)
    {
        if (item == null) throw  new IllegalArgumentException();
        Node<Item> oldlast = last;
        last = new Node<Item>();
        last.item = item;
        last.next = null;
        last.prev = oldlast;

        if (isEmpty()) first = last;
        else oldlast.next = last;
        n++; 
    }
   
    // remove and return the item from the front
    public Item removeFirst()
    {
        if (isEmpty()) throw new NoSuchElementException();
        Node<Item> oldfirst = first;
        Item item = first.item;
        first = first.next;
        oldfirst = null;
        n--;
        if (isEmpty()) last = null;   // to avoid loitering
        else first.prev = null;
        return item; 
    }
   
    // remove and return the item from the back
    public Item removeLast()
    {
        if (isEmpty()) throw new NoSuchElementException();
        Node<Item> oldlast = last;
        Item item = last.item;
        last = last.prev;
        oldlast = null;
        n--;
        if (isEmpty()) first = null;   // to avoid loitering
        else last.next = null;
        return item; 
    }
    
    // return an iterator over items in order from front to back
    public Iterator<Item> iterator()  {
        return new LinkedIterator();  
    }

    // an iterator, doesn't implement remove() since it's optional
    private class LinkedIterator implements Iterator<Item> 
    {
        private Node<Item> current;

        public LinkedIterator() {
            current = first;
        }

        public boolean hasNext()  { return current != null;                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next; 
            return item;
        }
    }
    // unit testing (required)
    public static void main(String[] args)
    {
    }

}
