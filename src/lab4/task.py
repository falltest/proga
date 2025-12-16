import copy
from collections import defaultdict

ans = []
correct_ans = []

class Order:
    def __init__(self, id : str, nabor : str, FIO : str, address : str, phone : str, priority):
        self.id = id
        self.nabor = nabor
        self.FIO = FIO
        self.address = address
        self.phone = phone
        self.priority = priority
        self.error_number = None

    def __repr__(self):
        if self.error_number == 1:
            return f"{self.id};{self.error_number};{self.address}"
        elif self.error_number == 2:
            return f"{self.id};{self.error_number};{self.phone}"
        else:
            return f"{self.id};{self.nabor};{self.FIO};{self.address};{self.phone};{self.priority}"

    @classmethod
    def str_decode(cls, raw_string: str):
        parts = raw_string.strip().split(';')
        id = parts[0]
        nabor = parts[1]
        FIO = parts[2]
        address = parts[3]
        phone = parts[4]
        priority = parts[5]
        return cls(id, nabor, FIO, address, phone, priority)

    def process(self) -> list:
        error_address = False
        error_tel = False
        if len(self.address) == 0:
            error_address = True

        parts_address = self.address.split('.')
        if len(parts_address) != 4:
            error_address = True
        else:
            for el in parts_address:
                if len(el) == 0:
                    error_address = True

        if self.phone[0] == '+':
            len_tel = [1, 3, 3, 2, 2]
            parts_tel = self.phone[1:].split('-')
            if len(parts_tel) != len(len_tel):
                error_tel = True
            else:
                for i in range(len(len_tel)):
                    if len(parts_tel[i]) != len_tel[i]:
                        error_tel = True
        else:
            error_tel = True

        if error_tel:
            self.error_number = 2
            ans.append(copy.copy(self))

        if error_address:
            self.error_number = 1
            ans.append(copy.copy(self))

    def comfy_list(self) -> str:
        d = defaultdict(int)
        parts = [item.strip() for item in self.nabor.split(',')]
        for el in parts:
            d[el] += 1

        result = []
        for name, count in d.items():
            if count > 1:
                result.append(f"{name} x{count}")
            else:
                result.append(name)

        return ", ".join(result)

rules = {'LOW' : 1, 'MIDDLE' : 2, 'MAX' : 3}
with open('orders.txt', 'r', encoding='utf-8') as file_in:
    for line in file_in:
        order = Order.str_decode(line)
        order.process()
        if order.error_number is None:
            correct_ans.append(order)

with open('non_valid_orders.txt', 'w', encoding='utf-8') as file_out:
    ans.sort(key=lambda x: (x.address.split('.')[0], -rules[x.priority]))
    empty_addresses = []
    for el in ans:
        if len(el.address) == 0:
            empty_addresses.append(el)
        else:
            print(el, file=file_out)
    for el in empty_addresses:
        el.address = 'no data'
        print(el, file=file_out)

with open('order_country.txt', 'w', encoding='utf-8') as file_out:
    correct_ans.sort(
        key=lambda x: (x.address.split('.')[0] != "Россия" and x.address.split('.')[0] != "Российская Федерация",
                       x.address.split('.')[0], -rules[x.priority]))

    for el in correct_ans:
        el.nabor = el.comfy_list()

        addr_parts = el.address.split('.')
        if len(addr_parts) > 1:
            el.address = ". ".join([p.strip() for p in addr_parts[1:]])

        print(el, file=file_out)
