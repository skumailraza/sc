/**
 * Created by Kumail on 4/4/17.
 */
public class GreatCircle {
    public double getDistance(double x1, double y1, double x2, double y2) {
//        double x1 = Math.toRadians(Double.parseDouble(args[0]));
//        double y1 = Math.toRadians(Double.parseDouble(args[1]));
//        double x2 = Math.toRadians(Double.parseDouble(args[2]));
//        double y2 = Math.toRadians(Double.parseDouble(args[3]));

        /*************************************************************************
         * Compute using law of cosines
         *************************************************************************/
        // great circle distance in radians
        double angle1 = Math.acos(Math.sin(x1) * Math.sin(x2)
                + Math.cos(x1) * Math.cos(x2) * Math.cos(y1 - y2));

        // convert back to degrees
        angle1 = Math.toDegrees(angle1);

        // each degree on a great circle of Earth is 60 nautical miles
        double distance1 = 60 * angle1;
        return distance1;
        //System.out.println(distance1 + " nautical miles");

    }
}