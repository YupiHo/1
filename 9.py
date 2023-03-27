def twelve_days(day):
    print("On the",day,"day of christmas,\nmy true love sent to me")
    def first():
            print("A partridge in a pear tree.\n")
    def second():
            print("Two turtle doves,\nAnd a partridge in a pear tree.\n")
    def third():
            print("Three French hens,")
            second()
    def fourth():
            print("Four calling birds,")
            third()
    def fifth():
            print("Five golden rings,")
            fourth()
    def sixth():
            print("Six geese a-laying,")
            fifth()
    def seventh():
            print("Seven swans a-swimming,")
            sixth()
    def eighth():
            print("Eight maids a-milking,")
            seventh()
    def ninth():
            print("Nine ladies dancing,")
            eighth()
    def tenth():
            print("Ten lords a-leaping,")
            ninth()
    def eleventh():
            print("Eleven pipers piping,")
            tenth()
    def twelfth():
            print("Twelve drummers drumming,")
            eleventh()
    if day == 1:
        first()
    if day == 2:
        second()
    if day == 3:
        third()
    if day == 4:
        fourth()
    if day == 5:
        fifth()
    if day == 6:
        sixth()
    if day == 7:
        seventh()
    if day == 8:
        eighth()
    if day == 9:
        ninth()
    if day == 10:
        tenth()
    if day == 11:
        eleventh()
    if day == 12:
        twelfth()
            
twelve_days(1)
twelve_days(2)
twelve_days(3)
twelve_days(4)
twelve_days(5)
twelve_days(6)
twelve_days(7)
twelve_days(8)
twelve_days(9)
twelve_days(10)
twelve_days(11)
twelve_days(12)