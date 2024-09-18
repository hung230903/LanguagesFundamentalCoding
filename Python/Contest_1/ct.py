def schedule_talks(talks):
    talks.sort(key=lambda x: x[1])
    
    scheduled_talks = []
    prev_end_time = 0
    
    for talk in talks:
        start_time, end_time = talk
        if start_time >= prev_end_time:
            scheduled_talks.append(talk)
            prev_end_time = end_time
    
    return scheduled_talks

talks = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
scheduled_talks = schedule_talks(talks)
print("Scheduled talks:")
for talk in scheduled_talks:
    print("Start:", talk[0], "End:", talk[1])
