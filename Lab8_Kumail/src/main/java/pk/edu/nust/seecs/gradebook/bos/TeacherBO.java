package pk.edu.nust.seecs.gradebook.bos;

import pk.edu.nust.seecs.gradebook.dao.TeacherDao;
import pk.edu.nust.seecs.gradebook.entity.Teacher;

/**
 * Created by skrk on 4/26/17.
 */
public class TeacherBO {
    public TeacherDao teacherDao;
    public Teacher teacher;


    public TeacherBO(){
        teacher = new Teacher();
        teacherDao = new TeacherDao();
    }
}
