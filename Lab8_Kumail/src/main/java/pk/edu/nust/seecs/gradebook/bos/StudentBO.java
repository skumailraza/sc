package pk.edu.nust.seecs.gradebook.bos;

import pk.edu.nust.seecs.gradebook.dao.StudentDao;
import pk.edu.nust.seecs.gradebook.entity.Student;

/**
 * Created by skrk on 4/26/17.
 */
public class StudentBO {
    public StudentDao studentDao;
    public Student student;

    public StudentBO(){
        student = new Student();
        studentDao = new StudentDao();
    }
}

