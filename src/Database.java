/**
 * Created by Kumail on 3/29/17.
 */

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Database {
    private static SessionFactory factory;
    public static void main(String arg[])
    {
        try{
            factory = new Configuration().configure().buildSessionFactory();
        }catch (Throwable ex) {
            System.err.println("Failed to create sessionFactory object." + ex);
            throw new ExceptionInInitializerError(ex);
        }
        System.out.println("This is a test");
        Database d = new Database();

      /* Add few employee records in database */
        String csvFile = "/Users/skrk/Downloads/SoftwareConstructionLabs-master/Lab05/src/GeoLiteCity-Location.csv";
        String line = "";
        String cvsSplitBy = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            br.readLine();
            br.readLine();
            while ((line = br.readLine()) != null) {

                String[] location = line.split(cvsSplitBy);
                System.out.println(location.length);
                d.addLocation(location[0], location[1],location[3],location[5], location[6]);



            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public Integer addLocation(String locId, String latitude, String longitude, String country, String city) {
        Session session = factory.openSession();
        Transaction tx = null;
        Integer employeeID = null;
        try {
            tx = session.beginTransaction();
            Location loc = new Location(locId, country,city,latitude,longitude);
            employeeID = (Integer) session.save(loc);
            tx.commit();
        } catch (HibernateException e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
        }
        return employeeID;
    }
}
