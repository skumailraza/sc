import unittest
import restaurant as restaurant_system


class TestReservationSystem(unittest.TestCase):

    def test_reserve_twelve(self):
        db = restaurant_system.database_connection("localhost", "root", "root", "restaurant_system")
        db.connect()
        myRestraunt = restaurant_system.restraunt()
        myRestraunt.set_tables(1, 3, 8, 4)
        self.assertTrue(myRestraunt.book_table(12,0,12,3, db))
        self.assertTrue(myRestraunt.book_table(12, 0, 12, 3,db))
        self.assertFalse(myRestraunt.book_table(4, 0, 12, 5,db)) #Restraunt close at 4
        self.assertFalse(myRestraunt.book_table(21,0,12,2,db)) #Should be false since book time exceel close time

    def test_reserve_six(self):
        myRestraunt = restaurant_system.restraunt()
        myRestraunt.set_tables(1, 3, 8, 4)
        self.assertTrue(myRestraunt.book_table(12,0,6,2))
        self.assertTrue(myRestraunt.book_table(12, 4, 6, 4))
        self.assertTrue(myRestraunt.book_table(12, 4, 6, 4))
        self.assertTrue(myRestraunt.book_table(12, 4, 6, 4))
        self.assertTrue(myRestraunt.book_table(12, 4, 6, 4)) #Because only 3 large tables
    def test_reserve_4(self):
        myRestraunt = restaurant_system.restraunt()
        myRestraunt.set_tables(1, 3, 8, 4)
        self.assertTrue(myRestraunt.book_table(12, 0, 4, 2))
        self.assertTrue(myRestraunt.book_table(12, 4, 4, 4))
        self.assertFalse(myRestraunt.book_table(21,4,4,4))

    def test_reserve_2(self):
        myRestraunt = restaurant_system.restraunt()
        myRestraunt.set_tables(1, 3, 8, 4)
        self.assertTrue(myRestraunt.book_table(12, 0, 2, 2))
        self.assertTrue(myRestraunt.book_table(12, 4, 2, 4))
        self.assertFalse(myRestraunt.book_table(21,4,2,4))

    def test_book_after_close(self):
        myRestraunt = restaurant_system.restraunt()
        myRestraunt.set_tables(1, 3, 8, 4)
        self.assertFalse(myRestraunt.book_table(23, 0, 12, 2))
        self.assertFalse(myRestraunt.book_table(21, 4, 6, 4))
        self.assertFalse(myRestraunt.book_table(4, 4, 4, 4))

    def book_random(self):
        myRestraunt = restaurant_system.restraunt()
        myRestraunt.set_tables(1, 3, 8, 4)
        self.assertFalse(myRestraunt.book_table(23, 0, 12, 2))
        self.assertFalse(myRestraunt.book_table(21, 4, 6, 4))
        self.assertFalse(myRestraunt.book_table(4, 4, 4, 4))

    def test_authentication(self):
        myDb = restaurant_system.database_connection("localhost", "root", "root", "restraunt_system")
        myDb.connect()
        self.assertTrue(myDb.authenticate("admin", "admin"))
        self.assertFalse(myDb.authenticate("admin","24"))
        self.assertFalse(myDb.authenticate("assd",'sd'))

if __name__ == '__main__':
    unittest.main()