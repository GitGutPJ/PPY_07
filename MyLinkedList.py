class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.nextE
        return " ".join(result)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return
        if self.head.data == e:
            self.head = self.head.nextE
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        current = self.head
        while current.nextE:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                if current.nextE is None:
                    self.tail = current
                self.size -= 1
                return
            current = current.nextE

    def append(self, e, func=None):
        element = Element(e)
        if self.head is None:
            self.head = element
            self.tail = element
            self.size += 1
            return
        if func is None:
            func = lambda a, b: a >= b
        if func(self.tail.data, e):
            self.tail.nextE = element
            self.tail = element
            self.size += 1
            return
        current = self.head
        previous = None
        while current:
            if func(e, current.data):
                element.nextE = current
                if previous is None:
                    self.head = element
                else:
                    previous.nextE = element
                self.size += 1
                return
            previous = current
            current = current.nextE
