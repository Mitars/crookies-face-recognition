def get_fps(now, old):
    global frame_count
    global time_delta

    frame_count += 1
    time_delta += (now - old).microseconds / (1000 * 1000)

    fps = frame_count / time_delta

    if frame_count == 1:
        time_delta = 0

    return fps


frame_count = 0
time_delta = 0
