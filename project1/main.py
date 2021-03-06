from Stack import Stack
from Stack import browse_web, backward, forward, visit


def main():

    print("-----TEST 1-----")
    back = Stack(homepage="www.google.com")
    forw = Stack()
    back.push("www.reddit.com")
    back.push("www.reddit.com/r/wheredidthesodago/")
    visit(back, forw, "www.reddit.com/r/dataisbeautiful/")
    visit(back, forw, "www.reddit.com/r/ProgrammerHumor/")
    back.pop()  # Programmer Humor
    forw.pop()  # None
    visit(back, forw, 1231.23)  # Error
    visit(back, forw, "www.reddit.com/r/iamverysmart/")
    back.pop()
    print("Back: ", back)
    print("Forward: ", forw)

    print("\n-----TEST 2-----")
    back = Stack(homepage="www.google.com")
    forw = Stack()
    visit(back, forw, "www.gmail.com")
    visit(back, forw, "www.egr.msu.edu")
    backward(back, forw)
    print("Back: ", back)
    print("Forward: ", forw)
    visit(back, forw, "www.google.com")
    visit(back, forw, "www.reddit.com/r/ethereum")
    backward(back, forw)
    backward(back, forw)
    backward(back, forw)
    backward(back, forw) #  Extra should do nothing
    backward(back, forw) #  Extra should do nothing
    print("Back: ", back)
    print("Forward: ", forw)

    print("\n-----TEST 3-----")
    back = Stack(homepage="www.google.com")
    forw = Stack()
    visit(back, forw, "www.gmail.com")
    visit(back, forw, "www.egr.msu.edu")
    backward(back, forw)
    visit(back, forw, "www.google.com")
    visit(back, forw, "www.reddit.com/r/ethereum")
    print("Back: ", back)
    print("Forward: ", forw)
    backward(back, forw)
    backward(back, forw)
    backward(back, forw)
    visit(back, forw, ["www.twitter.com/yash__v"])  # Error
    print("Back: ", back)
    print("Forward: ", forw)
    forward(back, forw)
    forward(back, forw)
    forward(back, forw)
    print("Back: ", back)
    print("Forward: ", forw)

    print("\n-----TEST 4-----")
    back = Stack(homepage="www.google.com")
    forw = Stack()
    visit(back, forw, "www.gmail.com")
    visit(back, forw, "www.egr.msu.edu")
    backward(back, forw)
    visit(back, forw, "www.facebook.com")
    visit(back, forw, "www.reddit.com/r/ethereum")
    print("Back: ", back)
    print("Forward: ", forw)
    backward(back, forw)
    backward(back, forw)
    backward(back, forw)
    print("Back: ", back)
    print("Forward: ", forw)
    forward(back, forw)
    visit(back, forw, ["www.twitter.com/yash__v"])  # Error
    browse_web(back, forw, "www.gmail.com")
    browse_web(back, forw, "www.facebook.com")
    print("Back: ", back)
    print("Forward: ", forw)
    browse_web(back, forw, "www.google.com")
    print("Back: ", back)
    print("Forward: ", forw)

    print("\n-----TEST 5-----")
    back = Stack(homepage="www.google.com")
    forw = Stack()
    visit(back, forw, "www.gmail.com")
    visit(back, forw, "www.egr.msu.edu")
    backward(back, forw)
    visit(back, forw, "www.facebook.com")
    visit(back, forw, "www.reddit.com/r/ethereum")
    print("Back: ", back)
    print("Forward: ", forw)
    backward(back, forw)
    backward(back, forw)
    backward(back, forw)
    print("Back: ", back)
    print("Forward: ", forw)
    forward(back, forw)

    browse_web(back, forw, "www.gmail.com")
    browse_web(back, forw, "www.facebook.com")
    print("Back: ", back)
    print("Forward: ", forw)
    browse_web(back, forw, "www.google.com")
    print("Back: ", back)
    print("Forward: ", forw)

if __name__ == "__main__":
    main()
