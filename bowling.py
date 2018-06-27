# scoresheet.txt should contain full lines of bowling separated by \n
file = open("scoresheet.txt", "r")
bowls = file.readline()

while bowls != '':
    score = 0
    multiplier = [1, 1, 1]
    currBowl = ''
    prevBowl = ''
    frame = 1
    firstBowl = True

    # Evaluate each bowl (not including final \n character)
    for i in range(len(bowls) - 1):
            prevBowl = currBowl
            currBowl = bowls[i]

            # make misses easier to work with
            if currBowl == '-':
                currBowl = '0'

            # if bowl is a strike add 10 (plus multipliers) to the score and
            # increase the multiplier for next two bowls
            if currBowl == 'X':
                score += 10 * multiplier[0]

                # frame 10 doesn't add multipliers, but rather extra bowls
                if frame < 10:
                    multiplier[1] += 1
                    multiplier[2] += 1

                frame += 1
                firstBowl = True

            # if bowl is a spare add remaining pins (plus multipliers) to the score
            # and increase the multiplier for next bowls
            elif currBowl == '/':
                score += (10 - int(prevBowl)) * multiplier[0]

                # frame 10 doesn't add multipliers, but rather extra bowls
                if frame < 10:
                    multiplier[1] += 1

                frame += 1
                firstBowl = True

            # otherwise simply add bowl (plus multipliers) to score only increment
            # frame count if this is the second bowl
            else:
                score += int(currBowl) * multiplier[0]
                
                if firstBowl:
                    firstBowl = not firstBowl
                else:
                    firstBowl = not firstBowl
                    frame += 1

            # move multipliers down and set newest one to 1
            multiplier[0] = multiplier[1]
            multiplier[1] = multiplier[2]
            multiplier[2] = 1

    # print final score and read next line
    print(score)
    bowls = file.readline()
