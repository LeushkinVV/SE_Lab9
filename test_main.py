from main import get_avg
def test_get_avg_test_avg():
    lines = [
        '0,1,Pcalss,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,12.2,0',
        '2,0,1,0,0,0,2.2,0',
        '3,0,2,0,0,0,32,0',
        '4,0,2,0,0,0,42,0',
        '5,0,3,0,0,0,22,0',
        '6,0,3,0,0,0,44.2,0',
    ]
    sibsp = 0
    assert get_avg(lines,sibsp) == [7.2, 37, 33.1]


def test_get_avg_test_age_false():
    lines = [
        '0,1,Pcalss,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,12.2,0',
        '2,0,1,0,0,0,,0',
        '3,0,2,0,0,0,32,0',
        '4,0,2,0,0,0,42,0',
        '5,0,3,0,0,0,,0',
        '6,0,3,0,0,0,44.2,0',
    ]
    sibsp = 0
    assert get_avg(lines,sibsp) == [12.2, 37, 44.2]


def test_get_avg_test_filter():
    lines = [
        '0,1,Pcalss,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,12.2,0',
        '2,0,1,0,0,0,2.2,1',
        '3,0,2,0,0,0,32,2',
        '4,0,2,0,0,0,42,3',
        '5,0,3,0,0,0,22,4',
        '6,0,3,0,0,0,44.2,5',
    ]
    sibsp = 0
    assert get_avg(lines,sibsp) == [12.2, 0, 0]