print("                          Rumah Sakit Husein")
print("                   __________________________________")

class Node:
    def __init__(self,urut = None):
        self.pasien =urut
        self.next_node = None


class MyLinkedList:
    def __init__(self):
        self.main_value = None

    def print_data(self):
        hospital = self.main_value
        while hospital != None:
            print(hospital.pasien)
            hospital = hospital.next_node

    def insert_first(self,new_value):
        node_baru = Node(new_value)
        node_baru.next_node = self.main_value
        self.main_value = node_baru

    def insert_last(self, new_value):
        node_baru = Node(new_value)
        node_akhir = self.main_value
        while node_akhir.next_node is not None:
            node_akhir= node_akhir.next_node

        node_akhir.next_node = node_baru

    def remove_first(self):
        node = self.main_value
        self.main_value = node.next_node
        del node



mylist = MyLinkedList()
mylist.main_value = Node(1)
n2 = Node(2)
n3 = Node(3)

mylist.main_value.next_node = n2
n2.next_node = n3

mylist.insert_last(4)
print("\n No Urut Antrian Pasien")
print("----------------------")
mylist.print_data()
print("\n Antrian Selanjutnya")
print("----------------------")
mylist.remove_first()
mylist.print_data()