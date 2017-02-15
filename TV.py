import os
import urllib2


class Channel:
    def __init__(self):
        self.data = None # contains the data
        self.info = None # description
        self.link = None # link url
        self.next = None # contains the reference to the next node


class TV_Manager:
    def __init__(self):
        self.cur_node = None

    def add_channel(self, data, discr, vlink):
        new_node = Channel() # create a new node
        new_node.data = data #setters
        new_node.info = discr
        new_node.link = vlink
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        print("\nChannel: ") 
        print("\n__________________")

        while node:
            print node.data #printing all channels
            node = node.next
        print("\n__________________\n")

    def replace_channel(self, old_data, new_data, new_info, new_link):
        node = self.cur_node    #replace channels
        while node:
            if(node.data == old_data):
                node.data = new_data
                node.info = new_info
                node.link = new_link
            node = node.next

    def remove_channel(self, name): #removing channels
        node = self.cur_node
        while node:
            if(node.next.data == name):
                temp = node.next
                node.next.data = None
                node.next.info = None
                node.next.link = None
                node.next = node.next.next
            node = node.next
            if(node.next == None):
                print("\n**** Channel Not Found! ****\n")
            
    def print_channel(self,name): #printing channel's description
        node = self.cur_node
        print("\nChannel: ")
        print("\n__________________")
        while node:
            if(node.data == name):
                ret_data = str("\nName: ") + str(node.info) + str("\nLink:") + str(node.link)
                return ret_data
            if(node.next == None):
                return 'Channel Not found!'
            node = node.next
        print("\n__________________")
    def watch(self, name):
        webbrowser.open('https://www.youtube.com/watch?v=f-gx5zIbDg4')


# ****** MAIN FUNCTION **********

ll = TV_Manager()   # a new TV manager
# Adding Channels Manually
ll.add_channel('Air Crash Investigation','Air Crash Investigation Series Videos. Also known as Mayday. Browse through them','https://www.youtube.com/user/dcbuza/videos')
ll.add_channel('Top Gear','Want to watch a bit of Top Gear on the interweb? Welcome to the most comprehensive collection of official clips youll find on YouTube. All the iconic films are here - from Richards epic race against the Eurofighter to Clarksons office drive in that tiny Peel P50. You can also relive the boys biggest challenges - including amphibious cars and that trip across America. Add to that a bunch of stars in our reasonably priced car, the odd explosive stunt and a ton of Stig power laps and everythings covered. Just browse using our playlists for comprehensive clip listings or search by most viewed or discussed. And dont forget that theres shedloads more clips in the video vault at http://www.topgear.com','https://www.youtube.com/user/TopGear/videos')
ll.add_channel('The Grand Tour','An Amazon original motoring series with Jeremy Clarkson, Richard Hammond and James May.', 'https://www.youtube.com/channel/UCZ1Sc5xjWpUnp_o_lUTkvgQ/videos')
ll.list_print()

# USER INTERFACE
while(1):
    quer = str("\nPlease Enter:") + str("\n1 to Add Channel") + str("\n2 to remove channel") + str("\n3 to replace a channel") + str("\n4 to Show Channels") + str("\n5 to Watch a channel") + str("\n6 to View Description\n")
    inp = input(quer)

    if(inp == 1):
        name = raw_input("Channel Name: ")
        data = raw_input("Channel Description: ")
        link = raw_input("Channel Link: ")
        ll.add_channel(name, data, link)
    if(inp == 2):
        name = raw_input("Channel Name: ")
        ll.remove_channel(name)
    if(inp == 3):
        old_name = input("Enter Channel's Name: ")
        name = raw_input("Enter New Name: ")
        discr = raw_input("Enter Description: ")
        link = raw_input("Enter link: ")
        ll.replace_channel(old_name, name, discr, link)
    if(inp == 4):
        ll.list_print()
    if(inp == 5):
        name = raw_input("Enter Channel's name: ")
        ll.watch(name)
    if(inp == 6):
        name = raw_input("Enter Channel's name: ")
        print ll.print_channel(name)
    continue


