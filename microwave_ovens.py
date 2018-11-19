class MicrowaveBase:
    def __init__(self):
        self.time = 0

    def __repr__(self):
        return f"{int(self.time) // 60:02d}:{int(self.time) % 60:02d}"

    def normalize(self):
        self.time = 90 * 60 if self.time > 90 * 60 else self.time
        self.time = 0 if self.time < 0 else self.time

    def set_time(self, time):
        minutes, _, seconds = time.partition(":")
        self.time = int(minutes) * 60 + int(seconds)
        self.normalize()

    def add_time(self, time: str):
        inc = 60 if time[-1:] == 'm' else 1
        self.time += int(time[:-1]) * inc
        self.normalize()

    def del_time(self, time: str):
        inc = 60 if time[-1:] == 'm' else 1
        self.time -= int(time[:-1]) * inc
        self.normalize()

class Microwave1(MicrowaveBase):
    def show_time(self):
        time_list = list(str(self))
        time_list[0] = '_'
        return "".join(time_list)

class Microwave2(MicrowaveBase):
    def show_time(self):
        time_list = list(str(self))
        time_list[-1] = '_'
        return "".join(time_list)

class Microwave3(MicrowaveBase):
    def show_time(self):
        return str(self)

class RemoteControl:
    def __init__(self, micro):
        self.micro = micro

    def add_time(self, time: str):
        self.micro.add_time(time)

    def del_time(self, time: str):
        self.micro.del_time(time)

    def set_time(self, time: str):
        self.micro.set_time(time)

    def show_time(self):
        print(self.micro.show_time())
        return self.micro.show_time()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")