def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int) or not all(
        isinstance(t, tuple)
        and len(t) == 2
        and isinstance(t[0], int)
        and isinstance(t[1], int)
        for t in permanence_period
    ):
        return None

    target_time_count = 0

    for study_time, max_study_time in permanence_period:
        if study_time <= target_time <= max_study_time:
            target_time_count += 1

    return target_time_count
