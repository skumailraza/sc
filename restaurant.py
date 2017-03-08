import numpy as np
class restraunt:
    def __init__(self, open=1100, close = 2200, max_time = 30):
        self.__opentime = open
        self.__closetime = close
        self.__maxtime = max_time
        self.capacity={"extra_large":12, "large":6, "medium":4, "small":2}
        self.__booktable = None
    def set_tables(self, extra_large=0, large=0, medium=0, small=0):
        self.tables={"extra_large":extra_large, "large":large, "medium":medium, "small":small}
        if self.__booktable == None:
            self.__booktable = np.ones((30,sum(self.tables.values()),24))
            self.__booktable[:,:,0:self.__opentime/100] = 0
            self.__booktable[:, :, self.__closetime/100: 24] = 0

    def book_table(self, time, day, people, duration=2):
        temp = people
        people += people%2
        table =np.copy(self.__booktable)
        if people <=6:
            duration = 2
        if people >6 and people <= 12:
            if np.sum(table[day,0,time:time+duration]) == duration:
                table[day, 0, time:time + duration] = 0
                print "RESERVING ONE EXTRA LARGE TABLE FOR "+str(duration) +" hours from "+ str(time) +" on day " + str(day)
                people = people-12
        if people >4 :
            for a in range(0, self.tables["large"]):
                if np.sum(table[day,self.tables["extra_large"]+a,time:time+duration]) == duration and people >4:
                    table[day,self.tables["extra_large"]+a,time:time+duration] = 0
                    print "RESERVING ONE LARGE TABLE FOR " + str(duration) + " hours from " + str(
                        time) + " on day " + str(day)
                    people = people-6
        if people > 2 :
            for a in range(0, self.tables["medium"]):
                if people >2 and np.sum(table[day, self.tables["extra_large"]+self.tables["large"]+a, time:time+duration]) == duration:
                    table[day, self.tables["extra_large"]+self.tables["large"]+a, time:time+duration]=0
                    people = people-4
        if people > 0 :
           for a in range(0, self.tables["small"]):
               if people > 0 and np.sum(table[day, self.tables["medium"]+ self.tables["extra_large"]+self.tables["large"]+a, time:time+duration]) == duration:
                   table[day, self.tables["medium"]+self.tables["extra_large"]+self.tables["large"]+a, time:time+duration]=0
                   people = people-2

        if people <=0:
            people = temp
            people += people % 2  # This makes people even. Now we treat it as a coin change problem
            table = self.__booktable
            if people <= 6:
                duration = 2
            if people > 6 and people <= 12:
                if np.sum(table[day, 0, time:time + duration]) == duration:
                    table[day, 0, time:time + duration] = 0
                    print "RESERVING ONE EXTRA LARGE TABLE FOR " + str(duration) + " hours from " + str(
                        time) + " on day " + str(day)
                    people = people - 12
            if people > 4:
                for a in range(0, self.tables["large"]):
                    if np.sum(table[day, self.tables["extra_large"] + a, time:time + duration]) == duration and people > 4:
                        table[day, self.tables["extra_large"] + a, time:time + duration] = 0
                        print "RESERVING ONE LARGE TABLE FOR " + str(duration) + " hours from " + str(
                            time) + " on day " + str(day)
                        people = people - 6
            if people > 2:
                for a in range(0, self.tables["medium"]):
                    if people > 2 and np.sum(table[day, self.tables["extra_large"] + self.tables["large"] + a,
                                             time:time + duration]) == duration:
                        table[day, self.tables["extra_large"] + self.tables["large"] + a, time:time + duration] = 0
                        people = people - 4
            if people > 0:
                for a in range(0, self.tables["small"]):
                    if people > 0 and np.sum(
                            table[day, self.tables["medium"] + self.tables["extra_large"] + self.tables["large"] + a,
                            time:time + duration]) == duration:
                        table[day, self.tables["medium"] + self.tables["extra_large"] + self.tables["large"] + a,
                        time:time + duration] = 0
                        people = people - 2
            if people <= 0:
                return True


        return False

    def get_table(self):
        return self.__booktable


