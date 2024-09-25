    def pop(self):
        if self.length == 0:
            print("list is empty")
        elif self.length == 1:
            self.head=None
            self.tail=None
        else:
            pre=self.head
            temp=self.head.next
            while(temp is not None):
                pre=self.head.next
            else:
                self.tail=pre
                self.tail.next=None
                return temp
            