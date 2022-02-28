
def make_divisions_by(num):

    def division(x) -> float:
        assert type(x) != str , "el valor debe ser un número"
        return x/num
    return division


def run():
    division_by_3 = make_divisions_by(3)
    division_by_5 = make_divisions_by(5)
    division_by_18 = make_divisions_by(18)
    print(division_by_18(36))
    print(division_by_5(36))
    print(division_by_3(10))


if __name__ == "__main__":
    run()