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

        System.out.println("****************\nMENU\n*************\n\n1)Search City?\n2)Nearby Cities by City?\n3)Nearby City by Lat/Lon?\n4)Distance between Cities\n5)Exit\n");
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
                System.out.println("Enter City? ");
                //System.out.println("\nEnter Lat: ");
                String city = scanner.next();
                System.out.println("Number of nearby cities? ");
                Scanner intScanner = new Scanner(System.in);
                int limit = intScanner.nextInt();
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
                                    Double.parseDouble(loc1.getLongitude()),
                                    Double.parseDouble(loc2.getLatitude()),
                                    Double.parseDouble(loc2.getLongitude()));
                            System.out.println("\n" + distance);

                                if(distance <= 1000) {    //if the distance between them is less than 1000 miles
                                    loc2.print();
                                    System.out.println();
                                    x+=1;
                                }
                                if(x == limit)
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
                                    Double.parseDouble(loc1.getLongitude()),
                                    Double.parseDouble(loc2.getLatitude()),
                                    Double.parseDouble(loc2.getLongitude()));
                            if(distance <= 1000) {
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
            case "4":
                System.out.println("Enter City 1?");
                String city1 = scanner.next();
                System.out.println("Enter City 2");
                String city2 = scanner.next();

                Query hql1 = session.createQuery("FROM Location WHERE city = :city1");
                Query hql2 = session.createQuery("FROM Location where city = :city2");
                hql1.setParameter("city1", city1);
                hql2.setParameter("city2", city2);

                Location loc1 = null;
                Location loc2 = null;

                int x = 0;
                try{
                    //tx = session.beginTransaction();
                    java.util.List locations1 = hql1.list();
                    java.util.List locations2 = hql2.list();
                    for (Iterator iterator = locations1.iterator(); iterator.hasNext();) {
                        loc1 = (Location) iterator.next();
//                        Query hql1 = session.createQuery("from Location where country =:country");
//                        hql1.setParameter("country", loc1.getCountry());
//                        java.util.List locations1 = hql1.list();
                    }
                    for (Iterator iterator1 = locations2.iterator(); iterator1.hasNext();){
                            loc2 = (Location) iterator1.next();
                    }
                    double distance = greatCircle.getDistance(Double.parseDouble(loc1.getLatitude()),
                            Double.parseDouble(loc1.getLongitude()),
                            Double.parseDouble(loc2.getLatitude()),
                            Double.parseDouble(loc2.getLongitude()));
                    System.out.println("Distance b/w " + loc1.getCity() + " and " + loc2.getCity() + " is: "+ distance);
                }catch (HibernateException e) {
                    if (tx!=null) tx.rollback();
                    e.printStackTrace();
                }finally {
                    session.close();
                }
                break;

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