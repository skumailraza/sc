package pk.edu.nust.seecs.gradebook.bos;

import pk.edu.nust.seecs.gradebook.dao.CloDao;
import pk.edu.nust.seecs.gradebook.entity.Clo;

/**
 * Created by skrk on 4/26/17.
 */
public class CloBO {
    public CloDao cloDao;
    public Clo clo;

    public CloBO(){
        cloDao = new CloDao();
        clo = new Clo();
    }

}
