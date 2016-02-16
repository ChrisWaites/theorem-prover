import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.NoSuchElementException;
import java.util.Queue;
/**
 * Created by ChrisWaites on 2/15/2016.
 */
public class UniqueQueue<T> {
    LinkedHashSet<T> backing;
    public UniqueQueue() {
        backing = new LinkedHashSet<>();
    }
    public boolean add(T element) {
        return backing.add(element);
    }
    public T element() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        return backing.iterator().next();
    }
    public boolean offer(T element) {
        return backing.add(element);
    }
    public T peek() {
        if (isEmpty()) {
            return null;
        }
        return backing.iterator().next();
    }
    public T poll() {
        if (isEmpty()) {
            return null;
        }
        Iterator<T> iter = backing.iterator();
        T next = iter.next();
        iter.remove();
        return next;
    }
    public T remove() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Iterator<T> iter = backing.iterator();
        T next = iter.next();
        iter.remove();
        return next;
    }
    public boolean isEmpty() {
        return backing.isEmpty();
    }
    public void clear() {
        backing = new LinkedHashSet<>();
    }
}
