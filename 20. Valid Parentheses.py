class Solution:
    def isValid(self, inputString: str) -> bool:
        openBracketStack = []
        matchingOpenBracket = {')': '(', '}': '{', ']': '['}

        for currentBracket in inputString:
            if currentBracket in matchingOpenBracket:
                topBracket = openBracketStack.pop() if openBracketStack else '#'
                if matchingOpenBracket[currentBracket] != topBracket:
                    return False
            else:
                openBracketStack.append(currentBracket)

        return not openBracketStack
