import time

import retrace


count = [0, ]


def limit(attempt_number):
    print "Current attempt: {}".format(attempt_number)
    print "Limiter, I will stop this if we go over 5 attempts."
    if attempt_number > 5:
        raise retrace.LimitReached()


def interval(attempt_number):
    print "Adding a delay between attempts, increasing by one second."
    time.sleep(attempt_number * 0.1)


@retrace.retry(limit=limit, interval=interval)
def unstable(pass_at):

    count[0] += 1

    if count[0] < pass_at:
        print "FAILING"
        time.sleep(1)
        raise Exception("FAIL")

    return "PASSING"


print "Calling unstable. Example 1"
print unstable(5)

count[0] = 0

print "\n\n\n"
print "Calling unstable. Example 2"
print unstable(10)