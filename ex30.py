people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars<people:
    print "We should not taket the cars"
else:
    print "we can't decide"

if buses > cars:
    print "That's too many cars"
elif buses <cars:
    print "Maybe we could take the buses"
else:
    print "We still can't decide"

if people > buses:
    print "Alright, let's just take the buses"
else:
    print "Fine, let's stay at home then"
