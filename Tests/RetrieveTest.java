import org.hibernate.*;
import org.hibernate.cfg.Configuration;
import org.hibernate.validator.AssertTrue;
import org.junit.Test;

import java.util.Iterator;

import static org.junit.Assert.*;

/**
 * Created by skrk on 4/5/17.
 */
public class RetrieveTest {
    @Test
    public void main() throws Exception {
        Configuration cfg = new Configuration();
        cfg.configure("hibernate.cfg.xml");// populates the data of the
        // configuration file
        GreatCircle greatCircle = new GreatCircle();
//        // creating seession factory object
        SessionFactory factory = cfg.buildSessionFactory();


        Session session = factory.openSession();
        Transaction tx = null;
        Transaction tx1 = null;

        String city = "Islamabad";
        Query hql = session.createQuery("FROM Location WHERE city = :city");
        hql.setParameter("city", city);
            tx = session.beginTransaction();
            java.util.List locations = hql.list();
            for (Iterator iterator = locations.iterator(); iterator.hasNext();){
                Location loc = (Location) iterator.next();
                loc.print();

            }
            tx.commit();
            session.close();


    }

}