/**
 * Created by Kumail on 3/29/17.
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Reader {

    public BufferedReader myBr;
    public Reader()
    {
        String csvFile = "/Users/skrk/Downloads/SoftwareConstructionLabs-master/Lab05/src/GeoLiteCity-Location.csv";
        String line = "";
        String cvsSplitBy = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            br.readLine();
            br.readLine();
            this.myBr = br;

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        String csvFile = "/Users/skrk/Downloads/SoftwareConstructionLabs-master/Lab05/src/GeoLiteCity-Location.csv";
        String line = "";
        String cvsSplitBy = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            br.readLine();
            br.readLine();
            while ((line = br.readLine()) != null) {

                String[] location = line.split(cvsSplitBy);
                System.out.println(location.length);
                Location l1 = new Location(location[0], location[1],location[3],location[5], location[6]);
                l1.print();


            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}