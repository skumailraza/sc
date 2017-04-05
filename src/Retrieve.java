/**
 * Created by skrk on 4/4/17.
 */

import org.hibernate.*;
import org.hibernate.cfg.Configuration;
import org.hibernate.mapping.List;

import java.util.Iterator;
import java.util.Scanner;

public class Retrieve {
    public static void main(String args[]) {
        Configuration cfg = new Configuration();
        cfg.configure("hibernate.cfg.xml");// populates the data of the
        // configuration file
        GreatCircle greatCircle = new GreatCircle();
//        // creating seession factory object
        SessionFactory factory = cfg.buildSessionFactory();
//
//        // creating session object
//        Session session = factory.openSession();
//
//        // creating transaction object
//        Transaction t = session.beginTransaction();

        Session session = factory.openSession();
        Transaction tx = null;
        Transaction tx1 = null;
//        try{
//            tx = session.beginTransaction();
//            java.util.List locations = session.createQuery("FROM Location").list();
//            for (Iterator iterator = locations.iterator(); iterator.hasNext();){
//                Location loc = (Location) iterator.next();
//                loc.print();
//
//            }
//            tx.commit();
//        }catch (HibernateException e) {
//            if (tx!=null) tx.rollback();
//            e.printStackTrace();
//        }finally {
//            session.close();
//        }

        System.out.println("****************\nMENU\n*************\n\n1)Search City?\n2)Nearby Cities by City?\n3)Nearby City by Lat/Lon?\n4)Exit\n");
        Scanner scanner = new Scanner (System.in);
        String input = scanner.next();


        switch (input){
            case "1":
            {
                System.out.println("\nEnter City Name: ");
                String city = scanner.next();
                Query hql = session.createQuery("FROM Location WHERE city = :city");
                hql.setParameter("city", city);
                try{
                    tx = session.beginTransaction();
                    java.util.List locations = hql.list();
                    for (Iterator iterator = locations.iterator(); iterator.hasNext();){
                        Location loc = (Location) iterator.next();
                        loc.print();

                    }
                    //tx.commit();
                }catch (HibernateException e) {
                    if (tx!=null) tx.rollback();
                    e.printStackTrace();
                }finally {
                    session.close();
                    break;
                }

            }
            case "2":
            {
                System.out.println("Enter City?");
                //System.out.println("\nEnter Lat: ");
                String city = scanner.next();
                Query hql = session.createQuery("FROM Location WHERE city = :city");
                hql.setParameter("city", city);
                Location loc1;
                Location loc2;
                int x = 0;
                try{
                    tx = session.beginTransaction();
                    java.util.List locations = hql.list();
                    for (Iterator iterator = locations.iterator(); iterator.hasNext();){
                        loc1 = (Location) iterator.next();
                        Query hql1 = session.createQuery("from Location where country =:country");
                        hql1.setParameter("country", loc1.getCountry());
                        java.util.List<Location> locations1 = hql1.list();
                        for (Iterator iterator1 = locations1.iterator(); iterator1.hasNext();){
                            loc2 = (Location) iterator1.next();

                            double distance = greatCircle.getDistance(Double.parseDouble(loc1.getLatitude()),
                                    Double.parseDouble(loc2.getLatitude()),
                                    Double.parseDouble(loc1.getLongitude()),
                                    Double.parseDouble(loc2.getLongitude()));
                            System.out.println("\n" + distance);

                                if(distance <= 10000) {    //if the distance between them is less than 120 miles
                                    loc2.print();
                                    System.out.println();
                                    x+=1;
                                }
                                if(x == 5)
                                    break;
                                //tx1.commit();
                            }


                        }
                    //tx.commit();
                }catch (HibernateException e) {
                    if (tx!=null) tx.rollback();
                    e.printStackTrace();
                }finally {
                    session.close();
                }
                break;
            }
            case "3":
            {
                System.out.println("Enter Lat/Lon?");
                String city = scanner.next();
                city = "Islamabad";
                Query hql = session.createQuery("FROM Location WHERE city = :city");
                hql.setParameter("city", city);
                Location loc1;
                Location loc2;
                int x = 0;
                try{
                    //tx = session.beginTransaction();
                    java.util.List locations = hql.list();
                    for (Iterator iterator = locations.iterator(); iterator.hasNext();){
                        loc1 = (Location) iterator.next();
                        Query hql1 = session.createQuery("from Location where country =:country");
                        hql1.setParameter("country", loc1.getCountry());
                        java.util.List locations1 = hql1.list();
                        for (Iterator iterator1 = locations1.iterator(); iterator1.hasNext();){
                            loc2 = (Location) iterator1.next();
                            double distance = greatCircle.getDistance(Double.parseDouble(loc1.getLatitude()),
                                    Double.parseDouble(loc2.getLatitude()),
                                    Double.parseDouble(loc1.getLongitude()),
                                    Double.parseDouble(loc2.getLongitude()));
                            if(distance <= 10000) {
                                loc2.print();
                                System.out.println();
                                x+=1;
                            }
                            if(x == 5)
                                break;
                        }


                    }
                    //tx.commit();
                }catch (HibernateException e) {
                    if (tx!=null) tx.rollback();
                    e.printStackTrace();
                }finally {
                    session.close();
                }
                break;
            }
            default:
                session.close();

        }


//
//        Query query = session.createQuery("from Location");
//        java.util.List list = query.list();
//        System.out.println(list);
//        t.commit();
//        session.close();
    }
}