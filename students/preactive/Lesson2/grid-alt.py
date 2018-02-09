def formation(gridSize, gridMulti):
    plusEl = "+ "
    mEl    = "- "
    sEl    = "  "
    pipeEl = "| "
    nlFeed = "\n"

    plusSec = plusEl + mEl * gridSize
    pipeSec = pipeEl + sEl * gridSize

    plusRow  = plusSec * gridMulti + plusEl + nlFeed
    pipeRows = pipeSec * gridMulti + pipeSec + nlFeed

    gridFinal = plusRow + (pipeRows * gridSize + plusRow) * gridMulti

    print(gridFinal)

formation(0,0)
formation(1,1)
formation(2,2)
formation(3,3)

# The frusteration and hours that I had in Grid.py trying to slove with logic operators
# and hundreds of lines of failed code then I figured this out on the train in 15 min.  AHHHHHH!!!!!