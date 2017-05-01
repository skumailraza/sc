package pk.edu.nust.seecs.gradebook.bos;

import pk.edu.nust.seecs.gradebook.dao.ContentDao;
import pk.edu.nust.seecs.gradebook.entity.Content;

/**
 * Created by skrk on 4/26/17.
 */
public class ContentBO {
    public ContentDao contentDao;
    public Content content;


    public ContentBO(){
        contentDao = new ContentDao();
        content = new Content();
    }
}
