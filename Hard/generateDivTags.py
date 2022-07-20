def generateDivTags(numberOfTags):
    tags = []
    generateDivTagsHelper(numberOfTags, 0, 0, '', tags)
    return tags

def generateDivTagsHelper(numberOfTags, numberOfOpeningTags, numberOfClosingTags, string, tags):
    if numberOfOpeningTags == numberOfClosingTags:
        if numberOfOpeningTags == numberOfTags:
            tags.append(string)
        else:
            generateDivTagsHelper(numberOfTags, numberOfOpeningTags + 1, numberOfClosingTags, string + '<div>', tags)
    elif numberOfOpeningTags == numberOfTags:
        generateDivTagsHelper(numberOfTags, numberOfOpeningTags, numberOfClosingTags + 1, string + '</div>', tags)
    else:
        generateDivTagsHelper(numberOfTags, numberOfOpeningTags + 1, numberOfClosingTags, string + '<div>', tags)
        generateDivTagsHelper(numberOfTags, numberOfOpeningTags, numberOfClosingTags + 1, string + '</div>', tags)
