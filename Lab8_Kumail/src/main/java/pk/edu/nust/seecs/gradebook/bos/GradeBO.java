package pk.edu.nust.seecs.gradebook.bos;

import pk.edu.nust.seecs.gradebook.dao.GradeDao;
import pk.edu.nust.seecs.gradebook.entity.Grade;

/**
 * Created by skrk on 4/26/17.
 */
public class GradeBO {
    public GradeDao gradeDao;
    public Grade grade;

    public GradeBO(){
        grade = new Grade();
        gradeDao = new GradeDao();
    }
}
