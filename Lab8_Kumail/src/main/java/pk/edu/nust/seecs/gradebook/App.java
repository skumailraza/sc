package pk.edu.nust.seecs.gradebook;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import pk.edu.nust.seecs.gradebook.bos.CloBO;
import pk.edu.nust.seecs.gradebook.bos.CourseBO;
import pk.edu.nust.seecs.gradebook.bos.TeacherBO;
import pk.edu.nust.seecs.gradebook.dao.CloDao;
import pk.edu.nust.seecs.gradebook.entity.Clo;

/**
 * My main App. 
 * <p>
 This executes everything.
 */

public class App {

    public static void main(String[] args) {
        CloDao clodao = new CloDao();

//        // Add new clo
//        Clo clo = new Clo();
//        clo.setName("CLO 1");
//        clo.setDescription("Design efficient solutions for algorithmic problems");
//        clo.setPlo("2");
//        clodao.addClo(clo);
//
//        clodao.updateClo(clo);
//
//        // Delete an existing clo
//        //dao.deleteClo(1);
//
//        // Get all clos
//        for (Clo iter : clodao.getAllClos()) {
//            System.out.println(iter);
//        }

//        CloBO cloBO = new CloBO();
//        cloBO.clo.setName("CLO 1");
//        cloBO.clo.setDescription("Understand the design patterns for software construction.");
//        cloBO.clo.setBtLevel("C2");
//        cloBO.clo.setPlo("1");
//
//        clodao.addClo(cloBO.clo);
//
//        cloBO.clo.setName("CLO 2");
//        cloBO.clo.setDescription("Analyze various techniques to solve algorithmic and real world problems.");
//        cloBO.clo.setBtLevel("C4");
//        cloBO.clo.setPlo("2");
//
//        clodao.addClo(cloBO.clo);
//
//        cloBO.clo.setName("CLO 3");
//        cloBO.clo.setDescription("Develop applications and tools using various frameworks.");
//        cloBO.clo.setBtLevel("C6");
//        cloBO.clo.setPlo("3");
//
//        clodao.addClo(cloBO.clo);
//
//        cloBO.clo.setName("CLO 4");
//        cloBO.clo.setDescription("Understand and apply various code management tools and techniques.");
//        cloBO.clo.setBtLevel("C3");
//        cloBO.clo.setPlo("11");
//
//        clodao.addClo(cloBO.clo);

        CourseBO courseBO = new CourseBO();
        courseBO.course.setClasstitle("Software Construction");
        courseBO.course.setCreditHours(4);

        courseBO.courseDao.addCourse(courseBO.course);

        TeacherBO teacherBO = new TeacherBO();
        teacherBO.teacher.setName("Fahad Satti");

        teacherBO.teacherDao.addTeacher(teacherBO.teacher);
        // Get clo by id
        System.out.println(clodao.getCloById(1));

        
    }

}