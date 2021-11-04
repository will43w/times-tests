from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

def test_nonoverlapping_input():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")

    result = compute_overlap_time(range1, range2)
    expected = []

    assert result == expected

def test_just_overlapping_input():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    result = compute_overlap_time(range1, range2)
    expected = []

    assert result == expected

def test_several_intervals_each():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:40:00", 3, 300) # 10:00 -> 10:10, 10:15 -> 10:25, 10:30 -> 10:40
    range2 = time_range("2010-01-12 10:05:00", "2010-01-12 10:45:00", 3, 300) # 10:05 -> 10:15, 10:20 -> 10:30, 10:35 -> 10:45

    result = compute_overlap_time(range1, range2)
    expected = [("2010-01-12 10:05:00", "2010-01-12 10:10:00"), ("2010-01-12 10:20:00", "2010-01-12 10:25:00"), ("2010-01-12 10:35:00", "2010-01-12 10:40:00")]

    assert result == expected

    