import numpy

maps = ["Altar of Flame",
		"Bannerfall",
		"Cauldron",
		"Convergence",
		"Disjunction",
		"Distant Shore",
		"Endless Vale",
		"Eternity",
		"Exodus Blue",
		"Fragment",
		"Javelin-4",
		"Midtown",
		"Pacifica",
		"Radiant Cliffs",
		"Rusted Lands",
		"The Anomaly",
		"The Burnout",
		"The Dead Cliffs",
		"The Fortress",
		"Twilight Gap",
		"Vostok",
		"Widow's Court",
		"Wormhaven"]
        
randomMap = numpy.random.randint(0, len(maps))
print(maps[randomMap])