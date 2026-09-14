def ai_recommendation(trains, assets, section, duration):

    available_assets = [
        asset for asset in assets
        if asset["status"].lower() == "available"
    ]

    recommendations = []

    for start in range(0, 24 - duration + 1):
        end = start + duration
        conflicts = 0

        for train in trains:
            train_start = int(train["start_time"])
            train_end = int(train["end_time"])

            if start < train_end and end > train_start:
                conflicts += 1

        score = conflicts * 10

        if len(available_assets) == 0:
            score += 20

        recommendations.append({
            "start": start,
            "end": end,
            "conflicts": conflicts,
            "score": score
        })

    best = min(recommendations, key=lambda x: x["score"])

    return best