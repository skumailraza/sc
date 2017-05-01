package pk.edu.nust.seecs.gradebook.bos;

import pk.edu.nust.seecs.gradebook.dao.CourseDao;
import pk.edu.nust.seecs.gradebook.entity.Course;

/**
 * Created by skrk on 4/26/17.
 */
public class CourseBO {
    public CourseDao courseDao;
    public Course course;

    public CourseBO(){
        courseDao = new CourseDao();
        course = new Course();
    }
}
